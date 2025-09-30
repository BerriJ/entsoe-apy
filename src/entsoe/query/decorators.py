from functools import wraps
import io
from time import sleep
import zipfile

from httpx import RequestError, Response
from loguru import logger
from pydantic import BaseModel

from ..config.config import get_config
from ..utils.utils import check_date_range_limit, split_date_range


class AcknowledgementDocumentError(Exception):
    """Raised when the API returns an acknowledgement document indicating an error."""

    pass


class ServiceUnavailableError(Exception):
    """Raised when the ENTSO-E API returns a 503 Service Unavailable status."""

    pass


def unzip(func):
    """
    Decorator that handles ZIP responses from the ENTSO-E API.

    Wraps query functions to automatically extract ZIP content when the API
    returns application/zip content-type. Each file in the ZIP archive is
    extracted and converted to a separate Response object, preserving the
    original response metadata.

    Returns:
        List of Response objects - one for each file found in the ZIP archive,
        or the original response list if the content is not a ZIP file.
    """

    @wraps(func)
    def unzip_wrapper(*args, **kwargs) -> list[Response]:
        # Call the original function to get the list of responses
        response_list = func(*args, **kwargs)

        # Since query_core returns a list, get the first (and typically only) response
        response = response_list[0]

        # Check if response is ZIP format
        if response.headers.get("Content-Type") == "application/zip":
            logger.debug("Response is ZIP format, extracting XML content")
            # Create a BytesIO object from the response content
            zip_buffer = io.BytesIO(response.content)

            # Open the ZIP file and extract XML files
            with zipfile.ZipFile(zip_buffer, "r") as zip_file:
                file_names = zip_file.namelist()

                logger.debug(f"Found {len(file_names)} files in ZIP: {file_names}")

                responses: list[Response] = []

                for file_name in file_names:
                    with zip_file.open(file_name) as xml_file:
                        xml_content = xml_file.read().decode("utf-8")

                    # Create a copy of the original response for each file
                    # Create a new Response object with the required attributes
                    new_response = Response(
                        status_code=response.status_code,
                        headers={
                            **response.headers,
                            "Content-Type": "text/xml; charset=utf-8",
                        },
                        content=xml_content.encode("utf-8"),
                        request=response.request,
                    )
                    responses.append(new_response)
                    logger.debug(
                        f"Created Response object for {file_name} ({len(xml_content)} characters)"
                    )

                return responses
        else:
            logger.debug("Response is not ZIP returning original response")
            return response_list

    return unzip_wrapper


def range_limited(func):
    """
    Decorator that handles range limit errors by splitting the requested period
    and combining the results.

    Catches cases where the date range exceeds the API's 1-year limit, splits
    the requested period in two, and makes recursive calls. The results from
    both halves are combined into a single list of BaseModel instances.

    Returns:
        List of BaseModel instances from all time periods combined.
    """

    @wraps(func)
    def range_wrapper(params, max_days_limit=365, *args, **kwargs):
        # Extract period parameters from params dict
        period_start = params.get("periodStart")
        period_end = params.get("periodEnd")

        # If no period parameters, just call the function normally
        if period_start is None or period_end is None:
            logger.debug("No period parameters found, calling function directly")
            return func(params, max_days_limit, *args, **kwargs)

        logger.debug(f"Range_limited decorator called for function: {func.__name__}")
        logger.debug(f"Period range: {period_start} to {period_end}")
        logger.debug(f"Using max_days_limit: {max_days_limit}")

        # Check if the range exceeds the limit
        if check_date_range_limit(period_start, period_end, max_days=max_days_limit):
            logger.debug(f"Range exceeds {max_days_limit} days, splitting range")

            # Split the range and make recursive calls
            pivot_date = split_date_range(
                period_start, period_end, max_days=max_days_limit
            )
            logger.debug(f"Split at pivot date: {pivot_date}")

            # Create new params for the first half
            params1 = params.copy()
            params1["periodEnd"] = pivot_date
            logger.debug(
                f"First half: {params1['periodStart']} to {params1['periodEnd']}"
            )

            # Create new params for the second half
            params2 = params.copy()
            params2["periodStart"] = pivot_date
            logger.debug(
                f"Second half: {params2['periodStart']} to {params2['periodEnd']}"
            )

            # Recursively call for both halves
            logger.debug("Making recursive call for first half")
            result1 = range_wrapper(params1, max_days_limit, *args, **kwargs)
            logger.debug("Making recursive call for second half")
            result2 = range_wrapper(params2, max_days_limit, *args, **kwargs)

            logger.debug("Merging results from both halves")
            return [*result1, *result2]

        else:
            # Range is within limit, make the API call
            logger.debug(f"Range within {max_days_limit} days, making API call")
            return func(params, max_days_limit, *args, **kwargs)

    return range_wrapper


def acknowledgement(func):
    """
    Decorator that handles acknowledgement documents from the ENTSO-E API.

    Checks if the API response contains an acknowledgement document indicating
    an error or "No matching data found" condition. Returns None for "No matching
    data found" cases, or raises an AcknowledgementDocumentError for other error
    conditions.

    Returns:
        The original BaseModel instance, or None if no data was found.

    Raises:
        AcknowledgementDocumentError: For acknowledgement documents containing errors
    """

    @wraps(func)
    def ack_wrapper(params, *args, **kwargs) -> BaseModel | None:
        logger.debug(f"acknowledgement decorator called for function: {func.__name__}")

        xml_model = func(params, *args, **kwargs)
        name = type(xml_model).__name__

        logger.debug(f"Received response with name: {name}")

        if "acknowledgementmarketdocument" in name.lower():
            logger.debug("Response contains acknowledgement document")
            reason = xml_model.reason[0].text
            logger.debug(f"Acknowledgement reason: {reason}")

            if "No matching data found" in reason:
                logger.debug(reason)
                logger.debug("Returning None")
                return None
            else:
                for reason in xml_model.reason:
                    logger.error(reason.text)
                raise AcknowledgementDocumentError(xml_model.reason)

        logger.debug("Acknowledgement check passed, returning xml_model")
        return xml_model

    return ack_wrapper


def pagination(func):
    """
    Decorator that handles pagination for API requests with large result sets.

    When an 'offset' parameter is present, this decorator automatically
    makes multiple API calls with increasing offset values (0, 100, 200, etc.)
    until all data is retrieved. Results from all pages are combined into
    a single list.

    Returns:
        List of BaseModel instances from all paginated results combined.
    """

    @wraps(func)
    def pagination_wrapper(params, *args, **kwargs):
        logger.debug(f"pagination decorator called for function: {func.__name__}")

        # Check if offset is in params (indicating pagination may be needed)
        if "offset" not in params:
            logger.debug("No offset parameter found, calling function directly")
            return func(params, *args, **kwargs)

        logger.debug("Offset parameter found, starting pagination")

        merged_result = []

        for offset in range(0, 4801, 100):  # 0 to 4800 in increments of 100
            logger.debug(f"Processing pagination offset: {offset}")
            params["offset"] = offset

            result = func(params, *args, **kwargs)

            if not result:
                logger.debug("Received empty result, pagination complete")
                break

            # Add results to accumulated list
            merged_result.extend(result)
            logger.debug(
                f"Added {len(result)} results, total accumulated: {len(merged_result)}"
            )

        logger.debug(
            f"Pagination completed, returning {len(merged_result)} total results"
        )
        return merged_result

    return pagination_wrapper


def service_unavailable(func):
    """
    Decorator that handles 503 Service Unavailable responses from the ENTSO-E API.

    Checks if any response in the returned list has a 503 status code, logs an error,
    and raises a ServiceUnavailableError with details about the service status.

    Returns:
        The original list of Response objects if no 503 responses are found.

    Raises:
        ServiceUnavailableError: When any response has a 503 Service Unavailable status
    """

    @wraps(func)
    def service_unavailable_wrapper(*args, **kwargs) -> list[Response]:
        logger.debug(
            "service_unavailable decorator called for function: {}", func.__name__
        )

        # Call the original function to get the list of responses
        response_list = func(*args, **kwargs)

        # Check each response for 503 status
        for response in response_list:
            if response.status_code == 503:
                logger.error("ENTSO-E API returned 503 Service Unavailable.")
                raise ServiceUnavailableError(
                    "ENTSO-E API is currently unavailable (HTTP 503). Please try again later."
                )

        logger.debug("No 503 Service Unavailable responses found")
        return response_list

    return service_unavailable_wrapper


def retry(func):
    """
    Decorator that catches connection errors, service unavailable errors, waits and retries.

    Args:
        retry_count: Number of retry attempts (default: 3)
        retry_delay: Wait time between retries in seconds (default: 10)
    """

    @wraps(func)
    def retry_wrapper(*args, **kwargs):
        config = get_config()
        last_exception = None

        for attempt in range(config.retries):
            try:
                result = func(*args, **kwargs)
                return result
            # Catch connection errors, socket errors, and service unavailable errors
            except (RequestError, ServiceUnavailableError) as e:
                last_exception = e
                if isinstance(e, ServiceUnavailableError):
                    logger.warning(
                        f"Service Unavailable Error on attempt {attempt + 1}/{config.retries}: "
                        f"{e}. Retrying in {config.retry_delay(attempt)} seconds..."
                    )
                else:
                    logger.warning(
                        f"Connection Error on attempt {attempt + 1}/{config.retries}: "
                        f"{e}. Retrying in {config.retry_delay(attempt)} seconds..."
                    )
                if attempt < config.retries - 1:  # Don't sleep on the last attempt
                    sleep(config.retry_delay(attempt))
                continue

        # If we've exhausted all retries, raise the last exception
        logger.error(f"All {config.retries} retry attempts failed")
        if last_exception:
            raise last_exception
        else:
            raise RuntimeError("All retry attempts failed with unknown error")

    return retry_wrapper

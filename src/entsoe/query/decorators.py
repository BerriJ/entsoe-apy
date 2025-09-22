from functools import wraps
from time import sleep

import httpx
from loguru import logger

from ..config.config import get_config
from ..utils.utils import check_date_range_limit, merge_documents, split_date_range


class AcknowledgementDocumentError(Exception):
    """Raised when the API returns an acknowledgement document indicating an error."""

    pass


def range_limited(func):
    """
    Decorator that handles range limit errors by splitting the requested period
    and merging the results.

    Catches a RangeLimitError, splits the requested period in two and tries
    again. Finally it merges the results using merge_documents.
    """

    @wraps(func)
    def range_wrapper(params, *args, **kwargs):
        # Extract period parameters from params dict
        period_start = params.get("periodStart")
        period_end = params.get("periodEnd")

        # If no period parameters, just call the function normally
        if period_start is None or period_end is None:
            logger.debug("No period parameters found, calling function directly")
            return func(params, *args, **kwargs)

        logger.debug(f"Range_limited decorator called for function: {func.__name__}")
        logger.debug(f"Period range: {period_start} to {period_end}")

        # Check if the range exceeds the limit (1 year = 365 days)
        if check_date_range_limit(period_start, period_end, max_days=365):
            logger.debug("Range exceeds 365 days, splitting range")

            # Split the range and make recursive calls
            pivot_date = split_date_range(period_start, period_end)
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
            result1 = range_wrapper(params1, *args, **kwargs)
            logger.debug("Making recursive call for second half")
            result2 = range_wrapper(params2, *args, **kwargs)

            logger.debug("Merging results from both halves")
            return merge_documents(result1, result2)

        else:
            # Range is within limit, make the API call
            logger.debug("Range within 365 days, making API call")
            return func(params, *args, **kwargs)

    return range_wrapper


def acknowledgement(func):
    @wraps(func)
    def ack_wrapper(params, *args, **kwargs):
        logger.debug(f"acknowledgement decorator called for function: {func.__name__}")

        name, response = func(params, *args, **kwargs)

        logger.debug(f"Received response with name: {name}")

        if "acknowledgementdocument" in name.lower():
            logger.debug("Response contains acknowledgement document")
            reason = response.reason[0].text
            logger.debug(f"Acknowledgement reason: {reason}")

            if "No matching data found" in reason:
                logger.debug(reason)
                logger.debug("Returning None")
                return None, None
            else:
                for reason in response.reason:
                    logger.error(reason.text)
                raise AcknowledgementDocumentError(response.reason)

        logger.debug("Acknowledgement check passed, returning response")
        return name, response

    return ack_wrapper


def pagination(func):
    @wraps(func)
    def pagination_wrapper(params, *args, **kwargs):
        logger.debug(f"pagination decorator called for function: {func.__name__}")

        # Check if offset is in params (indicating pagination may be needed)
        if "offset" not in params:
            logger.debug("No offset parameter found, calling function directly")
            return func(params, *args, **kwargs)

        logger.debug("Offset parameter found, starting pagination")
        merged_result = None

        for offset in range(0, 4801, 100):  # 0 to 4800 in increments of 100
            logger.debug(f"Processing pagination offset: {offset}")
            params["offset"] = offset

            result = func(params, *args, **kwargs)

            # If result is None, we've reached the end
            if result is None:
                logger.debug("Received None result, pagination complete")
                break

            # Merge with accumulated results
            merged_result = merge_documents(merged_result, result)
            logger.debug(
                f"Merged results, current result type: {type(result).__name__}"
            )

            # If we got fewer than 100 time series, we've reached the end
            if (
                result
                and hasattr(result, "time_series")
                and len(result.time_series) < 100
            ):
                logger.debug(
                    f"Received {len(result.time_series)} time series (< 100), "
                    "pagination complete"
                )
                break

        logger.debug("Pagination completed, returning merged result")
        return merged_result

    return pagination_wrapper


def retry(func):
    """
    Decorator that catches connection errors, waits and retries.

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
            # Catch httpx connection errors and socket errors
            except (httpx.RequestError,) as e:
                last_exception = e
                logger.warning(
                    f"Connection Error on attempt {attempt + 1}/{config.retries}: "
                    f"{e}. Retrying in {config.retry_delay} seconds..."
                )
                if attempt < config.retries - 1:  # Don't sleep on the last attempt
                    sleep(config.retry_delay)
                continue

        # If we've exhausted all retries, raise the last exception
        logger.error(f"All {config.retries} retry attempts failed")
        if last_exception:
            raise last_exception
        else:
            raise RuntimeError("All retry attempts failed with unknown error")

    return retry_wrapper

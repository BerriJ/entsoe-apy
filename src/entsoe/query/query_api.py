from httpx import Response, get
from pydantic import BaseModel
from xsdata_pydantic.bindings import XmlParser

from ..config.config import get_config, logger
from ..utils.utils import extract_namespace_and_find_classes
from .decorators import (
    check_if_banned,
    check_response_type,
    check_service_unavailable,
    handle_acknowledgement,
    pagination,
    rate_limit,
    retry,
    split_date_range,
    unzip,
)


@check_response_type
@check_if_banned
@check_service_unavailable
@rate_limit(max_calls=380, period=60)
def query_core(params: dict) -> Response:
    """
    Core function to make HTTP requests to the ENTSO-E API.

    Performs a basic HTTP GET request with authentication and timeout handling and checks for service unavailability.
    This is the lowest-level function that directly communicates with the API.

    Args:
        params: Dictionary of query parameters for the API request

    Returns:
        List containing a single HTTP Response object. Returned as a list
        to maintain consistency with decorators that may return multiple responses.
    """
    logger.trace("query_core: Enter")
    config = get_config()

    # Validate that security token is present and valid before making API request
    config.validate_security_token()

    # Make a copy of params and extend it with the security_token
    params_with_token = {**params, "securityToken": config.security_token}

    # Log the API call with sanitized parameters
    logger.info(f"Making API request with params: {params}")
    logger.debug(f"Request URL: {config.endpoint_url}, timeout: {config.timeout}s")

    response = get(
        config.endpoint_url, params=params_with_token, timeout=config.timeout
    )

    content_length = len(response.text) if response.text else 0
    logger.info(
        f"API response received: status={response.status_code}, size={content_length} bytes"
    )
    logger.trace(f"query_core: Exit with status {response.status_code}")

    return response


@unzip
def fetch_responses(params: dict) -> list[Response]:
    """
    Fetch responses from the ENTSO-E API with unzipping and error handling.

    Makes the HTTP request via query_core and automatically unzips ZIP responses into individual Response objects.

    Args:
        params: Dictionary of query parameters for the API request

    Returns:
        List of Response objects. Multiple responses are returned when the API
        returns a ZIP file containing multiple XML documents.
    """
    logger.trace("fetch_responses: Enter")
    response = query_core(params)
    logger.trace("fetch_responses: Exit")
    return [response]


@handle_acknowledgement
def parse_response(response: Response) -> BaseModel | None:
    """
    Parse a single HTTP response into a Pydantic BaseModel instance.

    Extracts the XML namespace and matching class from the response,
    then uses XmlParser to convert the XML content into a strongly-typed
    Pydantic model. The handle_acknowledgement decorator handles error responses
    and 'No matching data found' cases.

    Args:
        response: HTTP Response object containing XML data

    Returns:
        Pydantic BaseModel instance representing the parsed XML data,
        or None if the response is an acknowledgement with no matching data.
    """
    logger.trace("parse_response: Enter")
    logger.debug(f"Parsing response with status {response.status_code}")

    name, matching_class = extract_namespace_and_find_classes(response)

    class_name = matching_class.__name__ if matching_class else None
    logger.debug(f"Extracted namespace: {name}, matching class: {class_name}")

    xml_model = XmlParser().from_string(response.text, matching_class)

    logger.debug(f"Successfully parsed XML response into {type(xml_model).__name__}")
    logger.trace(f"parse_response: Exit with {type(xml_model).__name__}")

    return xml_model


@retry
def query_and_parse(params: dict) -> list[BaseModel]:
    """
    Query the API and parse responses with retry and error handling.

    This function orchestrates fetching responses from the API and parsing them
    into Pydantic models. It includes retry logic for transient failures and
    checks for unexpected errors in acknowledgement documents.

    Args:
        params: Dictionary of query parameters for the API request

    Returns:
        List of Pydantic BaseModel instances representing the parsed data.
        Filters out None values from acknowledgements with no matching data.
    """
    logger.trace("query_and_parse: Enter")

    responses = fetch_responses(params)

    logger.debug(f"Received {len(responses)} response(s), parsing each")

    # Parse each response and filter out None results (from "no matching data" acknowledgements)
    results = [
        parsed
        for response in responses
        if (parsed := parse_response(response)) is not None
    ]

    logger.debug(f"Parsed {len(results)} result(s)")
    logger.trace(f"query_and_parse: Exit with {len(results)} result(s)")

    return results


# Order matters! First handle range-limits, second handle pagination
@split_date_range
@pagination
def query_api(params: dict[str, str]) -> list[BaseModel]:
    """
    Main API query function that orchestrates the complete query process.

    This is the primary entry point for querying the ENTSO-E API. It handles
    the complete workflow including HTTP requests, response parsing, retry logic,
    date range splitting, and pagination.

    Configuration for decorators (max_days_limit and offset_increment) is provided
    via ContextVar objects (max_days_limit_ctx and offset_increment_ctx) that are
    set by the calling code before invoking this function.

    Args:
        params: Dictionary of string parameters for the ENTSO-E API query

    Returns:
        List of Pydantic BaseModel instances. Multiple models may be returned when:
        - The query spans multiple time periods that require separate API calls
        - The API returns paginated results
        - ZIP files contain multiple XML documents
        Each model preserves its original metadata and document structure.

    Note:
        The order of decorators is important:
        1. @split_date_range: Splits queries that exceed date range limits
        2. @pagination: Handles offset-based pagination for large result sets
    """
    logger.trace("query_api: Enter")

    results = query_and_parse(params)

    logger.trace(f"query_api: Exit with {len(results)} result(s)")

    return results

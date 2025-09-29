from httpx import Response, get
from loguru import logger
from pydantic import BaseModel
from xsdata_pydantic.bindings import XmlParser

from ..config.config import get_config
from ..utils.utils import extract_namespace_and_find_classes
from .decorators import (
    acknowledgement,
    pagination,
    range_limited,
    retry,
    service_unavailable,
    unzip,
)


@unzip
@service_unavailable
@retry
def query_core(params: dict) -> list[Response]:
    """
    Core function to make HTTP requests to the ENTSO-E API.

    This function handles the basic HTTP request with authentication and timeout.
    It's decorated with unzip and retry decorators to handle ZIP responses and
    connection failures respectively.

    Args:
        params: Dictionary of query parameters for the API request

    Returns:
        List containing a single HTTP Response object. Returned as a list
        to maintain consistency with decorators that may return multiple responses.
    """
    config = get_config()

    # Validate that security token is present and valid before making API request
    config.validate_security_token()

    URL = "https://web-api.tp.entsoe.eu/api"

    # Make a copy of params and extend it with the security_token
    params_with_token = {**params, "securityToken": config.security_token}

    # Log the API call with sanitized parameters
    logger.info(
        f"Making API request to {URL} with params: {params}, timeout: {config.timeout}"
    )

    response = get(URL, params=params_with_token, timeout=config.timeout)

    content_length = len(response.text) if response.text else 0
    logger.info(
        f"API response status: {response.status_code}, content length: {content_length}"
    )

    return [response]


@acknowledgement
def parse_response(response) -> BaseModel:
    """
    Parse an HTTP response into a Pydantic BaseModel.

    This function extracts the namespace and matching XML class from the response,
    then uses XmlParser to convert the XML content into a strongly-typed Pydantic model.
    The acknowledgement decorator handles error responses and 'No matching data found' cases.

    Args:
        response: HTTP Response object containing XML data from the ENTSO-E API

    Returns:
        Pydantic BaseModel instance representing the parsed XML data.
        Returns None if the response contains an acknowledgement indicating no data found.
    """
    logger.debug(f"Parsing response with status {response.status_code}")

    name, matching_class = extract_namespace_and_find_classes(response)

    class_name = matching_class.__name__ if matching_class else None
    logger.debug(f"Extracted namespace: {name}, matching class: {class_name}")

    xml_model = XmlParser().from_string(response.text, matching_class)

    logger.debug(f"Successfully parsed XML response into {type(xml_model).__name__}")

    return xml_model


# Order matters! First handle range-limits, second handle pagination
@range_limited
@pagination
def query_api(params: dict[str, str], max_days_limit: int = 365) -> list[BaseModel]:
    """
    Main API query function that orchestrates the complete query process.

    This function coordinates the entire API query workflow: making HTTP requests,
    parsing responses into Pydantic models, and handling various edge cases like
    date range limits and pagination. The decorators handle automatic splitting
    of large date ranges and pagination of results.

    Args:
        params: Dictionary of string parameters for the ENTSO-E API query
        max_days_limit: Maximum number of days allowed in a single query (default: 365)

    Returns:
        List of Pydantic BaseModel instances. Multiple models may be returned when:
        - The query spans multiple time periods that require separate API calls
        - The API returns paginated results
        - ZIP files contain multiple XML documents
        Each model preserves its original metadata and document structure.

    Note:
        The order of decorators is important:
        1. @range_limited: Splits queries that exceed date range limits
        2. @pagination: Handles offset-based pagination for large result sets
    """
    logger.debug("Starting query_api by calling query_core.")

    responses = query_core(params)
    results = [
        result
        for response in responses
        if (result := parse_response(response)) is not None
    ]

    logger.debug(f"query_api completed successfully, returning {len(results)} results.")

    return results

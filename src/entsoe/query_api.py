from httpx import get
from loguru import logger
from xsdata.formats.dataclass.parsers import XmlParser

from .decorators import acknowledgement, pagination, range_limited
from .utils import extract_namespace_and_find_classes


def _sanitize_params_for_logging(params: dict) -> dict:
    """
    Create a sanitized copy of params for logging by masking security tokens.

    Args:
        params: Original parameters dictionary

    Returns:
        Sanitized parameters dictionary with tokens masked
    """
    sanitized = params.copy()

    # Mask both possible token parameter names
    for token_key in ["securityToken", "security_token"]:
        if token_key in sanitized:
            sanitized[token_key] = "***MASKED***"

    return sanitized


def query_core(params: dict, timeout: int = 5):
    URL = "https://web-api.tp.entsoe.eu/api"

    # Log the API call with sanitized parameters
    sanitized_params = _sanitize_params_for_logging(params)
    logger.debug(
        f"Making API request to {URL} with params: {sanitized_params}, "
        f"timeout: {timeout}"
    )

    response = get(URL, params=params, timeout=timeout)

    content_length = len(response.text) if response.text else 0
    logger.debug(
        f"API response status: {response.status_code}, content length: {content_length}"
    )

    return response


@acknowledgement
def parse_response(response):
    logger.debug(f"Parsing response with status {response.status_code}")

    name, matching_class = extract_namespace_and_find_classes(response)

    class_name = matching_class.__name__ if matching_class else None
    logger.debug(f"Extracted namespace: {name}, matching class: {class_name}")

    result = XmlParser().from_string(response.text, matching_class)

    logger.debug(f"Successfully parsed XML response into {type(result).__name__}")

    return name, result


# Order matters! First handle range-limits, second handle pagination
@range_limited
@pagination
def query_api(params: dict, timeout: int = 5):
    sanitized_params = _sanitize_params_for_logging(params)
    logger.debug(
        f"Starting query_api with params: {sanitized_params}, timeout: {timeout}"
    )

    response = query_core(params, timeout=timeout)
    _, result = parse_response(response)

    logger.debug(f"query_api completed successfully, returning {type(result).__name__}")

    return result

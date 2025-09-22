from httpx import Response, get
from loguru import logger
from pydantic import BaseModel
from xsdata_pydantic.bindings import XmlParser

from ..config.config import get_config
from ..utils.utils import extract_namespace_and_find_classes
from .decorators import acknowledgement, pagination, range_limited, retry


@retry
def query_core(params: dict) -> Response:
    config = get_config()
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

    return response


@acknowledgement
def parse_response(response) -> tuple[str | None, BaseModel]:
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
def query_api(params: dict[str, str]) -> BaseModel:
    logger.debug("Starting query_api by calling query_core.")

    response = query_core(params)
    _, result = parse_response(response)

    logger.debug(f"query_api completed successfully, returning {type(result).__name__}")

    return result

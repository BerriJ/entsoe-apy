from httpx import get
from xsdata.formats.dataclass.parsers import XmlParser

from .decorators import acknowledgement, pagination, range_limited
from .utils import extract_namespace_and_find_classes


def query_core(params: dict, timeout: int = 5):
    URL = "https://web-api.tp.entsoe.eu/api"
    response = get(URL, params=params, timeout=timeout)
    return response


@acknowledgement
def parse_response(response):
    name, matching_class = extract_namespace_and_find_classes(response)
    result = XmlParser().from_string(response.text, matching_class)
    return name, result


# Order matters! First handle range-limits, second handle pagination
@range_limited
@pagination
def query_api(params: dict, timeout: int = 5):
    response = query_core(params, timeout=timeout)
    _, result = parse_response(response)
    return result

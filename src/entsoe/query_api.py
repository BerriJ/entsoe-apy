from httpx import get
from xsdata.formats.dataclass.parsers import XmlParser

from .decorators import Acknowledgement, range_limited
from .utils import extract_namespace_and_find_classes


def query_core(params):
    URL = "https://web-api.tp.entsoe.eu/api"
    response = get(URL, params=params, timeout=60)
    return response


@Acknowledgement
def parse_response(response):
    name, matching_class = extract_namespace_and_find_classes(response)
    result = XmlParser().from_string(response.text, matching_class)
    return name, result


@range_limited
def query_api(params):
    response = query_core(params)
    _, result = parse_response(response)
    return result

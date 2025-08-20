from httpx import get
from xsdata.formats.dataclass.parsers import XmlParser

from .utils import extract_namespace_and_find_classes


def query_core(params):
    URL = "https://web-api.tp.entsoe.eu/api"
    response = get(URL, params=params, timeout=60)
    namespace, matching_class = extract_namespace_and_find_classes(response)
    return namespace, matching_class, response


def parse_response(namespace, matching_class, response):
    result = XmlParser().from_string(response.text, matching_class)
    return result


def query_api(params):
    namespace, matching_class, response = query_core(params)
    result = parse_response(namespace, matching_class, response)
    return result

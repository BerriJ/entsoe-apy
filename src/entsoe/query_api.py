from httpx import get
from xsdata.formats.dataclass.parsers import XmlParser

from .decorators import range_limited
from .utils import extract_namespace_and_find_classes


def query_core(params):
    URL = "https://web-api.tp.entsoe.eu/api"
    response = get(URL, params=params, timeout=60)
    return response


@range_limited
def query_api(params):
    response = query_core(params)
    _, matching_class = extract_namespace_and_find_classes(response)
    result = XmlParser().from_string(response.text, matching_class)
    return result

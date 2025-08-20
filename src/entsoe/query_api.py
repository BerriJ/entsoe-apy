from httpx import get
from xsdata.formats.dataclass.parsers import XmlParser

from .utils import extract_namespace_and_find_classes


def query_api(params):
    # TODO: Add some logic to handle retries and rate limits
    URL = "https://web-api.tp.entsoe.eu/api"
    response = get(URL, params=params, timeout=60)

    try:
        response.raise_for_status()
    except Exception as e:
        raise RuntimeError(f"Failed to query ENTSO-E API: {e}")

    _, matching_class = extract_namespace_and_find_classes(response)
    result: matching_class = XmlParser().from_string(response.text, matching_class)
    return result

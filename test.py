# %%
from os import getenv

from httpx import get
from xsdata.formats.dataclass.parsers import XmlParser

from entsoe_api_py.utils import extract_namespace_and_find_classes
from entsoe_api_py.Market.base import Market_params


_ENTSOE_API = getenv("ENTSOE_API")
assert _ENTSOE_API is not None

EIC = "10Y1001A1001A82H"
documentType = "A44"
processType = "A16"

period_start = 202012312300
period_end = 202101022300

params = Market_params(
    security_token=_ENTSOE_API,
    document_type="A25",
    business_type="B10",
    contract_market_agreement_type="A01",
    out_domain=EIC,
    in_domain=EIC,
    period_start=period_start,
    period_end=period_end,
)
TIME_OUT_SECONDS = 60

URL = "https://web-api.tp.entsoe.eu/api"

response = get(URL, params=params, timeout=TIME_OUT_SECONDS)


namespace, matching_class = extract_namespace_and_find_classes(response)

result: matching_class = XmlParser().from_string(response.text, matching_class)
print(result.time_series[0])
# %%

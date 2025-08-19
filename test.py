# %%
from os import getenv

import entsoe_api_py.Base.Market as Market
from entsoe_api_py.query import query_api

_ENTSOE_API = getenv("ENTSOE_API")
assert _ENTSOE_API is not None

EIC = "10Y1001A1001A82H"
documentType = "A44"
processType = "A16"

period_start = 202012312300
period_end = 202101022300

params = Market(
    security_token=_ENTSOE_API,
    document_type="A25",
    business_type="B10",
    contract_market_agreement_type="A01",
    out_domain=EIC,
    in_domain=EIC,
    period_start=period_start,
    period_end=period_end,
).params

result = query_api(params)

print(result.time_series[0])
# %%

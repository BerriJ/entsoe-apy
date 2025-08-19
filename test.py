# %%
from os import getenv

from entsoe_api_py.Market import EnergyPrices

_ENTSOE_API = getenv("ENTSOE_API")
assert _ENTSOE_API is not None

EIC = "10Y1001A1001A82H"

period_start = 202012312300
period_end = 202101022300

object = EnergyPrices(
    security_token=_ENTSOE_API,
    in_domain=EIC,
    out_domain=EIC,
    period_start=period_start,
    period_end=period_end,
)

result = object.query_api()

# %%
from os import getenv

from httpx import get
from xsdata.formats.dataclass.parsers import XmlParser

from entsoe_api_py.xml_models.iec62325_451_1_acknowledgement_v7_0 import (
    AcknowledgementMarketDocument,
)
from entsoe_api_py.xml_models.iec62325_451_6_generationload_v3_0 import (
    GlMarketDocument,
)

_ENTSOE_API = getenv("ENTSOE_API")
assert _ENTSOE_API is not None

EIC = "10Y1001A1001A82H"
documentType = "A44"
processType = "A16"

period_start = 202012312300
period_end = 202101022300

URL = f"https://web-api.tp.entsoe.eu/api?documentType={documentType}&in_Domain={EIC}&out_Domain={EIC}&securityToken={_ENTSOE_API}&periodStart={period_start}&periodEnd={period_end}&contract_MarketAgreement.type=A01"
TIME_OUT_SECONDS = 60


response = get(URL, timeout=TIME_OUT_SECONDS)

response.read()

try:
    result: GlMarketDocument = XmlParser().from_string(response.text, GlMarketDocument)
    print("succeeded")
    print(result.time_series[0])
except Exception as e:
    result: AcknowledgementMarketDocument = XmlParser().from_string(
        response.text, AcknowledgementMarketDocument
    )
    print(result.reason)
# %%

response.read()

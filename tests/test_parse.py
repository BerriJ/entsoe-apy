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

URL = f"https://web-api.tp.entsoe.eu/api?documentType=A75&processType=A16&in_Domain=10Y1001A1001A82H&securityToken={_ENTSOE_API}&periodStart=201512312300&periodEnd=201601022300"
TIME_OUT_SECONDS = 60


def test():
    response = get(URL, timeout=TIME_OUT_SECONDS)
    try:
        result: GlMarketDocument = XmlParser().from_string(
            response.text, GlMarketDocument
        )
        print(result.time_series[0])
    except Exception:
        result: AcknowledgementMarketDocument = XmlParser().from_string(
            response.text, AcknowledgementMarketDocument
        )

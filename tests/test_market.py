# %%
from os import getenv

import pytest

from entsoe import set_config
from entsoe.config.config import reset_config
from entsoe.Market import EnergyPrices

_ENTSOE_API = getenv("ENTSOE_API")

EIC = "10Y1001A1001A82H"

period_start = 202012312300
period_end = 202101022300


@pytest.mark.skipif(
    _ENTSOE_API is None, reason="ENTSOE_API environment variable not set"
)
def test_energy_prices():
    set_config(security_token=_ENTSOE_API)
    try:
        object = EnergyPrices(
            in_domain=EIC,
            out_domain=EIC,
            period_start=period_start,
            period_end=period_end,
        )

        result = object.query_api()

        # Assert that we got a result back
        assert result is not None
    finally:
        reset_config()

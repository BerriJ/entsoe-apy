import pytest

from entsoe.config import get_config
from entsoe.Market import EnergyPrices

print("Security Token:")
print(get_config().security_token)


@pytest.mark.skipif(
    get_config().security_token is None,
    reason="ENTSOE_API environment variable not set",
)
def test_energy_prices():
    EIC = "10Y1001A1001A82H"
    period_start = 202012312300
    period_end = 202101022300
    object = EnergyPrices(
        in_domain=EIC,
        out_domain=EIC,
        period_start=period_start,
        period_end=period_end,
    )

    result = object.query_api()
    # Assert that we got a result back
    assert result, "Expected non-empty result from query_api()"

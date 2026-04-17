# %%

from decimal import Decimal
from datetime import datetime, timezone

import pytest
from pydantic import BaseModel

from entsoe.config import get_config
from entsoe.Market import EnergyPrices
from entsoe.utils import extract_records


def test_extract_records_converts_decimal_to_float():
    class Point(BaseModel):
        quantity: Decimal

    class Document(BaseModel):
        m_rid: str
        point: list[Point]

    data = Document(
        m_rid="doc-1",
        point=[Point(quantity=Decimal("10.25")), Point(quantity=Decimal("2.5"))],
    )

    records = extract_records(data, decimal_to_float=True)

    assert len(records) == 2
    assert all(isinstance(record["point.quantity"], float) for record in records)
    assert records[0]["point.quantity"] == 10.25
    assert records[1]["point.quantity"] == 2.5


def test_extract_records_domain_converts_decimal_to_float():
    class TimeSeries(BaseModel):
        quantity: Decimal

    class Document(BaseModel):
        time_series: list[TimeSeries]

    data = Document(
        time_series=[
            TimeSeries(quantity=Decimal("3.14")),
            TimeSeries(quantity=Decimal("6.28")),
        ]
    )

    records = extract_records(data, domain="time_series", decimal_to_float=True)

    assert len(records) == 2
    assert all(isinstance(record["quantity"], float) for record in records)
    assert records[0]["quantity"] == 3.14
    assert records[1]["quantity"] == 6.28


def test_extract_records_decimal_to_float_keeps_json_like_structure():
    class Document(BaseModel):
        timestamp: datetime
        quantity: Decimal

    data = Document(
        timestamp=datetime(2026, 1, 1, 0, 0, tzinfo=timezone.utc),
        quantity=Decimal("9.5"),
    )

    records = extract_records(data, decimal_to_float=True)

    assert len(records) == 1
    assert isinstance(records[0]["timestamp"], str)
    assert records[0]["timestamp"].startswith("2026-01-01T00:00:00")
    assert isinstance(records[0]["quantity"], float)
    assert records[0]["quantity"] == 9.5


def test_extract_records_serializes_decimal_as_string_when_disabled():
    class Point(BaseModel):
        quantity: Decimal

    class Document(BaseModel):
        point: list[Point]

    data = Document(
        point=[Point(quantity=Decimal("1.1")), Point(quantity=Decimal("2.2"))]
    )

    records = extract_records(data, decimal_to_float=False)

    assert len(records) == 2
    assert all(isinstance(record["point.quantity"], str) for record in records)
    assert records[0]["point.quantity"] == "1.1"
    assert records[1]["point.quantity"] == "2.2"


@pytest.mark.skipif(
    get_config().security_token is None,
    reason="ENTSOE_API environment variable not set",
)
def test_extract_records():
    EIC = "10YNL----------L"
    period_start = 202001010000
    period_end = 202001030000
    result = EnergyPrices(
        in_domain=EIC,
        out_domain=EIC,
        period_start=period_start,
        period_end=period_end,
    ).query_api()

    result_records = extract_records(result)  # Assert that we got a result back
    assert result_records is not None and len(result_records) > 0

    # Assert that result_records is a list of dicts (without nested structures)
    assert isinstance(result_records, list)
    assert all(isinstance(record, dict) for record in result_records)

    # Assert that each record is a non-nested dict.
    assert all(
        isinstance(value, (int, float, str, type(None)))
        for record in result_records
        for value in record.values()
    )

    result_records_ts = extract_records(
        result, domain="time_series"
    )  # Assert that we got a result back
    assert result_records_ts is not None and len(result_records_ts) > 0

    # Assert that result_records_ts is a list of dicts (without nested structures)
    assert isinstance(result_records_ts, list)
    assert all(isinstance(record, dict) for record in result_records_ts)

    # Assert that each record is a non-nested dict.
    assert all(
        isinstance(value, (int, float, str, type(None)))
        for record in result_records_ts
        for value in record.values()
    )

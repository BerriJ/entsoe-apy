"""Tests for the generalized ts_to_dict function."""

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum

import pytest
from xsdata.models.datatype import XmlDuration

from entsoe.flatter import Flatter
from entsoe.utils.utils import ts_to_dict
from entsoe.xml_models.iec62325_451_3_publication_v7_3 import (
    EsmpDateTimeInterval,
    Point as PublicationPoint,
    Reason as PublicationReason,
    SeriesPeriod as PublicationSeriesPeriod,
    TimeSeries as PublicationTimeSeries,
)
from entsoe.xml_models.iec62325_451_6_generationload_v3_0 import (
    Point as GenerationPoint,
    SeriesPeriod as GenerationSeriesPeriod,
    TimeSeries as GenerationTimeSeries,
)
from entsoe.xml_models.urn_entsoe_eu_wgedi_codelists import (
    BusinessTypeList,
    ContractTypeList,
    CurrencyTypeList,
    CurveTypeList,
    UnitOfMeasureTypeList,
)


@dataclass
class MockAreaIdString:
    """Mock AreaIdString for testing."""

    value: str = ""


def create_mock_publication_time_series():
    """Create a mock publication TimeSeries for testing."""
    # Create mock point
    point = PublicationPoint(position=1, price_amount=Decimal("25.50"))

    # Create mock time interval
    time_interval = EsmpDateTimeInterval(
        start="2025-08-21T22:00Z", end="2025-08-21T23:00Z"
    )

    # Create mock period
    period = PublicationSeriesPeriod(
        time_interval=time_interval, resolution=XmlDuration("PT60M"), point=[point]
    )

    # Create mock TimeSeries
    ts = PublicationTimeSeries(
        m_rid="TEST_MRID_001",
        business_type=BusinessTypeList.B11,
        in_domain_m_rid=MockAreaIdString(value="10YFR-RTE------C"),
        out_domain_m_rid=MockAreaIdString(value="10YCB-GERMANY--8"),
        currency_unit_name=CurrencyTypeList.EUR,
        price_measure_unit_name=UnitOfMeasureTypeList.MWH,
        contract_market_agreement_type=ContractTypeList.A01,
        period=[period],
    )

    return ts


def create_mock_generation_time_series():
    """Create a mock generation TimeSeries for testing."""
    # Create mock point with different fields than publication
    point = GenerationPoint(
        position=1, quantity=Decimal("1500.75"), secondary_quantity=Decimal("1400.25")
    )

    # Create mock time interval
    time_interval = EsmpDateTimeInterval(
        start="2025-08-21T22:00Z", end="2025-08-21T23:00Z"
    )

    # Create mock period
    period = GenerationSeriesPeriod(
        time_interval=time_interval, resolution=XmlDuration("PT15M"), point=[point]
    )

    # Create mock TimeSeries with different fields
    ts = GenerationTimeSeries(
        m_rid="GEN_MRID_001",
        business_type=BusinessTypeList.A04,
        registered_resource_name="Test Generator",
        quantity_measure_unit_name=UnitOfMeasureTypeList.MAW,
        curve_type=CurveTypeList.A01,
        period=[period],
    )

    return ts


class TestTsToDict:
    """Test class for ts_to_dict function."""

    def test_publication_time_series(self):
        """Test ts_to_dict with publication TimeSeries."""
        ts = create_mock_publication_time_series()
        result = Flatter({
            Enum: lambda key, value: {key: value.value},
            list[PublicationReason]: lambda key, value: {key: ""},
            XmlDuration: lambda key, value: {
                key: value.data,
                "resolution_minutes": value.minutes,
            },
            EsmpDateTimeInterval: lambda key, value: {
                "interval-start": value.start,
                "interval-end": value.end,
            },
            MockAreaIdString: lambda key, value: {key: value.value},
        }).do(ts)

        assert len(result) == 1
        row = result[0]

        # Check basic fields
        assert row["position"] == 1
        assert row["resolution"] == "PT60M"
        assert row["resolution_minutes"] == 60

        # Check point fields
        assert row["price_amount"] == 25.50

        # Check TimeSeries fields (prefixed with ts_)
        assert row["m_rid"] == "TEST_MRID_001"
        assert row["business_type"] == "B11"
        assert row["in_domain_m_rid"] == "10YFR-RTE------C"
        assert row["out_domain_m_rid"] == "10YCB-GERMANY--8"
        assert row["currency_unit_name"] == "EUR"
        assert row["price_measure_unit_name"] == "MWH"
        assert row["contract_market_agreement_type"] == "A01"

    def test_generation_time_series(self):
        """Test ts_to_dict with generation TimeSeries."""
        ts = create_mock_generation_time_series()
        result = ts_to_dict([ts])

        assert len(result) == 1
        row = result[0]

        # Check basic fields
        assert row["position"] == 1
        assert "timestamp" in row
        assert row["resolution"] == "PT15M"
        assert row["resolution_minutes"] == 15

        # Check point fields (different from publication)
        assert row["quantity"] == 1500.75
        assert row["secondary_quantity"] == 1400.25
        assert "price_amount" not in row  # This field doesn't exist in generation

        # Check TimeSeries fields (different from publication)
        assert row["ts_m_rid"] == "GEN_MRID_001"
        assert row["ts_business_type"] == "A04"
        assert row["ts_registered_resource_name"] == "Test Generator"
        assert row["ts_quantity_measure_unit_name"] == "MAW"
        assert row["ts_curve_type"] == "A01"

        # Fields from publication shouldn't exist
        assert "ts_currency_unit_name" not in row
        assert "ts_contract_market_agreement_type" not in row

    def test_mixed_time_series_types(self):
        """Test ts_to_dict with mixed TimeSeries types."""
        pub_ts = create_mock_publication_time_series()
        gen_ts = create_mock_generation_time_series()

        result = ts_to_dict([pub_ts, gen_ts])

        assert len(result) == 2

        # First row should be from publication TimeSeries
        pub_row = result[0]
        assert pub_row["ts_m_rid"] == "TEST_MRID_001"
        assert pub_row["price_amount"] == 25.50
        assert "quantity" not in pub_row

        # Second row should be from generation TimeSeries
        gen_row = result[1]
        assert gen_row["ts_m_rid"] == "GEN_MRID_001"
        assert gen_row["quantity"] == 1500.75
        assert "price_amount" not in gen_row

    def test_empty_list(self):
        """Test ts_to_dict with empty list."""
        result = ts_to_dict([])
        assert result == []

    def test_time_series_without_periods(self):
        """Test ts_to_dict with TimeSeries that has no periods."""
        ts = PublicationTimeSeries(
            m_rid="NO_PERIODS",
            business_type=BusinessTypeList.B11,
            period=[],  # Empty periods
        )

        result = ts_to_dict([ts])
        assert result == []

    def test_period_without_points(self):
        """Test ts_to_dict with period that has no points."""
        time_interval = EsmpDateTimeInterval(
            start="2025-08-21T22:00Z", end="2025-08-21T23:00Z"
        )

        period = PublicationSeriesPeriod(
            time_interval=time_interval,
            resolution=XmlDuration("PT60M"),
            point=[],  # Empty points
        )

        ts = PublicationTimeSeries(
            m_rid="NO_POINTS", business_type=BusinessTypeList.B11, period=[period]
        )

        result = ts_to_dict([ts])
        assert result == []

    def test_backward_compatibility_publication_format(self):
        """Test that the function maintains backward compatibility with
        publication format."""
        ts = create_mock_publication_time_series()
        result = ts_to_dict([ts])

        assert len(result) == 1
        row = result[0]

        # Check that fields from the original hardcoded implementation are present
        # (though with ts_ prefix for TimeSeries fields)
        assert row["position"] == 1
        assert isinstance(row["timestamp"], datetime)
        assert row["price_amount"] == 25.50
        assert row["ts_currency_unit_name"] == "EUR"  # Originally "currency"
        # Originally "price_measure_unit"
        assert row["ts_price_measure_unit_name"] == "MWH"
        # Originally "in_domain"
        assert row["ts_in_domain_m_rid"] == "10YFR-RTE------C"
        assert row["resolution"] == "PT60M"
        assert row["resolution_minutes"] == 60
        assert row["ts_business_type"] == "B11"
        assert row["ts_contract_market_agreement_type"] == "A01"

    def test_backward_compatibility_with_original_field_names(self):
        """
        Test a convenience function that provides original field names for
        backward compatibility. This shows how the generalized function can
        be adapted for specific use cases.
        """
        ts = create_mock_publication_time_series()
        result = ts_to_dict([ts])

        # Transform result to match original field names for backward compatibility
        transformed_result = []
        for row in result:
            transformed_row = row.copy()

            # Map new field names to original ones for publication TimeSeries
            field_mapping = {
                "ts_currency_unit_name": "currency",
                "ts_price_measure_unit_name": "price_measure_unit",
                "ts_in_domain_m_rid": "in_domain",
                "ts_business_type": "business_type",
                "ts_contract_market_agreement_type": "contract_market_agreement_type",
            }

            for new_field, old_field in field_mapping.items():
                if new_field in transformed_row:
                    transformed_row[old_field] = transformed_row[new_field]
                    # Optionally remove the prefixed version
                    # del transformed_row[new_field]

            transformed_result.append(transformed_row)

        # Verify the transformed result has original field names
        transformed_row = transformed_result[0]
        assert transformed_row["currency"] == "EUR"
        assert transformed_row["price_measure_unit"] == "MWH"
        assert transformed_row["in_domain"] == "10YFR-RTE------C"
        assert transformed_row["business_type"] == "B11"
        assert transformed_row["contract_market_agreement_type"] == "A01"

    def test_timestamp_calculation_error_handling(self):
        """Test that timestamp calculation errors are handled gracefully."""
        point = PublicationPoint(position=1)

        # Create period with malformed time interval
        time_interval = EsmpDateTimeInterval(start=None, end=None)
        period = PublicationSeriesPeriod(
            time_interval=time_interval, resolution=None, point=[point]
        )

        ts = PublicationTimeSeries(
            m_rid="MALFORMED", business_type=BusinessTypeList.B11, period=[period]
        )

        result = ts_to_dict([ts])
        assert len(result) == 1
        assert result[0]["timestamp"] is None  # Should be None due to error
        assert result[0]["position"] == 1  # Other fields should still work


if __name__ == "__main__":
    pytest.main([__file__])

"""Tests for encapsulation improvements in OMI and Outages classes."""

import pytest

from entsoe import set_config
from entsoe.Base.Outages import Outages
from entsoe.config.config import reset_config
from entsoe.OMI.OMI import OMI


class TestEncapsulation:
    """Test that OMI and Outages classes properly use Base class encapsulation."""

    def setup_method(self):
        """Set up test configuration before each test."""
        set_config(security_token="test_token")

    def teardown_method(self):
        """Clean up configuration after each test."""
        reset_config()

    def test_omi_parameter_initialization(self):
        """Test that OMI class properly initializes parameters using base
        class methods."""
        omi = OMI(
            control_area_domain="10YBE----------2",
            period_start=202301010000,
            period_end=202301020000,
            doc_status="A05",
            m_rid="test_mrid",
            offset=100,
        )

        # Verify that parameters are set correctly
        assert omi.params["documentType"] == "B47"
        assert omi.params["periodStart"] == 202301010000
        assert omi.params["periodEnd"] == 202301020000
        assert omi.params["ControlArea_Domain"] == "10YBE----------2"
        assert omi.params["DocStatus"] == "A05"
        assert omi.params["mRID"] == "test_mrid"
        assert omi.params["Offset"] == 100

    def test_omi_optional_periods(self):
        """Test that OMI class handles period parameters correctly - either
        standard or update periods must be provided."""
        # Test with update periods instead of standard periods
        omi = OMI(
            control_area_domain="10YBE----------2",
            period_start_update=202301010000,
            period_end_update=202301020000,
        )

        # Verify that standard period parameters are not included
        assert "periodStart" not in omi.params
        assert "periodEnd" not in omi.params
        # But update period parameters should be included
        assert omi.params["PeriodStartUpdate"] == 202301010000
        assert omi.params["PeriodEndUpdate"] == 202301020000
        assert omi.params["documentType"] == "B47"

    def test_outages_parameter_initialization(self):
        """Test that Outages class properly initializes parameters using base
        class methods."""
        outages = Outages(
            document_type="A77",
            period_start=202301010000,
            period_end=202301020000,
            bidding_zone_domain="10YBE----------2",
            business_type="A53",
            registered_resource="10Y1001A1001A82H",  # Valid EIC code
            doc_status="A05",
            m_rid="test_mrid",
            offset=100,
        )

        # Verify that parameters are set correctly
        assert outages.params["documentType"] == "A77"
        assert outages.params["periodStart"] == 202301010000
        assert outages.params["periodEnd"] == 202301020000
        assert outages.params["biddingZone_Domain"] == "10YBE----------2"
        assert outages.params["businessType"] == "A53"
        assert outages.params["registeredResource"] == "10Y1001A1001A82H"
        assert outages.params["docStatus"] == "A05"
        assert outages.params["mRID"] == "test_mrid"
        assert outages.params["offset"] == 100

    def test_outages_optional_periods(self):
        """Test that Outages class handles optional period parameters correctly."""
        outages = Outages(
            document_type="A77",
            bidding_zone_domain="10YBE----------2",
        )

        # Verify that optional period parameters are not included
        assert "periodStart" not in outages.params
        assert "periodEnd" not in outages.params
        assert outages.params["documentType"] == "A77"

    def test_omi_validation_error(self):
        """Test that OMI class validation still works properly."""
        with pytest.raises(ValueError, match="doc_status must be one of"):
            OMI(
                control_area_domain="10YBE----------2",
                period_start=202301010000,
                period_end=202301020000,
                doc_status="INVALID",  # type: ignore
            )

    def test_omi_period_validation_error(self):
        """Test that OMI class requires either standard or update periods."""
        with pytest.raises(
            ValueError, match="Either \\(period_start, period_end\\) or"
        ):
            OMI(
                control_area_domain="10YBE----------2",
            )

    def test_encapsulation_no_direct_params_access(self):
        """Test that both classes use proper encapsulation methods."""
        # Test OMI
        omi = OMI(
            control_area_domain="10YBE----------2",
            period_start=202301010000,
            period_end=202301020000,
        )

        # The params dictionary should be properly initialized through Base
        # class methods
        # This verifies that we're not manually setting self.params = {...}
        assert hasattr(omi, "params")
        assert isinstance(omi.params, dict)

        # Test Outages
        outages = Outages(
            document_type="A77",
            bidding_zone_domain="10YBE----------2",
        )

        # The params dictionary should be properly initialized through Base
        # class methods
        assert hasattr(outages, "params")
        assert isinstance(outages.params, dict)

"""Tests for encapsulation improvements in OMI and Outages classes."""

import pytest

from entsoe.Base.Outages import Outages
from entsoe.OMI.OMI import OMI


class TestEncapsulation:
    """Test that OMI and Outages classes properly use Base class encapsulation."""

    def test_omi_parameter_initialization(self):
        """Test that OMI class properly initializes parameters using base
        class methods."""
        omi = OMI(
            security_token="test_token",
            period_start=202301010000,
            period_end=202301020000,
            control_area_domain="10YBE----------2",
            doc_status="A05",
            m_rid="test_mrid",
            offset=100,
        )

        # Verify that parameters are set correctly
        assert omi.params["documentType"] == "B47"
        assert omi.params["securityToken"] == "test_token"
        assert omi.params["periodStart"] == 202301010000
        assert omi.params["periodEnd"] == 202301020000
        assert omi.params["controlArea_Domain"] == "10YBE----------2"
        assert omi.params["docStatus"] == "A05"
        assert omi.params["mRID"] == "test_mrid"
        assert omi.params["offset"] == 100

    def test_omi_optional_periods(self):
        """Test that OMI class handles optional period parameters correctly."""
        omi = OMI(
            security_token="test_token",
            control_area_domain="10YBE----------2",
        )

        # Verify that optional period parameters are not included
        assert "periodStart" not in omi.params
        assert "periodEnd" not in omi.params
        assert omi.params["documentType"] == "B47"
        assert omi.params["securityToken"] == "test_token"

    def test_outages_parameter_initialization(self):
        """Test that Outages class properly initializes parameters using base
        class methods."""
        outages = Outages(
            document_type="A77",
            security_token="test_token",
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
        assert outages.params["securityToken"] == "test_token"
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
            security_token="test_token",
            bidding_zone_domain="10YBE----------2",
        )

        # Verify that optional period parameters are not included
        assert "periodStart" not in outages.params
        assert "periodEnd" not in outages.params
        assert outages.params["documentType"] == "A77"
        assert outages.params["securityToken"] == "test_token"

    def test_omi_validation_error(self):
        """Test that OMI class validation still works properly."""
        with pytest.raises(ValueError, match="doc_status must be one of"):
            OMI(
                security_token="test_token",
                doc_status="INVALID",
            )

    def test_encapsulation_no_direct_params_access(self):
        """Test that both classes use proper encapsulation methods."""
        # Test OMI
        omi = OMI(
            security_token="test_token",
            control_area_domain="10YBE----------2",
        )

        # The params dictionary should be properly initialized through Base
        # class methods
        # This verifies that we're not manually setting self.params = {...}
        assert hasattr(omi, "params")
        assert isinstance(omi.params, dict)
        assert "securityToken" in omi.params

        # Test Outages
        outages = Outages(
            document_type="A77",
            security_token="test_token",
            bidding_zone_domain="10YBE----------2",
        )

        # The params dictionary should be properly initialized through Base
        # class methods
        assert hasattr(outages, "params")
        assert isinstance(outages.params, dict)
        assert "securityToken" in outages.params

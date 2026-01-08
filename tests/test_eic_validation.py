"""Tests for EIC code validation functionality."""

import pytest

from entsoe.Balancing import (
    ImbalancePrices,
    VolumesAndPricesOfContractedReserves,
)
from entsoe.Base.Base import Base, ValidationError
from entsoe.Market import EnergyPrices


class TestEICValidation:
    """Test cases for EIC code validation."""

    def test_validate_eic_code_valid(self):
        """Test validation passes for valid EIC codes."""
        base = Base(
            document_type="A44",
            period_start=202012312300,
            period_end=202101022300,
        )

        # Should not raise exception for valid EIC code
        base.validate_eic_code("10Y1001A1001A82H", "test_parameter")

    def test_validate_eic_code_invalid(self):
        """Test validation fails for invalid EIC codes."""
        base = Base(
            document_type="A44",
            period_start=202012312300,
            period_end=202101022300,
        )

        # Should raise ValidationError for invalid EIC code
        with pytest.raises(ValidationError) as exc_info:
            base.validate_eic_code("INVALID_EIC_CODE", "test_parameter")

        assert "Invalid EIC code 'INVALID_EIC_CODE'" in str(exc_info.value)
        assert "test_parameter" in str(exc_info.value)

    def test_validate_eic_code_none(self):
        """Test validation passes for None values."""
        base = Base(
            document_type="A44",
            period_start=202012312300,
            period_end=202101022300,
        )

        # Should not raise exception for None
        base.validate_eic_code(None, "test_parameter")

    def test_add_domain_params_valid_eic(self):
        """Test add_domain_params with valid EIC codes."""
        base = Base(
            document_type="A44",
            period_start=202012312300,
            period_end=202101022300,
        )

        # Should not raise exception for valid EIC codes
        base.add_domain_params(
            in_domain="10Y1001A1001A82H",
            out_domain="10YGB----------A",
            bidding_zone_domain="10YBE----------2",
        )

        assert base.params["in_Domain"] == "10Y1001A1001A82H"
        assert base.params["out_Domain"] == "10YGB----------A"
        assert base.params["biddingZone_Domain"] == "10YBE----------2"

    def test_add_domain_params_invalid_eic(self):
        """Test add_domain_params with invalid EIC codes."""
        base = Base(
            document_type="A44",
            period_start=202012312300,
            period_end=202101022300,
        )

        # Should raise ValidationError for invalid EIC code
        with pytest.raises(ValidationError) as exc_info:
            base.add_domain_params(in_domain="INVALID_EIC")

        assert "Invalid EIC code 'INVALID_EIC'" in str(exc_info.value)
        assert "in_domain" in str(exc_info.value)

    def test_balancing_class_eic_validation(self):
        """Test EIC validation in Balancing-derived classes."""
        # Should raise ValidationError for invalid control_area_domain
        with pytest.raises(ValidationError) as exc_info:
            ImbalancePrices(
                period_start=202012312300,
                period_end=202101022300,
                control_area_domain="INVALID_EIC",
            )

        assert "Invalid EIC code 'INVALID_EIC'" in str(exc_info.value)
        assert "control_area_domain" in str(exc_info.value)

    def test_balancing_eic_validation_bidding_zone(self):
        """Test EIC validation in specific parameter classes."""
        # Should raise ValidationError for invalid bidding_zone_domain
        with pytest.raises(ValidationError) as exc_info:
            VolumesAndPricesOfContractedReserves(
                period_start=202012312300,
                period_end=202101022300,
                bidding_zone_domain="INVALID_EIC",
                process_type="A52",
            )

        assert "Invalid EIC code 'INVALID_EIC'" in str(exc_info.value)
        assert "bidding_zone_domain" in str(exc_info.value)

    def test_market_class_eic_validation(self):
        """Test EIC validation in Market-derived classes."""
        # Should raise ValidationError for invalid in_domain
        with pytest.raises(ValidationError) as exc_info:
            EnergyPrices(
                period_start=202012312300,
                period_end=202101022300,
                in_domain="INVALID_EIC",
                out_domain="10YGB----------A",
            )

        assert "Invalid EIC code 'INVALID_EIC'" in str(exc_info.value)
        assert "in_domain" in str(exc_info.value)

    def test_valid_eic_construction_succeeds(self):
        """Test that construction with valid EIC codes succeeds."""
        # Should succeed with valid and matching EIC codes
        energy_prices = EnergyPrices(
            period_start=202012312300,
            period_end=202101022300,
            in_domain="10Y1001A1001A82H",
            out_domain="10Y1001A1001A82H",  # Must be same for EnergyPrices
        )

        assert energy_prices.params["in_Domain"] == "10Y1001A1001A82H"
        assert energy_prices.params["out_Domain"] == "10Y1001A1001A82H"

    def test_valid_balancing_construction(self):
        """Test that construction with valid EIC codes succeeds for specific classes."""
        # Should succeed with valid EIC codes
        imbalance_prices = ImbalancePrices(
            period_start=202012312300,
            period_end=202101022300,
            control_area_domain="10Y1001A1001A82H",
        )

        assert imbalance_prices.params["controlArea_Domain"] == "10Y1001A1001A82H"

    def test_mixed_valid_invalid_eic_validation(self):
        """Test validation with mixed valid and invalid EIC codes."""
        base = Base(
            document_type="A44",
            period_start=202012312300,
            period_end=202101022300,
        )

        # Should fail on the first invalid EIC code
        with pytest.raises(ValidationError) as exc_info:
            base.add_domain_params(
                in_domain="10Y1001A1001A82H",  # valid
                out_domain="INVALID_EIC",  # invalid
                bidding_zone_domain="10YBE----------2",  # valid
            )

        assert "Invalid EIC code 'INVALID_EIC'" in str(exc_info.value)
        assert "out_domain" in str(exc_info.value)

    def test_registered_resource_eic_validation(self):
        """Test EIC validation for registered_resource parameter."""
        base = Base(
            document_type="A44",
            period_start=202012312300,
            period_end=202101022300,
        )

        # Should raise ValidationError for invalid registered_resource
        with pytest.raises(ValidationError) as exc_info:
            base.add_resource_params(registered_resource="INVALID_EIC")

        assert "Invalid EIC code 'INVALID_EIC'" in str(exc_info.value)
        assert "registered_resource" in str(exc_info.value)

        # Should succeed with valid EIC code
        base.add_resource_params(registered_resource="10Y1001A1001A82H")
        assert base.params["registeredResource"] == "10Y1001A1001A82H"

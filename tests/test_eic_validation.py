"""Tests for EIC code validation functionality."""

import pytest

from entsoe import set_config
from entsoe.Balancing import AcceptedAggregatedOffers, CrossBorderBalancing
from entsoe.Base.Base import Base, ValidationError
from entsoe.config.config import reset_config
from entsoe.Market import EnergyPrices


class TestEICValidation:
    """Test cases for EIC code validation."""

    def setup_method(self):
        """Set up test configuration before each test."""
        set_config(security_token="test_token")

    def teardown_method(self):
        """Clean up configuration after each test."""
        reset_config()

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
            AcceptedAggregatedOffers(
                period_start=202012312300,
                period_end=202101022300,
                control_area_domain="INVALID_EIC",
            )

        assert "Invalid EIC code 'INVALID_EIC'" in str(exc_info.value)
        assert "control_area_domain" in str(exc_info.value)

    def test_cross_border_balancing_eic_validation(self):
        """Test EIC validation in specific parameter classes."""
        # Should raise ValidationError for invalid acquiring_domain
        with pytest.raises(ValidationError) as exc_info:
            CrossBorderBalancing(
                period_start=202012312300,
                period_end=202101022300,
                acquiring_domain="INVALID_EIC",
                connecting_domain="10YBE----------2",
            )

        assert "Invalid EIC code 'INVALID_EIC'" in str(exc_info.value)
        assert "acquiring_domain" in str(exc_info.value)

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
        # Should succeed with valid EIC codes
        energy_prices = EnergyPrices(
            period_start=202012312300,
            period_end=202101022300,
            in_domain="10Y1001A1001A82H",
            out_domain="10YGB----------A",
        )

        assert energy_prices.params["in_Domain"] == "10Y1001A1001A82H"
        assert energy_prices.params["out_Domain"] == "10YGB----------A"

    def test_valid_cross_border_balancing_construction(self):
        """Test that construction with valid EIC codes succeeds for specific classes."""
        # Should succeed with valid EIC codes
        cross_border = CrossBorderBalancing(
            period_start=202012312300,
            period_end=202101022300,
            acquiring_domain="10Y1001A1001A82H",
            connecting_domain="10YGB----------A",
        )

        assert cross_border.params["acquiring_Domain"] == "10Y1001A1001A82H"
        assert cross_border.params["connecting_Domain"] == "10YGB----------A"

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

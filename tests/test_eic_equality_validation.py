"""Tests for EIC equality validation functionality."""

import pytest

from entsoe.Base.Base import ValidationError
from entsoe.Market import (
    EnergyPrices,
    ExplicitAllocationsAuctionRevenue,
    ImplicitAuctionNetPositions,
    ImplicitFlowBasedAllocationsCongestionIncome,
    TotalNominatedCapacity,
)
from entsoe.Transmission import (
    CommercialSchedules,
    CrossBorderPhysicalFlows,
    ForecastedTransferCapacities,
)


class TestEICEqualityValidation:
    """Test cases for EIC equality validation."""

    # Market classes requiring SAME EICs

    def test_energy_prices_requires_same_eics(self):
        """Test that EnergyPrices requires same in_domain and out_domain."""
        # Should succeed with same EIC codes
        energy_prices = EnergyPrices(
            period_start=202012312300,
            period_end=202101022300,
            in_domain="10Y1001A1001A82H",
            out_domain="10Y1001A1001A82H",
        )
        assert energy_prices.params["in_Domain"] == "10Y1001A1001A82H"
        assert energy_prices.params["out_Domain"] == "10Y1001A1001A82H"

        # Should fail with different EIC codes
        with pytest.raises(ValidationError) as exc_info:
            EnergyPrices(
                period_start=202012312300,
                period_end=202101022300,
                in_domain="10Y1001A1001A82H",
                out_domain="10YGB----------A",
            )

        assert "must be the same" in str(exc_info.value)
        assert "10Y1001A1001A82H" in str(exc_info.value)
        assert "10YGB----------A" in str(exc_info.value)

    def test_implicit_auction_net_positions_requires_same_eics(self):
        """Test that ImplicitAuctionNetPositions requires same EICs."""
        # Should succeed with same EIC codes
        net_positions = ImplicitAuctionNetPositions(
            period_start=202012312300,
            period_end=202101022300,
            in_domain="10YBE----------2",
            out_domain="10YBE----------2",
        )
        assert net_positions.params["in_Domain"] == "10YBE----------2"
        assert net_positions.params["out_Domain"] == "10YBE----------2"

        # Should fail with different EIC codes
        with pytest.raises(ValidationError) as exc_info:
            ImplicitAuctionNetPositions(
                period_start=202012312300,
                period_end=202101022300,
                in_domain="10YBE----------2",
                out_domain="10YGB----------A",
            )

        assert "must be the same" in str(exc_info.value)

    def test_implicit_flow_based_allocations_congestion_income_requires_same_eics(
        self,
    ):
        """Test that ImplicitFlowBasedAllocationsCongestionIncome requires same EICs."""
        # Should succeed with same EIC codes
        congestion = ImplicitFlowBasedAllocationsCongestionIncome(
            period_start=202012312300,
            period_end=202101022300,
            in_domain="10YAT-APG------L",
            out_domain="10YAT-APG------L",
        )
        assert congestion.params["in_Domain"] == "10YAT-APG------L"
        assert congestion.params["out_Domain"] == "10YAT-APG------L"

        # Should fail with different EIC codes
        with pytest.raises(ValidationError) as exc_info:
            ImplicitFlowBasedAllocationsCongestionIncome(
                period_start=202012312300,
                period_end=202101022300,
                in_domain="10YAT-APG------L",
                out_domain="10YBE----------2",
            )

        assert "must be the same" in str(exc_info.value)

    # Market classes requiring DIFFERENT EICs

    def test_total_nominated_capacity_requires_different_eics(self):
        """Test that TotalNominatedCapacity requires different in_domain and out_domain."""
        # Should succeed with different EIC codes
        capacity = TotalNominatedCapacity(
            period_start=202012312300,
            period_end=202101022300,
            in_domain="10YGB----------A",
            out_domain="10YBE----------2",
        )
        assert capacity.params["in_Domain"] == "10YGB----------A"
        assert capacity.params["out_Domain"] == "10YBE----------2"

        # Should fail with same EIC codes
        with pytest.raises(ValidationError) as exc_info:
            TotalNominatedCapacity(
                period_start=202012312300,
                period_end=202101022300,
                in_domain="10YGB----------A",
                out_domain="10YGB----------A",
            )

        assert "must be different" in str(exc_info.value)
        assert "10YGB----------A" in str(exc_info.value)

    def test_explicit_allocations_auction_revenue_requires_different_eics(self):
        """Test that ExplicitAllocationsAuctionRevenue requires different EICs."""
        # Should succeed with different EIC codes
        revenue = ExplicitAllocationsAuctionRevenue(
            period_start=202012312300,
            period_end=202101022300,
            in_domain="10Y1001A1001A82H",
            out_domain="10YBE----------2",
        )
        assert revenue.params["in_Domain"] == "10Y1001A1001A82H"
        assert revenue.params["out_Domain"] == "10YBE----------2"

        # Should fail with same EIC codes
        with pytest.raises(ValidationError) as exc_info:
            ExplicitAllocationsAuctionRevenue(
                period_start=202012312300,
                period_end=202101022300,
                in_domain="10Y1001A1001A82H",
                out_domain="10Y1001A1001A82H",
            )

        assert "must be different" in str(exc_info.value)

    # Transmission classes requiring DIFFERENT EICs

    def test_cross_border_physical_flows_requires_different_eics(self):
        """Test that CrossBorderPhysicalFlows requires different EICs."""
        # Should succeed with different EIC codes
        flows = CrossBorderPhysicalFlows(
            period_start=202012312300,
            period_end=202101022300,
            in_domain="10YGB----------A",
            out_domain="10YBE----------2",
        )
        assert flows.params["in_Domain"] == "10YGB----------A"
        assert flows.params["out_Domain"] == "10YBE----------2"

        # Should fail with same EIC codes
        with pytest.raises(ValidationError) as exc_info:
            CrossBorderPhysicalFlows(
                period_start=202012312300,
                period_end=202101022300,
                in_domain="10YGB----------A",
                out_domain="10YGB----------A",
            )

        assert "must be different" in str(exc_info.value)

    def test_commercial_schedules_requires_different_eics(self):
        """Test that CommercialSchedules requires different EICs."""
        # Should succeed with different EIC codes
        schedules = CommercialSchedules(
            period_start=202012312300,
            period_end=202101022300,
            in_domain="10YGB----------A",
            out_domain="10YNL----------L",
        )
        assert schedules.params["in_Domain"] == "10YGB----------A"
        assert schedules.params["out_Domain"] == "10YNL----------L"

        # Should fail with same EIC codes
        with pytest.raises(ValidationError) as exc_info:
            CommercialSchedules(
                period_start=202012312300,
                period_end=202101022300,
                in_domain="10YGB----------A",
                out_domain="10YGB----------A",
            )

        assert "must be different" in str(exc_info.value)

    def test_forecasted_transfer_capacities_requires_different_eics(self):
        """Test that ForecastedTransferCapacities requires different EICs."""
        # Should succeed with different EIC codes
        capacities = ForecastedTransferCapacities(
            period_start=202012312300,
            period_end=202101022300,
            in_domain="10YGB----------A",
            out_domain="10YFR-RTE------C",
            contract_market_agreement_type="A01",
        )
        assert capacities.params["in_Domain"] == "10YGB----------A"
        assert capacities.params["out_Domain"] == "10YFR-RTE------C"

        # Should fail with same EIC codes
        with pytest.raises(ValidationError) as exc_info:
            ForecastedTransferCapacities(
                period_start=202012312300,
                period_end=202101022300,
                in_domain="10YGB----------A",
                out_domain="10YGB----------A",
                contract_market_agreement_type="A01",
            )

        assert "must be different" in str(exc_info.value)

    def test_validation_with_none_values(self):
        """Test that validation is skipped when either parameter is None."""
        # This test verifies that the validation doesn't fail when
        # parameters are None (which shouldn't happen in practice
        # for these specific classes, but the validation method should handle it)
        from entsoe.Base.Base import Base

        base = Base(
            document_type="A44",
            period_start=202012312300,
            period_end=202101022300,
        )

        # Should not raise exception when parameters are None
        base.validate_eic_equality(None, "10YGB----------A", must_be_equal=True)
        base.validate_eic_equality("10YGB----------A", None, must_be_equal=True)
        base.validate_eic_equality(None, None, must_be_equal=True)

        base.validate_eic_equality(None, "10YGB----------A", must_be_equal=False)
        base.validate_eic_equality("10YGB----------A", None, must_be_equal=False)
        base.validate_eic_equality(None, None, must_be_equal=False)

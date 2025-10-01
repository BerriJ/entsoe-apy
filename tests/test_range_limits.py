"""Test max_days_limit for various endpoints."""

from entsoe.Generation import (
    ActualGenerationPerGenerationUnit,
    InstalledCapacityPerProductionType,
)
from entsoe.Load import (
    ActualTotalLoad,
    DayAheadTotalLoadForecast,
    MonthAheadTotalLoadForecast,
    WeekAheadTotalLoadForecast,
    YearAheadForecastMargin,
    YearAheadTotalLoadForecast,
)
from entsoe.Market import EnergyPrices


class TestRangeLimits:
    """Test that max_days_limit is set correctly for various endpoint classes."""

    def test_installed_capacity_has_high_default_limit(self):
        """Test that InstalledCapacityPerProductionType uses high default (100000)."""
        # This endpoint has no documented limit, so should use the high default
        params = InstalledCapacityPerProductionType(
            period_start=202401010000,
            period_end=202412310000,
            in_domain="10YDE-RWENET---I",  # Germany
        )
        assert params.max_days_limit == 100000

    def test_actual_generation_per_unit_has_1_day_limit(self):
        """Test that ActualGenerationPerGenerationUnit has 1 day limit."""
        params = ActualGenerationPerGenerationUnit(
            period_start=202401010000,
            period_end=202401020000,
            in_domain="10YDE-RWENET---I",  # Germany
        )
        assert params.max_days_limit == 1

    def test_actual_total_load_has_1_year_limit(self):
        """Test that ActualTotalLoad has 365 day limit."""
        params = ActualTotalLoad(
            out_bidding_zone_domain="10YDE-RWENET---I",  # Germany
            period_start=202401010000,
            period_end=202412310000,
        )
        assert params.max_days_limit == 365

    def test_day_ahead_total_load_has_1_year_limit(self):
        """Test that DayAheadTotalLoadForecast has 365 day limit."""
        params = DayAheadTotalLoadForecast(
            out_bidding_zone_domain="10YDE-RWENET---I",  # Germany
            period_start=202401010000,
            period_end=202412310000,
        )
        assert params.max_days_limit == 365

    def test_week_ahead_total_load_has_1_year_limit(self):
        """Test that WeekAheadTotalLoadForecast has 365 day limit."""
        params = WeekAheadTotalLoadForecast(
            out_bidding_zone_domain="10YDE-RWENET---I",  # Germany
            period_start=202401010000,
            period_end=202412310000,
        )
        assert params.max_days_limit == 365

    def test_month_ahead_total_load_has_1_year_limit(self):
        """Test that MonthAheadTotalLoadForecast has 365 day limit."""
        params = MonthAheadTotalLoadForecast(
            out_bidding_zone_domain="10YDE-RWENET---I",  # Germany
            period_start=202401010000,
            period_end=202412310000,
        )
        assert params.max_days_limit == 365

    def test_year_ahead_total_load_has_1_year_limit(self):
        """Test that YearAheadTotalLoadForecast has 365 day limit."""
        params = YearAheadTotalLoadForecast(
            out_bidding_zone_domain="10YDE-RWENET---I",  # Germany
            period_start=202401010000,
            period_end=202412310000,
        )
        assert params.max_days_limit == 365

    def test_year_ahead_forecast_margin_has_1_year_limit(self):
        """Test that YearAheadForecastMargin has 365 day limit."""
        params = YearAheadForecastMargin(
            out_bidding_zone_domain="10YDE-RWENET---I",  # Germany
            period_start=202401010000,
            period_end=202412310000,
        )
        assert params.max_days_limit == 365

    def test_energy_prices_has_1_year_limit(self):
        """Test that EnergyPrices has 365 day limit."""
        params = EnergyPrices(
            period_start=202401010000,
            period_end=202412310000,
            in_domain="10YDE-RWENET---I",  # Germany
            out_domain="10YDE-RWENET---I",  # Germany
        )
        assert params.max_days_limit == 365

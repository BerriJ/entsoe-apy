"""Load data parameter classes for ENTSO-E Transparency Platform."""

from .specific_params import (
    ActualTotalLoad,
    DayAheadTotalLoadForecast,
    MonthAheadTotalLoadForecast,
    WeekAheadTotalLoadForecast,
    YearAheadForecastMargin,
    YearAheadTotalLoadForecast,
)

__all__ = [
    "ActualTotalLoad",
    "DayAheadTotalLoadForecast",
    "WeekAheadTotalLoadForecast",
    "MonthAheadTotalLoadForecast",
    "YearAheadTotalLoadForecast",
    "YearAheadForecastMargin",
]

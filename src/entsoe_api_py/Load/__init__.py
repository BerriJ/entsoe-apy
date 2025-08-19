"""Load data parameter classes for ENTSO-E Transparency Platform."""

from ..Base.Load import Load as LoadParams
from .specific_params import (
    ActualTotalLoad,
    DayAheadTotalLoadForecast,
    MonthAheadTotalLoadForecast,
    WeekAheadTotalLoadForecast,
    YearAheadForecastMargin,
    YearAheadTotalLoadForecast,
)

__all__ = [
    "LoadParams",
    "ActualTotalLoad",
    "DayAheadTotalLoadForecast",
    "WeekAheadTotalLoadForecast",
    "MonthAheadTotalLoadForecast",
    "YearAheadTotalLoadForecast",
    "YearAheadForecastMargin",
]

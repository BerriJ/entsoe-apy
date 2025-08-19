"""Load data parameter classes for ENTSO-E Transparency Platform."""

from ..Base.Load import LoadParams
from .specific_params import (
    ActualTotalLoadParams,
    DayAheadTotalLoadForecastParams,
    MonthAheadTotalLoadForecastParams,
    WeekAheadTotalLoadForecastParams,
    YearAheadForecastMarginParams,
    YearAheadTotalLoadForecastParams,
)

__all__ = [
    "LoadParams",
    "ActualTotalLoadParams",
    "DayAheadTotalLoadForecastParams",
    "WeekAheadTotalLoadForecastParams",
    "MonthAheadTotalLoadForecastParams",
    "YearAheadTotalLoadForecastParams",
    "YearAheadForecastMarginParams",
]

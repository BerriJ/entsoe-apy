from decimal import Decimal
from typing import List, Optional, Protocol, runtime_checkable

from xsdata.models.datatype import XmlDuration

from entsoe.xml_models.urn_entsoe_eu_wgedi_codelists import (
    BusinessTypeList,
    CurveTypeList,
    UnitOfMeasureTypeList,
)


@runtime_checkable
class EsmpDateTimeInterval(Protocol):
    start: Optional[str]
    end: Optional[str]


@runtime_checkable
class Reason(Protocol):
    code: Optional[str]
    text: Optional[str]


@runtime_checkable
class Point(Protocol):
    position: Optional[int]
    quantity: Optional[Decimal]
    price_amount: Optional[Decimal]
    reason: list[Reason]


@runtime_checkable
class SeriesPeriod(Protocol):
    time_interval: Optional[EsmpDateTimeInterval]
    resolution: Optional[XmlDuration]
    point: List[Point]


@runtime_checkable
class TimeSeries(Protocol):
    m_rid: Optional[str]
    business_type: Optional[BusinessTypeList]
    quantity_measure_unit_name: Optional[UnitOfMeasureTypeList]
    curve_type: Optional[CurveTypeList]
    period: List[SeriesPeriod]

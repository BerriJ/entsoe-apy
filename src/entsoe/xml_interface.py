from decimal import Decimal
from typing import List, Optional, Protocol

from xsdata.models.datatype import XmlDuration

from entsoe.xml_models.urn_entsoe_eu_wgedi_codelists import (
    BusinessTypeList,
    CurveTypeList,
    UnitOfMeasureTypeList,
)


class EsmpDateTimeInterval(Protocol):
    start: Optional[str]
    end: Optional[str]


class Reason(Protocol):
    code: Optional[str]
    text: Optional[str]


class Point(Protocol):
    position: Optional[int]
    quantity: Optional[Decimal]
    price_amount: Optional[Decimal]
    reason: list[Reason]


class SeriesPeriod(Protocol):
    time_interval: Optional[EsmpDateTimeInterval]
    resolution: Optional[XmlDuration]
    point: List[Point]


class TimeSeries(Protocol):
    m_rid: Optional[str]
    business_type: Optional[BusinessTypeList]
    quantity_measure_unit_name: Optional[UnitOfMeasureTypeList]
    curve_type: Optional[CurveTypeList]
    period: List[SeriesPeriod]

from collections.abc import Iterable
from decimal import Decimal
from itertools import product
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


def is_iterable(obj):
    return isinstance(obj, Iterable) and not isinstance(obj, (str, bytes))


def flatten_to_rows(obj):
    if hasattr(obj, "__dict__"):
        values = []
        for value in vars(obj).values():
            if is_iterable(value):
                nested = []
                for item in value:
                    nested.extend(flatten_to_rows(item))
                values.append(nested)
            else:
                values.append([[value]])
        # Cartesian product of all attribute rows
        return [sum(row, []) for row in product(*values)]
    elif is_iterable(obj):
        rows = []
        for item in obj:
            rows.extend(flatten_to_rows(item))
        return rows
    else:
        return [[obj]]

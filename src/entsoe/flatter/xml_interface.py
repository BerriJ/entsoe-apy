from enum import Enum

from xsdata.models.datatype import XmlDuration

from entsoe.flatter.base import Flatter
from entsoe.xml_interface import EsmpDateTimeInterval, Reason

TS_FLATTER = Flatter({
    Enum: lambda key, value: {key: value.value},
    list[Reason]: lambda key, value: {key: ""},
    XmlDuration: lambda key, value: {
        key: value.data,
        "resolution_minutes": value.minutes,
    },
    EsmpDateTimeInterval: lambda key, value: {
        f"{key}-start": value.start,
        f"{key}-end": value.end,
    },
})

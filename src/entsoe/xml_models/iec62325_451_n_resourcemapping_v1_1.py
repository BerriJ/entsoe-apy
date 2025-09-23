from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDate, XmlTime
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    CodingSchemeTypeList,
    IndicatorTypeList,
    MessageTypeList,
    RoleTypeList,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-n:resourcemappingdocument:1:1"


class PartyIdString(BaseModel):
    class Meta:
        name = "PartyID_String"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 16,
        },
    )
    coding_scheme: CodingSchemeTypeList = field(
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
            "required": True,
        }
    )


class ResourceIdString(BaseModel):
    class Meta:
        name = "ResourceID_String"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 60,
        },
    )
    coding_scheme: CodingSchemeTypeList = field(
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
            "required": True,
        }
    )


class RegisteredResource(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcemappingdocument:1:1",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcemappingdocument:1:1",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcemappingdocument:1:1",
        },
    )


class TimeSeries(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcemappingdocument:1:1",
            "required": True,
            "max_length": 60,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcemappingdocument:1:1",
        },
    )
    cancelled_ts: Optional[IndicatorTypeList] = field(
        default=None,
        metadata={
            "name": "cancelledTS",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcemappingdocument:1:1",
        },
    )
    start_date_and_or_time_date: XmlDate = field(
        metadata={
            "name": "start_DateAndOrTime.date",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcemappingdocument:1:1",
            "required": True,
        }
    )
    start_date_and_or_time_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "start_DateAndOrTime.time",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcemappingdocument:1:1",
        },
    )
    end_date_and_or_time_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "end_DateAndOrTime.date",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcemappingdocument:1:1",
        },
    )
    end_date_and_or_time_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "end_DateAndOrTime.time",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcemappingdocument:1:1",
        },
    )
    market_registered_resource_m_rid: ResourceIdString = field(
        metadata={
            "name": "market_RegisteredResource.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcemappingdocument:1:1",
            "required": True,
        }
    )
    market_registered_resource_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "market_RegisteredResource.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcemappingdocument:1:1",
        },
    )
    market_registered_resource_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "market_RegisteredResource.description",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcemappingdocument:1:1",
        },
    )
    registered_resource: list[RegisteredResource] = field(
        default_factory=list,
        metadata={
            "name": "RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcemappingdocument:1:1",
            "min_occurs": 1,
        },
    )


class ResourceMappingMarketDocument(BaseModel):
    class Meta:
        name = "ResourceMapping_MarketDocument"
        namespace = (
            "urn:iec62325.351:tc57wg16:451-n:resourcemappingdocument:1:1"
        )

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "required": True,
            "max_length": 60,
        }
    )
    revision_number: str = field(
        metadata={
            "name": "revisionNumber",
            "type": "Element",
            "required": True,
            "pattern": r"[1-9]([0-9]){0,2}",
        }
    )
    type_value: MessageTypeList = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    sender_market_participant_m_rid: PartyIdString = field(
        metadata={
            "name": "sender_MarketParticipant.mRID",
            "type": "Element",
            "required": True,
        }
    )
    sender_market_participant_market_role_type: RoleTypeList = field(
        metadata={
            "name": "sender_MarketParticipant.marketRole.type",
            "type": "Element",
            "required": True,
        }
    )
    receiver_market_participant_m_rid: PartyIdString = field(
        metadata={
            "name": "receiver_MarketParticipant.mRID",
            "type": "Element",
            "required": True,
        }
    )
    receiver_market_participant_market_role_type: RoleTypeList = field(
        metadata={
            "name": "receiver_MarketParticipant.marketRole.type",
            "type": "Element",
            "required": True,
        }
    )
    created_date_time: str = field(
        metadata={
            "name": "createdDateTime",
            "type": "Element",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)",
        }
    )
    time_series: list[TimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "TimeSeries",
            "type": "Element",
            "min_occurs": 1,
        },
    )

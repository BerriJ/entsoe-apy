from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDate
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    AssetTypeList,
    CodingSchemeTypeList,
    CoordinateSystemTypeList,
    MessageTypeList,
    RoleTypeList,
    StatusTypeList,
)

__NAMESPACE__ = (
    "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0"
)


class ActionStatus(BaseModel):
    class Meta:
        name = "Action_Status"

    model_config = ConfigDict(defer_build=True)
    value: StatusTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
            "required": True,
        }
    )


class AreaIdString(BaseModel):
    class Meta:
        name = "AreaID_String"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 18,
        },
    )
    coding_scheme: CodingSchemeTypeList = field(
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
            "required": True,
        }
    )


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


class EnvironmentalMonitoringStation(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )
    location_m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "location.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )
    location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )
    location_position_points_x_position: Optional[str] = field(
        default=None,
        metadata={
            "name": "location.positionPoints.xPosition",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )
    location_position_points_y_position: Optional[str] = field(
        default=None,
        metadata={
            "name": "location.positionPoints.yPosition",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )
    location_position_points_z_position: Optional[str] = field(
        default=None,
        metadata={
            "name": "location.positionPoints.zPosition",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )
    location_coordinate_system_m_rid: Optional[CoordinateSystemTypeList] = (
        field(
            default=None,
            metadata={
                "name": "location.coordinateSystem.mRID",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
            },
        )
    )
    location_coordinate_system_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "location.coordinateSystem.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )


class RegisteredResource(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )
    p_srtype_psr_type: AssetTypeList = field(
        metadata={
            "name": "pSRType.psrType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
            "required": True,
        }
    )
    location_m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "location.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )
    location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )
    location_position_points_x_position: Optional[str] = field(
        default=None,
        metadata={
            "name": "location.positionPoints.xPosition",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )
    location_position_points_y_position: Optional[str] = field(
        default=None,
        metadata={
            "name": "location.positionPoints.yPosition",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )
    location_position_points_z_position: Optional[str] = field(
        default=None,
        metadata={
            "name": "location.positionPoints.zPosition",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )
    location_coordinate_system_m_rid: Optional[CoordinateSystemTypeList] = (
        field(
            default=None,
            metadata={
                "name": "location.coordinateSystem.mRID",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
            },
        )
    )
    location_coordinate_system_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "location.coordinateSystem.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )


class TimeSeries(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
            "required": True,
            "max_length": 35,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )
    start_date_and_or_time_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "start_DateAndOrTime.date",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )
    end_date_and_or_time_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "end_DateAndOrTime.date",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )
    associated_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "associated_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )
    registered_resource: list[RegisteredResource] = field(
        default_factory=list,
        metadata={
            "name": "RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
        },
    )
    environmental_monitoring_station: list[EnvironmentalMonitoringStation] = (
        field(
            default_factory=list,
            metadata={
                "name": "EnvironmentalMonitoringStation",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0",
            },
        )
    )


class WeatherConfigurationMarketDocument(BaseModel):
    class Meta:
        name = "WeatherConfiguration_MarketDocument"
        namespace = (
            "urn:iec62325.351:tc57wg16:451-n:weatherconfigurationdocument:1:0"
        )

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "required": True,
            "max_length": 35,
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
    doc_status: ActionStatus = field(
        metadata={
            "name": "docStatus",
            "type": "Element",
            "required": True,
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

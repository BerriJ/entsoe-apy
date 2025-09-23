from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDateTime, XmlDuration
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    BusinessTypeList,
    CodingSchemeTypeList,
    CurveTypeList,
    EnergyProductTypeList,
    FlowCommodityTypeList,
    MessageTypeList,
    ProcessTypeList,
    ReasonCodeTypeList,
    RoleTypeList,
    StatusTypeList,
    UnitOfMeasureTypeList,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0"


class EsmpDateTimeInterval(BaseModel):
    class Meta:
        name = "ESMP_DateTimeInterval"

    model_config = ConfigDict(defer_build=True)
    start: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )
    end: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )


class MeasurementPointIdString(BaseModel):
    class Meta:
        name = "MeasurementPointID_String"

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


class Series(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
            "max_length": 60,
        },
    )
    business_type: Optional[BusinessTypeList] = field(
        default=None,
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )
    product: Optional[EnergyProductTypeList] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )
    curve_type: Optional[CurveTypeList] = field(
        default=None,
        metadata={
            "name": "curveType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )
    flow_commodity_option: Optional[FlowCommodityTypeList] = field(
        default=None,
        metadata={
            "name": "flowCommodityOption",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )
    measurement_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "measurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )
    reading_period_resolution: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "reading_Period.resolution",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )
    reading_period_time_interval: Optional[EsmpDateTimeInterval] = field(
        default=None,
        metadata={
            "name": "reading_Period.timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )


class Permission(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
            "max_length": 60,
        },
    )
    created_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "createdDateTime",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)",
        },
    )
    permitted_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "permitted_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )
    permitted_market_participant_market_role_type: Optional[RoleTypeList] = (
        field(
            default=None,
            metadata={
                "name": "permitted_MarketParticipant.marketRole.type",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
            },
        )
    )
    permitting_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "permitting_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )
    permitting_market_participant_market_role_type: Optional[RoleTypeList] = (
        field(
            default=None,
            metadata={
                "name": "permitting_MarketParticipant.marketRole.type",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
            },
        )
    )
    purpose_reason_code: Optional[ReasonCodeTypeList] = field(
        default=None,
        metadata={
            "name": "purpose_Reason.code",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )
    purpose_reason_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "purpose_Reason.text",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
            "max_length": 512,
        },
    )
    permission_end_date_and_or_time_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "permissionEnd_DateAndOrTime.dateTime",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )
    max_lifetime_permission_date_and_or_time_date_time: Optional[
        XmlDateTime
    ] = field(
        default=None,
        metadata={
            "name": "maxLifetimePermission_DateAndOrTime.dateTime",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )
    end_of_permission_reason_code: Optional[ReasonCodeTypeList] = field(
        default=None,
        metadata={
            "name": "endOfPermission_Reason.code",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )
    end_of_permission_reason_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "endOfPermission_Reason.text",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
            "max_length": 512,
        },
    )
    permission_status_status: Optional[StatusTypeList] = field(
        default=None,
        metadata={
            "name": "permissionStatus.status",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )
    transmission_schedule_period_resolution: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "transmissionSchedule_Period.resolution",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )
    transmission_schedule_period_time_interval: Optional[
        EsmpDateTimeInterval
    ] = field(
        default=None,
        metadata={
            "name": "transmissionSchedule_Period.timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )
    series: list[Series] = field(
        default_factory=list,
        metadata={
            "name": "Series",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )


class AccountingPoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: Optional[MeasurementPointIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )
    flow_commodity_option: Optional[FlowCommodityTypeList] = field(
        default=None,
        metadata={
            "name": "flowCommodityOption",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )
    permission: list[Permission] = field(
        default_factory=list,
        metadata={
            "name": "Permission",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )


class MktActivityRecord(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
            "required": True,
        }
    )
    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
            "required": True,
        }
    )
    accounting_point: list[AccountingPoint] = field(
        default_factory=list,
        metadata={
            "name": "AccountingPoint",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0",
        },
    )


class PermissionMarketDocument(BaseModel):
    class Meta:
        name = "Permission_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-n:permissiondocument:1:0"

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "required": True,
            "max_length": 60,
        }
    )
    type_value: MessageTypeList = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    process_process_type: ProcessTypeList = field(
        metadata={
            "name": "process.processType",
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
    period_time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "period.timeInterval",
            "type": "Element",
            "required": True,
        }
    )
    mkt_activity_record: list[MktActivityRecord] = field(
        default_factory=list,
        metadata={
            "name": "MktActivityRecord",
            "type": "Element",
        },
    )

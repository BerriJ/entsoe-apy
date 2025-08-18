from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDuration

from xml_models.urn_entsoe_eu_wgedi_codelists import (
    AssetTypeList,
    BusinessTypeList,
    CodingSchemeTypeList,
    MessageTypeList,
    ProcessTypeList,
    ReasonCodeTypeList,
    RoleTypeList,
    StatusTypeList,
    UnitOfMeasureTypeList,
    UnitSymbol,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1"


@dataclass
class EsmpDateTimeInterval:
    class Meta:
        name = "ESMP_DateTimeInterval"

    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        },
    )
    end: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        },
    )


@dataclass
class AreaIdString:
    class Meta:
        name = "AreaID_String"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 18,
        },
    )
    coding_scheme: Optional[CodingSchemeTypeList] = field(
        default=None,
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EsmpVoltage:
    class Meta:
        name = "ESMP_Voltage"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"([0-9]*\.?[0-9]*)",
        },
    )
    unit: UnitSymbol = field(
        init=False,
        default=UnitSymbol.KVT,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PartyIdString:
    class Meta:
        name = "PartyID_String"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 16,
        },
    )
    coding_scheme: Optional[CodingSchemeTypeList] = field(
        default=None,
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Reason:
    code: Optional[ReasonCodeTypeList] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
            "required": True,
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
            "max_length": 512,
        },
    )


@dataclass
class ResourceIdString:
    class Meta:
        name = "ResourceID_String"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 60,
        },
    )
    coding_scheme: Optional[CodingSchemeTypeList] = field(
        default=None,
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SwitchedBackTimePeriod:
    class Meta:
        name = "SwitchedBack_Time_Period"

    time_interval: Optional[EsmpDateTimeInterval] = field(
        default=None,
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
            "required": True,
        },
    )


@dataclass
class AlternativeRegisteredResource:
    class Meta:
        name = "Alternative_RegisteredResource"

    m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
            "required": True,
        },
    )


@dataclass
class RegisteredResource:
    m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
            "required": True,
        },
    )
    p_srtype_psr_type: Optional[AssetTypeList] = field(
        default=None,
        metadata={
            "name": "pSRType.psrType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
        },
    )
    p_srtype_power_system_resources_high_voltage_limit: Optional[
        EsmpVoltage
    ] = field(
        default=None,
        metadata={
            "name": "pSRType.powerSystemResources.highVoltageLimit",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
        },
    )
    p_srtype_power_system_resources_low_voltage_limit: Optional[
        EsmpVoltage
    ] = field(
        default=None,
        metadata={
            "name": "pSRType.powerSystemResources.lowVoltageLimit",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
        },
    )


@dataclass
class TimeSeries:
    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
            "required": True,
            "max_length": 60,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
        },
    )
    business_type: Optional[BusinessTypeList] = field(
        default=None,
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
            "required": True,
        },
    )
    project_names_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "project_Names.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
        },
    )
    case_reference_names_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "caseReference_Names.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
        },
    )
    outage_period_time_interval: Optional[EsmpDateTimeInterval] = field(
        default=None,
        metadata={
            "name": "outage_Period.timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
            "required": True,
        },
    )
    last_change_market_agreement_created_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastChange_MarketAgreement.createdDateTime",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)",
        },
    )
    positive_offset_constraint_duration_duration: Optional[XmlDuration] = (
        field(
            default=None,
            metadata={
                "name": "positiveOffset_ConstraintDuration.duration",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
            },
        )
    )
    negative_offset_constraint_duration_duration: Optional[XmlDuration] = (
        field(
            default=None,
            metadata={
                "name": "negativeOffset_ConstraintDuration.duration",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
            },
        )
    )
    no_restitution_constraint_duration_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "noRestitution_ConstraintDuration.type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
        },
    )
    maximum_restitution_constraint_duration_duration: Optional[XmlDuration] = (
        field(
            default=None,
            metadata={
                "name": "maximumRestitution_ConstraintDuration.duration",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
            },
        )
    )
    day_time_restitution_constraint_duration_duration: Optional[
        XmlDuration
    ] = field(
        default=None,
        metadata={
            "name": "dayTimeRestitution_ConstraintDuration.duration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
        },
    )
    night_time_restitution_constraint_duration_duration: Optional[
        XmlDuration
    ] = field(
        default=None,
        metadata={
            "name": "nightTimeRestitution_ConstraintDuration.duration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
        },
    )
    week_end_restitution_constraint_duration_duration: Optional[
        XmlDuration
    ] = field(
        default=None,
        metadata={
            "name": "weekEndRestitution_ConstraintDuration.duration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
        },
    )
    market_object_status_status: Optional[StatusTypeList] = field(
        default=None,
        metadata={
            "name": "marketObjectStatus.status",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
            "required": True,
        },
    )
    coordination_market_object_status_status: Optional[StatusTypeList] = field(
        default=None,
        metadata={
            "name": "coordination_MarketObjectStatus.status",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
        },
    )
    measurement_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "measurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
        },
    )
    unavailable_capacity_quantity_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "unavailableCapacity_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
        },
    )
    day_market_object_status_status: Optional[StatusTypeList] = field(
        default=None,
        metadata={
            "name": "day_MarketObjectStatus.status",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
            "required": True,
        },
    )
    week_market_object_status_status: Optional[StatusTypeList] = field(
        default=None,
        metadata={
            "name": "week_MarketObjectStatus.status",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
        },
    )
    saturday_market_object_status_status: Optional[StatusTypeList] = field(
        default=None,
        metadata={
            "name": "saturday_MarketObjectStatus.status",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
        },
    )
    sunday_market_object_status_status: Optional[StatusTypeList] = field(
        default=None,
        metadata={
            "name": "sunday_MarketObjectStatus.status",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
        },
    )
    registered_resource: list[RegisteredResource] = field(
        default_factory=list,
        metadata={
            "name": "RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
            "min_occurs": 1,
        },
    )
    alternative_registered_resource: list[AlternativeRegisteredResource] = (
        field(
            default_factory=list,
            metadata={
                "name": "Alternative_RegisteredResource",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
            },
        )
    )
    switched_back_period: list[SwitchedBackTimePeriod] = field(
        default_factory=list,
        metadata={
            "name": "SwitchedBack_Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1",
        },
    )


@dataclass
class OutageScheduleMarketDocument:
    class Meta:
        name = "OutageSchedule_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-n:mltopdocument:1:1"

    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "required": True,
            "max_length": 60,
        },
    )
    revision_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "revisionNumber",
            "type": "Element",
            "required": True,
            "pattern": r"[1-9]([0-9]){0,2}",
        },
    )
    type_value: Optional[MessageTypeList] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    process_process_type: Optional[ProcessTypeList] = field(
        default=None,
        metadata={
            "name": "process.processType",
            "type": "Element",
            "required": True,
        },
    )
    sender_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "sender_MarketParticipant.mRID",
            "type": "Element",
            "required": True,
        },
    )
    sender_market_participant_market_role_type: Optional[RoleTypeList] = field(
        default=None,
        metadata={
            "name": "sender_MarketParticipant.marketRole.type",
            "type": "Element",
            "required": True,
        },
    )
    receiver_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "receiver_MarketParticipant.mRID",
            "type": "Element",
            "required": True,
        },
    )
    receiver_market_participant_market_role_type: Optional[RoleTypeList] = (
        field(
            default=None,
            metadata={
                "name": "receiver_MarketParticipant.marketRole.type",
                "type": "Element",
                "required": True,
            },
        )
    )
    created_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "createdDateTime",
            "type": "Element",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)",
        },
    )
    schedule_period_time_interval: Optional[EsmpDateTimeInterval] = field(
        default=None,
        metadata={
            "name": "schedule_Period.timeInterval",
            "type": "Element",
        },
    )
    domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "domain.mRID",
            "type": "Element",
            "required": True,
        },
    )
    time_series: list[TimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "TimeSeries",
            "type": "Element",
        },
    )

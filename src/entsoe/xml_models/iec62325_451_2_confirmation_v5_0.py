from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDuration
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    BusinessTypeList,
    CodingSchemeTypeList,
    ContractTypeList,
    CurveTypeList,
    EnergyProductTypeList,
    MessageTypeList,
    ObjectAggregationTypeList,
    ProcessTypeList,
    ReasonCodeTypeList,
    RoleTypeList,
    UnitOfMeasureTypeList,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0"


class EsmpDateTimeInterval(BaseModel):
    class Meta:
        name = "ESMP_DateTimeInterval"

    model_config = ConfigDict(defer_build=True)
    start: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )
    end: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
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


class MeasurementPointIdString(BaseModel):
    class Meta:
        name = "MeasurementPointID_String"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 35,
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


class Reason(BaseModel):
    model_config = ConfigDict(defer_build=True)
    code: ReasonCodeTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "required": True,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "max_length": 512,
        },
    )


class Point(BaseModel):
    model_config = ConfigDict(defer_build=True)
    position: int = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )
    quantity: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "required": True,
        }
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
        },
    )


class SeriesPeriod(BaseModel):
    class Meta:
        name = "Series_Period"

    model_config = ConfigDict(defer_build=True)
    time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "required": True,
        }
    )
    resolution: XmlDuration = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "required": True,
        }
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "min_occurs": 1,
        },
    )


class ConfirmedTimeSeries(BaseModel):
    class Meta:
        name = "Confirmed_TimeSeries"

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "required": True,
            "max_length": 35,
        }
    )
    version: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "required": True,
            "pattern": r"[1-9]([0-9]){0,2}",
        }
    )
    business_type: BusinessTypeList = field(
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "required": True,
        }
    )
    product: EnergyProductTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "required": True,
        }
    )
    object_aggregation: ObjectAggregationTypeList = field(
        metadata={
            "name": "objectAggregation",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "required": True,
        }
    )
    in_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
        },
    )
    out_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
        },
    )
    market_evaluation_point_m_rid: Optional[MeasurementPointIdString] = field(
        default=None,
        metadata={
            "name": "marketEvaluationPoint.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
        },
    )
    in_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "in_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
        },
    )
    out_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "out_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
        },
    )
    market_agreement_type: Optional[ContractTypeList] = field(
        default=None,
        metadata={
            "name": "marketAgreement.type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
        },
    )
    market_agreement_m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "marketAgreement.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "max_length": 35,
        },
    )
    measure_unit_name: UnitOfMeasureTypeList = field(
        metadata={
            "name": "measure_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "required": True,
        }
    )
    curve_type: Optional[CurveTypeList] = field(
        default=None,
        metadata={
            "name": "curveType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
        },
    )
    period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
        },
    )


class ImposedTimeSeries(BaseModel):
    class Meta:
        name = "Imposed_TimeSeries"

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "required": True,
            "max_length": 35,
        }
    )
    version: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "required": True,
            "pattern": r"[1-9]([0-9]){0,2}",
        }
    )
    business_type: BusinessTypeList = field(
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "required": True,
        }
    )
    product: EnergyProductTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "required": True,
        }
    )
    object_aggregation: ObjectAggregationTypeList = field(
        metadata={
            "name": "objectAggregation",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "required": True,
        }
    )
    in_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
        },
    )
    out_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
        },
    )
    market_evaluation_point_m_rid: Optional[MeasurementPointIdString] = field(
        default=None,
        metadata={
            "name": "marketEvaluationPoint.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
        },
    )
    in_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "in_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
        },
    )
    out_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "out_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
        },
    )
    market_agreement_type: Optional[ContractTypeList] = field(
        default=None,
        metadata={
            "name": "marketAgreement.type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
        },
    )
    market_agreement_m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "marketAgreement.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "max_length": 35,
        },
    )
    measure_unit_name: UnitOfMeasureTypeList = field(
        metadata={
            "name": "measure_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "required": True,
        }
    )
    curve_type: Optional[CurveTypeList] = field(
        default=None,
        metadata={
            "name": "curveType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
        },
    )
    period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "min_occurs": 1,
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0",
            "min_occurs": 1,
        },
    )


class ConfirmationMarketDocument(BaseModel):
    class Meta:
        name = "Confirmation_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-2:confirmationdocument:5:0"

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "required": True,
            "max_length": 35,
        }
    )
    type_value: MessageTypeList = field(
        metadata={
            "name": "type",
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
    schedule_period_time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "schedule_Period.timeInterval",
            "type": "Element",
            "required": True,
        }
    )
    confirmed_market_document_m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "confirmed_MarketDocument.mRID",
            "type": "Element",
            "max_length": 35,
        },
    )
    confirmed_market_document_revision_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "confirmed_MarketDocument.revisionNumber",
            "type": "Element",
            "pattern": r"[1-9]([0-9]){0,2}",
        },
    )
    domain_m_rid: AreaIdString = field(
        metadata={
            "name": "domain.mRID",
            "type": "Element",
            "required": True,
        }
    )
    subject_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "subject_MarketParticipant.mRID",
            "type": "Element",
        },
    )
    subject_market_participant_market_role_type: Optional[RoleTypeList] = (
        field(
            default=None,
            metadata={
                "name": "subject_MarketParticipant.marketRole.type",
                "type": "Element",
            },
        )
    )
    process_process_type: Optional[ProcessTypeList] = field(
        default=None,
        metadata={
            "name": "process.processType",
            "type": "Element",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    imposed_time_series: list[ImposedTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "Imposed_TimeSeries",
            "type": "Element",
        },
    )
    confirmed_time_series: list[ConfirmedTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "Confirmed_TimeSeries",
            "type": "Element",
        },
    )

from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDuration
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    BusinessTypeList,
    CodingSchemeTypeList,
    EnergyProductTypeList,
    MessageTypeList,
    ProcessTypeList,
    RoleTypeList,
    TarifTypeTypeList,
    UnitOfMeasureTypeList,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0"


class EsmpDateTimeInterval(BaseModel):
    class Meta:
        name = "ESMP_DateTimeInterval"

    model_config = ConfigDict(defer_build=True)
    start: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )
    end: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
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


class DomainAccountAceTariffType(BaseModel):
    class Meta:
        name = "DomainAccount_AceTariffType"

    model_config = ConfigDict(defer_build=True)
    type_value: TarifTypeTypeList = field(
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
            "required": True,
        }
    )
    opening_point_quantity: Decimal = field(
        metadata={
            "name": "opening_Point.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
            "required": True,
        }
    )
    closing_point_quantity: Decimal = field(
        metadata={
            "name": "closing_Point.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
            "required": True,
        }
    )
    compensation_point_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "compensation_Point.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
        },
    )
    measure_unit_name: UnitOfMeasureTypeList = field(
        metadata={
            "name": "measure_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
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


class Point(BaseModel):
    model_config = ConfigDict(defer_build=True)
    position: int = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )
    quantity: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
            "required": True,
        }
    )
    secondary_quantity: Decimal = field(
        metadata={
            "name": "secondaryQuantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
            "required": True,
        }
    )
    ace_tariff_type_type: Optional[TarifTypeTypeList] = field(
        default=None,
        metadata={
            "name": "aceTariffType.type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
            "required": True,
        }
    )
    resolution: XmlDuration = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
            "required": True,
        }
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
            "min_occurs": 1,
        },
    )


class TimeSeries(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
            "required": True,
            "max_length": 35,
        }
    )
    business_type: BusinessTypeList = field(
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
            "required": True,
        }
    )
    product: EnergyProductTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
            "required": True,
        }
    )
    subject_domain_m_rid: AreaIdString = field(
        metadata={
            "name": "subject_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
            "required": True,
        }
    )
    area_domain_m_rid: AreaIdString = field(
        metadata={
            "name": "area_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
            "required": True,
        }
    )
    market_evaluation_point_m_rid: Optional[MeasurementPointIdString] = field(
        default=None,
        metadata={
            "name": "marketEvaluationPoint.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
        },
    )
    measure_unit_name: UnitOfMeasureTypeList = field(
        metadata={
            "name": "measure_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
            "required": True,
        }
    )
    period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0",
            "min_occurs": 1,
        },
    )


class RgcesettlementMarketDocument(BaseModel):
    class Meta:
        name = "RGCEsettlement_MarketDocument"
        namespace = (
            "urn:iec62325.351:tc57wg16:451-n:rgcesettlementdocument:1:0"
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
    recording_period_time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "recording_Period.timeInterval",
            "type": "Element",
            "required": True,
        }
    )
    compensation_period_time_interval: Optional[EsmpDateTimeInterval] = field(
        default=None,
        metadata={
            "name": "compensation_Period.timeInterval",
            "type": "Element",
        },
    )
    domain_m_rid: AreaIdString = field(
        metadata={
            "name": "domain.mRID",
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
    domain_account_ace_tariff_type: list[DomainAccountAceTariffType] = field(
        default_factory=list,
        metadata={
            "name": "DomainAccount_AceTariffType",
            "type": "Element",
            "min_occurs": 1,
        },
    )

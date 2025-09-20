from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDuration
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    BusinessTypeList,
    CodingSchemeTypeList,
    ContractTypeList,
    CurrencyTypeList,
    CurveTypeList,
    DirectionTypeList,
    MessageTypeList,
    ProcessTypeList,
    ReasonCodeTypeList,
    RoleTypeList,
    UnitOfMeasureTypeList,
)

__NAMESPACE__ = (
    "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3"
)


class EsmpDateTimeInterval(BaseModel):
    class Meta:
        name = "ESMP_DateTimeInterval"

    model_config = ConfigDict(defer_build=True)
    start: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )
    end: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "required": True,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "max_length": 512,
        },
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


class Point(BaseModel):
    model_config = ConfigDict(defer_build=True)
    position: int = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )
    quantity: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "required": True,
        }
    )
    price_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "price.amount",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "total_digits": 17,
        },
    )
    secondary_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "secondaryQuantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
        },
    )
    bid_price_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "bid_Price.amount",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "total_digits": 17,
        },
    )
    bid_energy_price_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "bidEnergy_Price.amount",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "total_digits": 17,
        },
    )
    energy_price_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "energy_Price.amount",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "total_digits": 17,
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "required": True,
        }
    )
    resolution: XmlDuration = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "required": True,
        }
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "min_occurs": 1,
        },
    )


class TimeSeries(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "required": True,
            "max_length": 60,
        }
    )
    bid_original_market_document_m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "bid_Original_MarketDocument.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "max_length": 60,
        },
    )
    bid_original_market_document_revision_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "bid_Original_MarketDocument.revisionNumber",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "pattern": r"[1-9]([0-9]){0,2}",
        },
    )
    bid_original_market_document_bid_bid_time_series_m_rid: Optional[str] = (
        field(
            default=None,
            metadata={
                "name": "bid_Original_MarketDocument.bid_BidTimeSeries.mRID",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
                "max_length": 60,
            },
        )
    )
    bid_original_market_document_tendering_market_participant_m_rid: PartyIdString = field(
        metadata={
            "name": "bid_Original_MarketDocument.tendering_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "required": True,
        }
    )
    auction_m_rid: str = field(
        metadata={
            "name": "auction.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "required": True,
            "max_length": 60,
        }
    )
    business_type: BusinessTypeList = field(
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "required": True,
        }
    )
    acquiring_domain_m_rid: AreaIdString = field(
        metadata={
            "name": "acquiring_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "required": True,
        }
    )
    connecting_domain_m_rid: AreaIdString = field(
        metadata={
            "name": "connecting_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "required": True,
        }
    )
    market_agreement_type: ContractTypeList = field(
        metadata={
            "name": "marketAgreement.type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "required": True,
        }
    )
    market_agreement_m_rid: str = field(
        metadata={
            "name": "marketAgreement.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "required": True,
            "max_length": 60,
        }
    )
    market_agreement_created_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "marketAgreement.createdDateTime",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)",
        },
    )
    quantity_measurement_unit_name: UnitOfMeasureTypeList = field(
        metadata={
            "name": "quantity_Measurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "required": True,
        }
    )
    currency_unit_name: Optional[CurrencyTypeList] = field(
        default=None,
        metadata={
            "name": "currency_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
        },
    )
    price_measurement_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "price_Measurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
        },
    )
    energy_measurement_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "energy_Measurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
        },
    )
    registered_resource_m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "registeredResource.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
        },
    )
    flow_direction_direction: DirectionTypeList = field(
        metadata={
            "name": "flowDirection.direction",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "required": True,
        }
    )
    minimum_activation_quantity_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "minimumActivation_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
        },
    )
    step_increment_quantity_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "stepIncrement_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
        },
    )
    order_number_attribute_instance_component_position: Optional[int] = field(
        default=None,
        metadata={
            "name": "orderNumber_AttributeInstanceComponent.position",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "min_inclusive": 1,
            "max_inclusive": 999999,
        },
    )
    activation_constraint_duration_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "activation_ConstraintDuration.duration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
        },
    )
    resting_constraint_duration_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "resting_ConstraintDuration.duration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
        },
    )
    minimum_constraint_duration_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "minimum_ConstraintDuration.duration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
        },
    )
    maximum_constraint_duration_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "maximum_ConstraintDuration.duration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
        },
    )
    curve_type: Optional[CurveTypeList] = field(
        default=None,
        metadata={
            "name": "curveType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
        },
    )
    period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
            "min_occurs": 1,
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3",
        },
    )


class ReserveAllocationResultMarketDocument(BaseModel):
    class Meta:
        name = "ReserveAllocationResult_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:3"

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
    process_process_type: Optional[ProcessTypeList] = field(
        default=None,
        metadata={
            "name": "process.processType",
            "type": "Element",
        },
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
    reserve_bid_period_time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "reserveBid_Period.timeInterval",
            "type": "Element",
            "required": True,
        }
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
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
        },
    )

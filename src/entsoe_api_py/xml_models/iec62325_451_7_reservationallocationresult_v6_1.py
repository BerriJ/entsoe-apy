from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .urn_entsoe_eu_wgedi_codelists import (
    BusinessTypeList,
    CodingSchemeTypeList,
    ContractTypeList,
    CurrencyTypeList,
    DirectionTypeList,
    MessageTypeList,
    ProcessTypeList,
    ReasonCodeTypeList,
    RoleTypeList,
    UnitOfMeasureTypeList,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1"


@dataclass
class AttributeInstanceComponent:
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        },
    )


@dataclass
class Auction:
    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
            "max_length": 60,
        },
    )


@dataclass
class BidTimeSeries:
    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
            "max_length": 60,
        },
    )


@dataclass
class ConstraintDuration:
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )


@dataclass
class EsmpDateTimeInterval:
    class Meta:
        name = "ESMP_DateTimeInterval"

    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        },
    )
    end: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        },
    )


@dataclass
class Price:
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
            "total_digits": 17,
        },
    )


@dataclass
class Quantity:
    quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
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
class ContractMarketAgreement:
    class Meta:
        name = "Contract_MarketAgreement"

    type_value: Optional[ContractTypeList] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )
    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
            "max_length": 60,
        },
    )
    created_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "createdDateTime",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)",
        },
    )


@dataclass
class CurrencyUnit:
    class Meta:
        name = "Currency_Unit"

    name: Optional[CurrencyTypeList] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )


@dataclass
class FlowDirection:
    direction: Optional[DirectionTypeList] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )


@dataclass
class MarketRole:
    type_value: Optional[RoleTypeList] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )


@dataclass
class MeasureUnit:
    class Meta:
        name = "Measure_Unit"

    name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
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
class Process:
    process_type: Optional[ProcessTypeList] = field(
        default=None,
        metadata={
            "name": "processType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )


@dataclass
class Reason:
    code: Optional[ReasonCodeTypeList] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
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
class TimePeriod:
    class Meta:
        name = "Time_Period"

    time_interval: Optional[EsmpDateTimeInterval] = field(
        default=None,
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )


@dataclass
class Domain:
    m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )


@dataclass
class MarketParticipant:
    m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )
    market_role: Optional[MarketRole] = field(
        default=None,
        metadata={
            "name": "MarketRole",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )


@dataclass
class Point:
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        },
    )
    quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )
    price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    secondary_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "secondaryQuantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    bid_price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "Bid_Price",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    bid_energy_price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "BidEnergy_Price",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    energy_price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "Energy_Price",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )


@dataclass
class RegisteredResource:
    m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )


@dataclass
class TenderingMarketParticipant:
    class Meta:
        name = "Tendering_MarketParticipant"

    m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )


@dataclass
class OriginalMarketDocument:
    class Meta:
        name = "Original_MarketDocument"

    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "max_length": 60,
        },
    )
    revision_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "revisionNumber",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "pattern": r"[1-9]([0-9]){0,2}",
        },
    )
    bid_bid_time_series: Optional[BidTimeSeries] = field(
        default=None,
        metadata={
            "name": "Bid_BidTimeSeries",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    tendering_market_participant: Optional[TenderingMarketParticipant] = field(
        default=None,
        metadata={
            "name": "Tendering_MarketParticipant",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )


@dataclass
class SeriesPeriod:
    class Meta:
        name = "Series_Period"

    time_interval: Optional[EsmpDateTimeInterval] = field(
        default=None,
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )
    resolution: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "min_occurs": 1,
        },
    )


@dataclass
class TimeSeries:
    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
            "max_length": 60,
        },
    )
    bid_original_market_document: Optional[OriginalMarketDocument] = field(
        default=None,
        metadata={
            "name": "Bid_Original_MarketDocument",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )
    auction: Optional[Auction] = field(
        default=None,
        metadata={
            "name": "Auction",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )
    business_type: Optional[BusinessTypeList] = field(
        default=None,
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )
    acquiring_domain: Optional[Domain] = field(
        default=None,
        metadata={
            "name": "Acquiring_Domain",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )
    connecting_domain: Optional[Domain] = field(
        default=None,
        metadata={
            "name": "Connecting_Domain",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )
    market_agreement: Optional[ContractMarketAgreement] = field(
        default=None,
        metadata={
            "name": "MarketAgreement",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )
    quantity_measure_unit: Optional[MeasureUnit] = field(
        default=None,
        metadata={
            "name": "Quantity_Measure_Unit",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )
    currency_unit: Optional[CurrencyUnit] = field(
        default=None,
        metadata={
            "name": "Currency_Unit",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    price_measure_unit: Optional[MeasureUnit] = field(
        default=None,
        metadata={
            "name": "Price_Measure_Unit",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    energy_measurement_unit: Optional[MeasureUnit] = field(
        default=None,
        metadata={
            "name": "Energy_Measurement_Unit",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    registered_resource: Optional[RegisteredResource] = field(
        default=None,
        metadata={
            "name": "RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    flow_direction: Optional[FlowDirection] = field(
        default=None,
        metadata={
            "name": "FlowDirection",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        },
    )
    minimum_activation_quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "MinimumActivation_Quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    step_increment_quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "StepIncrement_Quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    order_number_attribute_instance_component: Optional[AttributeInstanceComponent] = (
        field(
            default=None,
            metadata={
                "name": "OrderNumber_AttributeInstanceComponent",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            },
        )
    )
    activation_constraint_duration: Optional[ConstraintDuration] = field(
        default=None,
        metadata={
            "name": "Activation_ConstraintDuration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    resting_constraint_duration: Optional[ConstraintDuration] = field(
        default=None,
        metadata={
            "name": "Resting_ConstraintDuration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    minimum_constraint_duration: Optional[ConstraintDuration] = field(
        default=None,
        metadata={
            "name": "Minimum_ConstraintDuration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    maximum_constraint_duration: Optional[ConstraintDuration] = field(
        default=None,
        metadata={
            "name": "Maximum_ConstraintDuration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "min_occurs": 1,
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )


@dataclass
class ReserveAllocationResultMarketDocument:
    class Meta:
        name = "ReserveAllocationResult_MarketDocument"
        namespace = (
            "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1"
        )

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
    process: Optional[Process] = field(
        default=None,
        metadata={
            "name": "Process",
            "type": "Element",
        },
    )
    sender_market_participant: Optional[MarketParticipant] = field(
        default=None,
        metadata={
            "name": "Sender_MarketParticipant",
            "type": "Element",
            "required": True,
        },
    )
    receiver_market_participant: Optional[MarketParticipant] = field(
        default=None,
        metadata={
            "name": "Receiver_MarketParticipant",
            "type": "Element",
            "required": True,
        },
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
    reserve_bid_period: Optional[TimePeriod] = field(
        default=None,
        metadata={
            "name": "ReserveBid_Period",
            "type": "Element",
            "required": True,
        },
    )
    domain: Optional[Domain] = field(
        default=None,
        metadata={
            "name": "Domain",
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
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
        },
    )

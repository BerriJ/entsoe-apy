from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .urn_entsoe_eu_wgedi_codelists import (
    AssetTypeList,
    BusinessTypeList,
    CodingSchemeTypeList,
    ContractTypeList,
    CurrencyTypeList,
    DirectionTypeList,
    IndicatorTypeList,
    MarketProductTypeList,
    MessageTypeList,
    ProcessTypeList,
    ReasonCodeTypeList,
    RoleTypeList,
    StatusTypeList,
    UnitOfMeasureTypeList,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4"


@dataclass
class EsmpDateTimeInterval:
    class Meta:
        name = "ESMP_DateTimeInterval"

    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        },
    )
    end: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        },
    )


@dataclass
class Point:
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        },
    )
    quantity_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "required": True,
        },
    )
    minimum_quantity_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "minimum_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    price_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "price.amount",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "total_digits": 17,
        },
    )
    energy_price_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "energy_Price.amount",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "total_digits": 17,
        },
    )


@dataclass
class ActionStatus:
    class Meta:
        name = "Action_Status"

    value: Optional[StatusTypeList] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "required": True,
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
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
class SeriesPeriod:
    class Meta:
        name = "Series_Period"

    time_interval: Optional[EsmpDateTimeInterval] = field(
        default=None,
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "required": True,
        },
    )
    resolution: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "required": True,
        },
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "min_occurs": 1,
        },
    )


@dataclass
class BiddingZoneDomain:
    class Meta:
        name = "BiddingZone_Domain"

    m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )


@dataclass
class LinkedBidTimeSeries:
    class Meta:
        name = "Linked_BidTimeSeries"

    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "required": True,
            "max_length": 60,
        },
    )
    status: Optional[ActionStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )


@dataclass
class OriginMarketParticipant:
    class Meta:
        name = "Origin_MarketParticipant"

    m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "required": True,
        },
    )


@dataclass
class BidTimeSeries:
    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "required": True,
            "max_length": 60,
        },
    )
    auction_m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "auction.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "max_length": 60,
        },
    )
    business_type: Optional[BusinessTypeList] = field(
        default=None,
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "required": True,
        },
    )
    acquiring_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "acquiring_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "required": True,
        },
    )
    connecting_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "connecting_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "required": True,
        },
    )
    provider_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "provider_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    quantity_measurement_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "quantity_Measurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "required": True,
        },
    )
    currency_unit_name: Optional[CurrencyTypeList] = field(
        default=None,
        metadata={
            "name": "currency_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    price_measurement_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "price_Measurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    divisible: Optional[IndicatorTypeList] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "required": True,
        },
    )
    linked_bids_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "linkedBidsIdentification",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "max_length": 60,
        },
    )
    multipart_bid_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "multipartBidIdentification",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "max_length": 60,
        },
    )
    exclusive_bids_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "exclusiveBidsIdentification",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "max_length": 60,
        },
    )
    block_bid: Optional[IndicatorTypeList] = field(
        default=None,
        metadata={
            "name": "blockBid",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    status: Optional[ActionStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    priority: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    registered_resource_m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "registeredResource.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    flow_direction_direction: Optional[DirectionTypeList] = field(
        default=None,
        metadata={
            "name": "flowDirection.direction",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "required": True,
        },
    )
    step_increment_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "stepIncrementQuantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    energy_price_measurement_unit_name: Optional[UnitOfMeasureTypeList] = (
        field(
            default=None,
            metadata={
                "name": "energyPrice_Measurement_Unit.name",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            },
        )
    )
    market_agreement_type: Optional[ContractTypeList] = field(
        default=None,
        metadata={
            "name": "marketAgreement.type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    market_agreement_m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "marketAgreement.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "max_length": 60,
        },
    )
    market_agreement_created_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "marketAgreement.createdDateTime",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)",
        },
    )
    activation_constraint_duration_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "activation_ConstraintDuration.duration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    resting_constraint_duration_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "resting_ConstraintDuration.duration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    minimum_constraint_duration_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "minimum_ConstraintDuration.duration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    maximum_constraint_duration_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "maximum_ConstraintDuration.duration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    standard_market_product_market_product_type: Optional[
        MarketProductTypeList
    ] = field(
        default=None,
        metadata={
            "name": "standard_MarketProduct.marketProductType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    original_market_product_market_product_type: Optional[
        MarketProductTypeList
    ] = field(
        default=None,
        metadata={
            "name": "original_MarketProduct.marketProductType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    validity_period_time_interval: Optional[EsmpDateTimeInterval] = field(
        default=None,
        metadata={
            "name": "validity_Period.timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    inclusive_bids_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "inclusiveBidsIdentification",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "max_length": 60,
        },
    )
    mkt_psrtype_psr_type: Optional[AssetTypeList] = field(
        default=None,
        metadata={
            "name": "mktPSRType.psrType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
            "min_occurs": 1,
        },
    )
    available_bidding_zone_domain: list[BiddingZoneDomain] = field(
        default_factory=list,
        metadata={
            "name": "AvailableBiddingZone_Domain",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    linked_bid_time_series: list[LinkedBidTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "Linked_BidTimeSeries",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    procured_for_market_participant: Optional[OriginMarketParticipant] = field(
        default=None,
        metadata={
            "name": "ProcuredFor_MarketParticipant",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    shared_with_market_participant: list[OriginMarketParticipant] = field(
        default_factory=list,
        metadata={
            "name": "SharedWith_MarketParticipant",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )
    exchanged_with_market_participant: list[OriginMarketParticipant] = field(
        default_factory=list,
        metadata={
            "name": "ExchangedWith_MarketParticipant",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4",
        },
    )


@dataclass
class ReserveBidMarketDocument:
    class Meta:
        name = "ReserveBid_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-7:reservebiddocument:7:4"

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
    reserve_bid_period_time_interval: Optional[EsmpDateTimeInterval] = field(
        default=None,
        metadata={
            "name": "reserveBid_Period.timeInterval",
            "type": "Element",
            "required": True,
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
    bid_time_series: list[BidTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "Bid_TimeSeries",
            "type": "Element",
        },
    )

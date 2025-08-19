from dataclasses import dataclass, field
from typing import Optional

from .urn_entsoe_eu_wgedi_codelists import (
    AllocationModeTypeList,
    AuctionTypeList,
    CategoryTypeList,
    CodingSchemeTypeList,
    ContractTypeList,
    CurrencyTypeList,
    IndicatorTypeList,
    MessageTypeList,
    ProcessTypeList,
    RoleTypeList,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0"


@dataclass
class EsmpDateTimeInterval:
    class Meta:
        name = "ESMP_DateTimeInterval"

    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        },
    )
    end: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
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
class Point:
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        },
    )
    time_series_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "timeSeries.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
            "required": True,
        },
    )
    time_series_in_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "timeSeries.in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
            "required": True,
        },
    )
    time_series_out_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "timeSeries.out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
            "required": True,
        },
    )
    time_series_currency_unit_name: Optional[CurrencyTypeList] = field(
        default=None,
        metadata={
            "name": "timeSeries.currency_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
            "required": True,
        },
    )
    time_series_auction_category: Optional[CategoryTypeList] = field(
        default=None,
        metadata={
            "name": "timeSeries.auction.category",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
        },
    )


@dataclass
class AllocationTimeSeries:
    class Meta:
        name = "Allocation_TimeSeries"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
            "required": True,
            "max_length": 20,
        },
    )
    cancelled_ts: Optional[IndicatorTypeList] = field(
        default=None,
        metadata={
            "name": "cancelledTS",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
            "max_length": 100,
        },
    )
    auction_type: Optional[AuctionTypeList] = field(
        default=None,
        metadata={
            "name": "auction.type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
            "required": True,
        },
    )
    auction_allocation_mode: Optional[AllocationModeTypeList] = field(
        default=None,
        metadata={
            "name": "auction.allocationMode",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
        },
    )
    sub_type_auction_type: Optional[AuctionTypeList] = field(
        default=None,
        metadata={
            "name": "subType_Auction.type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
        },
    )
    market_agreement_type: Optional[ContractTypeList] = field(
        default=None,
        metadata={
            "name": "marketAgreement.type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
            "required": True,
        },
    )
    time_zone_attribute_instance_component_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "timeZone_AttributeInstanceComponent.attribute",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
            "required": True,
        },
    )
    delivery_period_time_interval: Optional[EsmpDateTimeInterval] = field(
        default=None,
        metadata={
            "name": "delivery_Period.timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
            "required": True,
        },
    )
    allocation_period_time_interval: Optional[EsmpDateTimeInterval] = field(
        default=None,
        metadata={
            "name": "allocation_Period.timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
            "required": True,
        },
    )
    bidding_period_time_interval: Optional[EsmpDateTimeInterval] = field(
        default=None,
        metadata={
            "name": "bidding_Period.timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
        },
    )
    offered_capacity_provider_market_participant_m_rid: Optional[
        PartyIdString
    ] = field(
        default=None,
        metadata={
            "name": "offeredCapacityProvider_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
        },
    )
    use_of_capacity_provider_market_participant_m_rid: Optional[
        PartyIdString
    ] = field(
        default=None,
        metadata={
            "name": "useOfCapacityProvider_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
        },
    )
    already_allocated_capacity_provider_market_participant_m_rid: Optional[
        PartyIdString
    ] = field(
        default=None,
        metadata={
            "name": "alreadyAllocatedCapacityProvider_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
        },
    )
    auction_revenue_provider_market_participant_m_rid: Optional[
        PartyIdString
    ] = field(
        default=None,
        metadata={
            "name": "auctionRevenueProvider_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
        },
    )
    capacity_third_countries_provider_market_participant_m_rid: Optional[
        PartyIdString
    ] = field(
        default=None,
        metadata={
            "name": "capacityThirdCountriesProvider_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
        },
    )
    congestion_income_market_participant_m_rid: Optional[PartyIdString] = (
        field(
            default=None,
            metadata={
                "name": "congestionIncome_MarketParticipant.mRID",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
            },
        )
    )
    conducting_party_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "conductingParty_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
        },
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0",
            "min_occurs": 1,
        },
    )


@dataclass
class CapacityAllocationConfigurationMarketDocument:
    class Meta:
        name = "CapacityAllocationConfiguration_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-6a:capacityallocationconfigurationdocument:1:0"

    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "required": True,
            "max_length": 35,
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
    allocation_time_series: list[AllocationTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "Allocation_TimeSeries",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 31,
        },
    )

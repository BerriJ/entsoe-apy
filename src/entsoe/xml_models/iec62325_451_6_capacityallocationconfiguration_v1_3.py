from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    AllocationModeTypeList,
    AuctionTypeList,
    CategoryTypeList,
    ClassificationTypeList,
    CodingSchemeTypeList,
    ContractTypeList,
    CurrencyTypeList,
    IndicatorTypeList,
    MessageTypeList,
    ProcessTypeList,
    RoleTypeList,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3"


class EsmpDateTimeInterval(BaseModel):
    class Meta:
        name = "ESMP_DateTimeInterval"

    model_config = ConfigDict(defer_build=True)
    start: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )
    end: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )
    time_series_name: str = field(
        metadata={
            "name": "timeSeries.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
            "required": True,
        }
    )
    time_series_in_domain_m_rid: AreaIdString = field(
        metadata={
            "name": "timeSeries.in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
            "required": True,
        }
    )
    time_series_out_domain_m_rid: AreaIdString = field(
        metadata={
            "name": "timeSeries.out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
            "required": True,
        }
    )
    time_series_currency_unit_name: CurrencyTypeList = field(
        metadata={
            "name": "timeSeries.currency_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
            "required": True,
        }
    )
    time_series_auction_category: Optional[CategoryTypeList] = field(
        default=None,
        metadata={
            "name": "timeSeries.auction.category",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
        },
    )


class AllocationTimeSeries(BaseModel):
    class Meta:
        name = "Allocation_TimeSeries"

    model_config = ConfigDict(defer_build=True)
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
            "required": True,
            "max_length": 20,
        }
    )
    cancelled_ts: Optional[IndicatorTypeList] = field(
        default=None,
        metadata={
            "name": "cancelledTS",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
            "max_length": 100,
        },
    )
    auction_type: AuctionTypeList = field(
        metadata={
            "name": "auction.type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
            "required": True,
        }
    )
    auction_allocation_mode: Optional[AllocationModeTypeList] = field(
        default=None,
        metadata={
            "name": "auction.allocationMode",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
        },
    )
    sub_type_auction_type: Optional[AuctionTypeList] = field(
        default=None,
        metadata={
            "name": "subType_Auction.type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
        },
    )
    market_agreement_type: ContractTypeList = field(
        metadata={
            "name": "marketAgreement.type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
            "required": True,
        }
    )
    time_zone_attribute_instance_component_attribute: str = field(
        metadata={
            "name": "timeZone_AttributeInstanceComponent.attribute",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
            "required": True,
        }
    )
    delivery_period_time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "delivery_Period.timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
            "required": True,
        }
    )
    allocation_period_time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "allocation_Period.timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
            "required": True,
        }
    )
    bidding_period_time_interval: Optional[EsmpDateTimeInterval] = field(
        default=None,
        metadata={
            "name": "bidding_Period.timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
        },
    )
    offered_capacity_provider_market_participant_m_rid: Optional[
        PartyIdString
    ] = field(
        default=None,
        metadata={
            "name": "offeredCapacityProvider_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
        },
    )
    use_of_capacity_provider_market_participant_m_rid: Optional[
        PartyIdString
    ] = field(
        default=None,
        metadata={
            "name": "useOfCapacityProvider_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
        },
    )
    already_allocated_capacity_provider_market_participant_m_rid: Optional[
        PartyIdString
    ] = field(
        default=None,
        metadata={
            "name": "alreadyAllocatedCapacityProvider_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
        },
    )
    auction_revenue_provider_market_participant_m_rid: Optional[
        PartyIdString
    ] = field(
        default=None,
        metadata={
            "name": "auctionRevenueProvider_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
        },
    )
    capacity_third_countries_provider_market_participant_m_rid: Optional[
        PartyIdString
    ] = field(
        default=None,
        metadata={
            "name": "capacityThirdCountriesProvider_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
        },
    )
    congestion_income_market_participant_m_rid: Optional[PartyIdString] = (
        field(
            default=None,
            metadata={
                "name": "congestionIncome_MarketParticipant.mRID",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
            },
        )
    )
    conducting_party_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "conductingParty_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
        },
    )
    connecting_line_registered_resource_m_rid: Optional[ResourceIdString] = (
        field(
            default=None,
            metadata={
                "name": "connectingLine_RegisteredResource.mRID",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
            },
        )
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3",
            "min_occurs": 1,
        },
    )


class CapacityAllocationConfigurationMarketDocument(BaseModel):
    class Meta:
        name = "CapacityAllocationConfiguration_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-6:capacityallocationconfigurationdocument:1:3"

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
    process_classification_type: Optional[ClassificationTypeList] = field(
        default=None,
        metadata={
            "name": "process.classificationType",
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
    allocation_time_series: list[AllocationTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "Allocation_TimeSeries",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 31,
        },
    )

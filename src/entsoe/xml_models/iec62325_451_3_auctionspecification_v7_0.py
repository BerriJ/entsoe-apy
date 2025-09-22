from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDateTime, XmlDuration
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    AllocationModeTypeList,
    AuctionTypeList,
    BusinessTypeList,
    CategoryTypeList,
    CodingSchemeTypeList,
    ContractTypeList,
    CurrencyTypeList,
    CurveTypeList,
    IndicatorTypeList,
    MessageTypeList,
    PaymentTermsTypeList,
    ProcessTypeList,
    ReasonCodeTypeList,
    RightsTypeList,
    RoleTypeList,
    UnitOfMeasureTypeList,
)

__NAMESPACE__ = (
    "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0"
)


class AttributeInstanceComponent(BaseModel):
    model_config = ConfigDict(defer_build=True)
    position: int = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    attribute: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )


class EsmpDateTimeInterval(BaseModel):
    class Meta:
        name = "ESMP_DateTimeInterval"

    model_config = ConfigDict(defer_build=True)
    start: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )
    end: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )


class Point(BaseModel):
    model_config = ConfigDict(defer_build=True)
    position: int = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )
    quantity: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
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


class Reason(BaseModel):
    model_config = ConfigDict(defer_build=True)
    code: ReasonCodeTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
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


class RightsCharacteristicsAuction(BaseModel):
    class Meta:
        name = "RightsCharacteristics_Auction"

    model_config = ConfigDict(defer_build=True)
    rights: RightsTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )


class SeriesPeriod(BaseModel):
    class Meta:
        name = "Series_Period"

    model_config = ConfigDict(defer_build=True)
    time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    resolution: XmlDuration = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "min_occurs": 1,
        },
    )


class AuctionTimeSeries(BaseModel):
    class Meta:
        name = "Auction_TimeSeries"

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
            "max_length": 35,
        }
    )
    business_type: BusinessTypeList = field(
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    auction_category: CategoryTypeList = field(
        metadata={
            "name": "auction.category",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    auction_type: AuctionTypeList = field(
        metadata={
            "name": "auction.type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    auction_allocation_mode: AllocationModeTypeList = field(
        metadata={
            "name": "auction.allocationMode",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    auction_payment_terms: PaymentTermsTypeList = field(
        metadata={
            "name": "auction.paymentTerms",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    auction_cancelled: Optional[IndicatorTypeList] = field(
        default=None,
        metadata={
            "name": "auction.cancelled",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
        },
    )
    bidding_period_time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "bidding_Period.timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    in_domain_m_rid: AreaIdString = field(
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    out_domain_m_rid: AreaIdString = field(
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    market_agreement_type: ContractTypeList = field(
        metadata={
            "name": "marketAgreement.type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    delivery_period_time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "delivery_Period.timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    quantity_measure_unit_name: UnitOfMeasureTypeList = field(
        metadata={
            "name": "quantity_Measure_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    price_measure_unit_name: UnitOfMeasureTypeList = field(
        metadata={
            "name": "price_Measure_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    currency_unit_name: CurrencyTypeList = field(
        metadata={
            "name": "currency_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    notification_market_agreement_created_date_time: XmlDateTime = field(
        metadata={
            "name": "notification_MarketAgreement.createdDateTime",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    contestation_market_agreement_created_date_time: XmlDateTime = field(
        metadata={
            "name": "contestation_MarketAgreement.createdDateTime",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    publication_market_agreement_created_date_time: XmlDateTime = field(
        metadata={
            "name": "publication_MarketAgreement.createdDateTime",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    resale_market_agreement_created_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "resale_MarketAgreement.createdDateTime",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
        },
    )
    curve_type: CurveTypeList = field(
        metadata={
            "name": "curveType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
            "required": True,
        }
    )
    period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
        },
    )
    auction_description_attribute_instance_component: list[
        AttributeInstanceComponent
    ] = field(
        default_factory=list,
        metadata={
            "name": "AuctionDescription_AttributeInstanceComponent",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
        },
    )
    rights_characteristics_auction: list[RightsCharacteristicsAuction] = field(
        default_factory=list,
        metadata={
            "name": "RightsCharacteristics_Auction",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0",
        },
    )


class CapacityAuctionSpecificationMarketDocument(BaseModel):
    class Meta:
        name = "CapacityAuctionSpecification_MarketDocument"
        namespace = (
            "urn:iec62325.351:tc57wg16:451-3:capacityspecificationdocument:7:0"
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
    receiver_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "receiver_MarketParticipant.mRID",
            "type": "Element",
        },
    )
    receiver_market_participant_market_role_type: Optional[RoleTypeList] = (
        field(
            default=None,
            metadata={
                "name": "receiver_MarketParticipant.marketRole.type",
                "type": "Element",
            },
        )
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
    domain_m_rid: AreaIdString = field(
        metadata={
            "name": "domain.mRID",
            "type": "Element",
            "required": True,
        }
    )
    auction_time_series: list[AuctionTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "Auction_TimeSeries",
            "type": "Element",
            "min_occurs": 1,
        },
    )

from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDateTime, XmlDuration
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    AssetTypeList,
    BusinessTypeList,
    CodingSchemeTypeList,
    ContractTypeList,
    CurrencyTypeList,
    CurveTypeList,
    DirectionTypeList,
    IndicatorTypeList,
    MarketProductTypeList,
    MessageTypeList,
    PriceCategoryTypeList,
    PriceDirectionTypeList,
    ProcessTypeList,
    RoleTypeList,
    StatusTypeList,
    UnitOfMeasureTypeList,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2"


class EsmpDateTimeInterval(BaseModel):
    class Meta:
        name = "ESMP_DateTimeInterval"

    model_config = ConfigDict(defer_build=True)
    start: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )
    end: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )


class ActionStatus(BaseModel):
    class Meta:
        name = "Action_Status"

    model_config = ConfigDict(defer_build=True)
    value: StatusTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
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


class FinancialPrice(BaseModel):
    class Meta:
        name = "Financial_Price"

    model_config = ConfigDict(defer_build=True)
    amount: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
            "required": True,
            "total_digits": 17,
        }
    )
    direction: PriceDirectionTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )
    quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
        },
    )
    secondary_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "secondaryQuantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
        },
    )
    unavailable_quantity_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "unavailable_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
        },
    )
    activation_price_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "activation_Price.amount",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
            "total_digits": 17,
        },
    )
    procurement_price_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "procurement_Price.amount",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
            "total_digits": 17,
        },
    )
    min_price_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "min_Price.amount",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
            "total_digits": 17,
        },
    )
    max_price_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "max_Price.amount",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
            "total_digits": 17,
        },
    )
    imbalance_price_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "imbalance_Price.amount",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
            "total_digits": 17,
        },
    )
    imbalance_price_category: Optional[PriceCategoryTypeList] = field(
        default=None,
        metadata={
            "name": "imbalance_Price.category",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
        },
    )
    flow_direction_direction: Optional[DirectionTypeList] = field(
        default=None,
        metadata={
            "name": "flowDirection.direction",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
        },
    )
    financial_price: list[FinancialPrice] = field(
        default_factory=list,
        metadata={
            "name": "Financial_Price",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
            "required": True,
        }
    )
    resolution: XmlDuration = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
            "required": True,
        }
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
            "min_occurs": 1,
        },
    )


class TimeSeries(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
            "required": True,
            "max_length": 60,
        }
    )
    business_type: BusinessTypeList = field(
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
            "required": True,
        }
    )
    acquiring_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "acquiring_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
        },
    )
    connecting_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "connecting_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
        },
    )
    type_market_agreement_type: Optional[ContractTypeList] = field(
        default=None,
        metadata={
            "name": "type_MarketAgreement.type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
        },
    )
    standard_market_product_market_product_type: Optional[
        MarketProductTypeList
    ] = field(
        default=None,
        metadata={
            "name": "standard_MarketProduct.marketProductType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
        },
    )
    original_market_product_market_product_type: Optional[
        MarketProductTypeList
    ] = field(
        default=None,
        metadata={
            "name": "original_MarketProduct.marketProductType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
        },
    )
    mkt_psrtype_psr_type: Optional[AssetTypeList] = field(
        default=None,
        metadata={
            "name": "mktPSRType.psrType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
        },
    )
    flow_direction_direction: Optional[DirectionTypeList] = field(
        default=None,
        metadata={
            "name": "flowDirection.direction",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
        },
    )
    currency_unit_name: Optional[CurrencyTypeList] = field(
        default=None,
        metadata={
            "name": "currency_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
        },
    )
    quantity_measure_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "quantity_Measure_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
        },
    )
    price_measure_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "price_Measure_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
        },
    )
    curve_type: Optional[CurveTypeList] = field(
        default=None,
        metadata={
            "name": "curveType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
        },
    )
    cancelled_ts: Optional[IndicatorTypeList] = field(
        default=None,
        metadata={
            "name": "cancelledTS",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
        },
    )
    auction_m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "auction.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
            "max_length": 60,
        },
    )
    period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2",
        },
    )


class BalancingMarketDocument(BaseModel):
    class Meta:
        name = "Balancing_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-6:balancingdocument:4:2"

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
    doc_status: Optional[ActionStatus] = field(
        default=None,
        metadata={
            "name": "docStatus",
            "type": "Element",
        },
    )
    area_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "area_Domain.mRID",
            "type": "Element",
        },
    )
    allocation_decision_date_and_or_time_date_time: Optional[XmlDateTime] = (
        field(
            default=None,
            metadata={
                "name": "allocationDecision_DateAndOrTime.dateTime",
                "type": "Element",
            },
        )
    )
    period_time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "period.timeInterval",
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

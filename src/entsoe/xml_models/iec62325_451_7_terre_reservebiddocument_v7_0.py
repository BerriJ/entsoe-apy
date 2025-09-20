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
    DirectionTypeList,
    IndicatorTypeList,
    MessageTypeList,
    ProcessTypeList,
    ReasonCodeTypeList,
    RoleTypeList,
    StatusTypeList,
    UnitOfMeasureTypeList,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:"


class EsmpDateTimeInterval(BaseModel):
    class Meta:
        name = "ESMP_DateTimeInterval"

    model_config = ConfigDict(defer_build=True)
    start: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )
    end: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )


class Point(BaseModel):
    model_config = ConfigDict(defer_build=True)
    position: int = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )
    quantity_quantity: Decimal = field(
        metadata={
            "name": "quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "required": True,
        }
    )
    minimum_quantity_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "minimum_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
        },
    )
    price_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "price.amount",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "total_digits": 17,
        },
    )
    energy_price_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "energy_Price.amount",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "total_digits": 17,
        },
    )


class ActionStatus(BaseModel):
    class Meta:
        name = "Action_Status"

    model_config = ConfigDict(defer_build=True)
    value: StatusTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "required": True,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
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


class SeriesPeriod(BaseModel):
    class Meta:
        name = "Series_Period"

    model_config = ConfigDict(defer_build=True)
    time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "required": True,
        }
    )
    resolution: XmlDuration = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "required": True,
        }
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "min_occurs": 1,
        },
    )


class MbaDomain(BaseModel):
    class Meta:
        name = "MBA_Domain"

    model_config = ConfigDict(defer_build=True)
    m_rid: AreaIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "required": True,
        }
    )


class BidTimeSeries(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "required": True,
            "max_length": 35,
        }
    )
    auction_m_rid: str = field(
        metadata={
            "name": "auction.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "required": True,
            "max_length": 35,
        }
    )
    business_type: BusinessTypeList = field(
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "required": True,
        }
    )
    acquiring_domain_m_rid: AreaIdString = field(
        metadata={
            "name": "acquiring_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "required": True,
        }
    )
    connecting_domain_m_rid: AreaIdString = field(
        metadata={
            "name": "connecting_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "required": True,
        }
    )
    quantity_measure_unit_name: UnitOfMeasureTypeList = field(
        metadata={
            "name": "quantity_Measure_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "required": True,
        }
    )
    currency_unit_name: Optional[CurrencyTypeList] = field(
        default=None,
        metadata={
            "name": "currency_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
        },
    )
    price_measure_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "price_Measure_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
        },
    )
    divisible: IndicatorTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "required": True,
        }
    )
    linked_bids_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "linkedBidsIdentification",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "max_length": 35,
        },
    )
    exclusive_bids_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "exclusiveBidsIdentification",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "max_length": 35,
        },
    )
    block_bid: IndicatorTypeList = field(
        metadata={
            "name": "blockBid",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "required": True,
        }
    )
    status: Optional[ActionStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
        },
    )
    priority: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
        },
    )
    registered_resource_m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "registeredResource.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
        },
    )
    flow_direction_direction: DirectionTypeList = field(
        metadata={
            "name": "flowDirection.direction",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "required": True,
        }
    )
    step_increment_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "stepIncrementQuantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
        },
    )
    energy_price_measure_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "energyPrice_Measure_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
        },
    )
    market_agreement_type: Optional[ContractTypeList] = field(
        default=None,
        metadata={
            "name": "marketAgreement.type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
        },
    )
    market_agreement_m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "marketAgreement.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "max_length": 35,
        },
    )
    activation_constraint_duration_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "activation_ConstraintDuration.duration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
        },
    )
    resting_constraint_duration_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "resting_ConstraintDuration.duration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
        },
    )
    minimum_constraint_duration_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "minimum_ConstraintDuration.duration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
        },
    )
    maximum_constraint_duration_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "maximum_ConstraintDuration.duration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
        },
    )
    period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
            "min_occurs": 1,
        },
    )
    available_mba_domain: list[MbaDomain] = field(
        default_factory=list,
        metadata={
            "name": "AvailableMBA_Domain",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:",
        },
    )


class ReserveBidMarketDocument(BaseModel):
    class Meta:
        name = "ReserveBid_MarketDocument"
        namespace = (
            "urn:iec62325.351:tc57wg16:451-7_TERRE:reservebiddocument:7:"
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
    subject_market_participant_m_rid: PartyIdString = field(
        metadata={
            "name": "subject_MarketParticipant.mRID",
            "type": "Element",
            "required": True,
        }
    )
    subject_market_participant_market_role_type: RoleTypeList = field(
        metadata={
            "name": "subject_MarketParticipant.marketRole.type",
            "type": "Element",
            "required": True,
        }
    )
    bid_time_series: list[BidTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "Bid_TimeSeries",
            "type": "Element",
        },
    )

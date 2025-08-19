from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .urn_entsoe_eu_wgedi_codelists import (
    BusinessTypeList,
    CodingSchemeTypeList,
    CurrencyTypeList,
    DirectionTypeList,
    MessageTypeList,
    ProcessTypeList,
    ReasonCodeTypeList,
    RoleTypeList,
    StatusTypeList,
    UnitOfMeasureTypeList,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0"


@dataclass
class EsmpDateTimeInterval:
    class Meta:
        name = "ESMP_DateTimeInterval"

    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        },
    )
    end: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        },
    )
    quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "required": True,
        },
    )
    price_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "price.amount",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "total_digits": 17,
        },
    )
    energy_price_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "energy_Price.amount",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "total_digits": 17,
        },
    )
    activated_quantity_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "activated_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "required": True,
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
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
class SeriesPeriod:
    class Meta:
        name = "Series_Period"

    time_interval: Optional[EsmpDateTimeInterval] = field(
        default=None,
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "required": True,
        },
    )
    resolution: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "required": True,
        },
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "min_occurs": 1,
        },
    )


@dataclass
class MolTimeSeries:
    class Meta:
        name = "MOL_TimeSeries"

    market_agreement_m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "marketAgreement.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "required": True,
            "max_length": 35,
        },
    )
    market_agreement_created_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "marketAgreement.createdDateTime",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)",
        },
    )
    order_number_attribute_instance_component_position: Optional[int] = field(
        default=None,
        metadata={
            "name": "orderNumber_AttributeInstanceComponent.position",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "min_inclusive": 1,
            "max_inclusive": 999999,
        },
    )
    resource_provider_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "resourceProvider_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "required": True,
        },
    )
    registered_resource_m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "registeredResource.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
        },
    )
    acquiring_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "acquiring_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "required": True,
        },
    )
    connecting_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "connecting_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "required": True,
        },
    )
    auction_m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "auction.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "required": True,
            "max_length": 35,
        },
    )
    business_type: Optional[BusinessTypeList] = field(
        default=None,
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "required": True,
        },
    )
    bid_period_time_interval: Optional[EsmpDateTimeInterval] = field(
        default=None,
        metadata={
            "name": "bid_Period.timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "required": True,
        },
    )
    quantity_measurement_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "quantityMeasurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "required": True,
        },
    )
    currency_unit_name: Optional[CurrencyTypeList] = field(
        default=None,
        metadata={
            "name": "currency_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
        },
    )
    price_measurement_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "priceMeasurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
        },
    )
    energy_price_measurement_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "energyPriceMeasurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
        },
    )
    flow_direction_direction: Optional[DirectionTypeList] = field(
        default=None,
        metadata={
            "name": "flowDirection.direction",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "required": True,
        },
    )
    minimum_activation_quantity_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "minimumActivation_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
        },
    )
    step_increment_quantity_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "stepIncrement_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
        },
    )
    market_object_status_status: Optional[StatusTypeList] = field(
        default=None,
        metadata={
            "name": "marketObjectStatus.status",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "required": True,
        },
    )
    period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
            "min_occurs": 1,
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0",
        },
    )


@dataclass
class MeritOrderListMarketDocument:
    class Meta:
        name = "MeritOrderList_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-7:moldocument:6:0"

    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "required": True,
            "max_length": 35,
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
    receiver_market_participant_market_role_type: Optional[RoleTypeList] = field(
        default=None,
        metadata={
            "name": "receiver_MarketParticipant.marketRole.type",
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
    valid_time_period_time_interval: Optional[EsmpDateTimeInterval] = field(
        default=None,
        metadata={
            "name": "valid_Time_Period.timeInterval",
            "type": "Element",
            "required": True,
        },
    )
    domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "domain.mRID",
            "type": "Element",
        },
    )
    mol_time_series: list[MolTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "MOL_TimeSeries",
            "type": "Element",
        },
    )

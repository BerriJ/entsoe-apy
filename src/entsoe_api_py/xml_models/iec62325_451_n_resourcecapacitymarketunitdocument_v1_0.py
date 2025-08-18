from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime, XmlDuration

from entsoe_api_py.xml_models.urn_entsoe_eu_wgedi_codelists import (
    AnalogTypeList,
    AssetTypeList,
    BusinessTypeList,
    CodingSchemeTypeList,
    CoordinateSystemTypeList,
    CurveTypeList,
    EnergyProductTypeList,
    MarketProductTypeList,
    MessageTypeList,
    ProcessTypeList,
    RoleTypeList,
    StatusTypeList,
    UnitOfMeasureTypeList,
    UnitSymbol,
)

__NAMESPACE__ = (
    "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0"
)


@dataclass
class EsmpDateTimeInterval:
    class Meta:
        name = "ESMP_DateTimeInterval"

    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        },
    )
    end: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        },
    )


@dataclass
class ElectronicAddress:
    email1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
            "max_length": 70,
        },
    )


@dataclass
class Point:
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        },
    )
    quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
        },
    )


@dataclass
class StreetDetail:
    address_general: Optional[str] = field(
        default=None,
        metadata={
            "name": "addressGeneral",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "max_length": 70,
        },
    )
    address_general2: Optional[str] = field(
        default=None,
        metadata={
            "name": "addressGeneral2",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "max_length": 70,
        },
    )
    address_general3: Optional[str] = field(
        default=None,
        metadata={
            "name": "addressGeneral3",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "max_length": 70,
        },
    )
    floor_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "floorIdentification",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
        },
    )


@dataclass
class TelephoneNumber:
    itu_phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "ituPhone",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
            "max_length": 15,
        },
    )


@dataclass
class TownDetail:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
            "max_length": 35,
        },
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
            "length": 2,
            "pattern": r"[A-Z]*",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
        },
    )


@dataclass
class Analog:
    measurement_type: Optional[AnalogTypeList] = field(
        default=None,
        metadata={
            "name": "measurementType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
        },
    )
    unit_symbol: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "unitSymbol",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
        },
    )
    analog_values_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "analogValues.value",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
            "pattern": r"([0-9]*\.?[0-9]*)",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
        },
    )
    resolution: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
        },
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "min_occurs": 1,
        },
    )


@dataclass
class StreetAddress:
    street_detail: Optional[StreetDetail] = field(
        default=None,
        metadata={
            "name": "streetDetail",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
        },
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "postalCode",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
            "max_length": 10,
        },
    )
    town_detail: Optional[TownDetail] = field(
        default=None,
        metadata={
            "name": "townDetail",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
        },
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
        },
    )


@dataclass
class MeteringPointAggregateNode:
    class Meta:
        name = "MeteringPoint_AggregateNode"

    m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
        },
    )


@dataclass
class ResourceCapacityMarketUnitRegisteredResource:
    class Meta:
        name = "ResourceCapacityMarketUnit_RegisteredResource"

    m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
        },
    )
    resource_capacity_maximum_capacity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "resourceCapacity.maximumCapacity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    resource_capacity_unit_symbol: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "resourceCapacity.unitSymbol",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    metering_point_aggregate_node: list[MeteringPointAggregateNode] = field(
        default_factory=list,
        metadata={
            "name": "MeteringPoint_AggregateNode",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )


@dataclass
class UnitRegisteredResource:
    class Meta:
        name = "Unit_RegisteredResource"

    m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
        },
    )
    resource_capacity_maximum_capacity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "resourceCapacity.maximumCapacity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    resource_capacity_unit_symbol: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "resourceCapacity.unitSymbol",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    p_srtype_psr_type: Optional[AssetTypeList] = field(
        default=None,
        metadata={
            "name": "pSRType.psrType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    street_location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "street_Location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    street_number_location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "streetNumber_Location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    city_location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "city_Location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    postal_code_location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "postalCode_Location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    country_location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "country_Location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    g_ps_location_g_ps_coordinate_system_m_rid: Optional[
        CoordinateSystemTypeList
    ] = field(
        default=None,
        metadata={
            "name": "gPS_Location.gPS_CoordinateSystem.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    g_ps_location_g_ps_position_points_x_position: Optional[str] = field(
        default=None,
        metadata={
            "name": "gPS_Location.gPS_PositionPoints.xPosition",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    g_ps_location_g_ps_position_points_y_position: Optional[str] = field(
        default=None,
        metadata={
            "name": "gPS_Location.gPS_PositionPoints.yPosition",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    g_ps_location_g_ps_position_points_z_position: Optional[str] = field(
        default=None,
        metadata={
            "name": "gPS_Location.gPS_PositionPoints.zPosition",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    measurements: list[Analog] = field(
        default_factory=list,
        metadata={
            "name": "Measurements",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    metering_point_aggregate_node: list[MeteringPointAggregateNode] = field(
        default_factory=list,
        metadata={
            "name": "MeteringPoint_AggregateNode",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )


@dataclass
class TimeSeries:
    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
            "max_length": 60,
        },
    )
    business_type: Optional[BusinessTypeList] = field(
        default=None,
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
        },
    )
    product: Optional[EnergyProductTypeList] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
        },
    )
    resource_capacity_market_unit_registered_resource: Optional[
        ResourceCapacityMarketUnitRegisteredResource
    ] = field(
        default=None,
        metadata={
            "name": "ResourceCapacityMarketUnit_RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            "required": True,
        },
    )
    curve_type: Optional[CurveTypeList] = field(
        default=None,
        metadata={
            "name": "curveType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    resource_provider_market_participant_m_rid: Optional[PartyIdString] = (
        field(
            default=None,
            metadata={
                "name": "resourceProvider_MarketParticipant.mRID",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            },
        )
    )
    resource_provider_market_participant_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "resourceProvider_MarketParticipant.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    resource_provider_market_participant_street_address: Optional[
        StreetAddress
    ] = field(
        default=None,
        metadata={
            "name": "resourceProvider_MarketParticipant.streetAddress",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    resource_provider_market_participant_phone1: Optional[TelephoneNumber] = (
        field(
            default=None,
            metadata={
                "name": "resourceProvider_MarketParticipant.phone1",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            },
        )
    )
    resource_provider_market_participant_electronic_address: Optional[
        ElectronicAddress
    ] = field(
        default=None,
        metadata={
            "name": "resourceProvider_MarketParticipant.electronicAddress",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    network_operator_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "networkOperator_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    resource_capacity_mechanism_operator_market_participant_m_rid: Optional[
        PartyIdString
    ] = field(
        default=None,
        metadata={
            "name": "resourceCapacityMechanismOperator_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    member_state_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "memberState_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    last_verification_date_and_or_time_date_time: Optional[XmlDateTime] = (
        field(
            default=None,
            metadata={
                "name": "lastVerification_DateAndOrTime.dateTime",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
            },
        )
    )
    market_participation_market_object_status_status: Optional[
        StatusTypeList
    ] = field(
        default=None,
        metadata={
            "name": "marketParticipation_MarketObjectStatus.status",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    capacity_mechanism_market_product_market_product_type: Optional[
        MarketProductTypeList
    ] = field(
        default=None,
        metadata={
            "name": "capacityMechanism_MarketProduct.marketProductType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    measurement_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "measurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    unit_registered_resource: list[UnitRegisteredResource] = field(
        default_factory=list,
        metadata={
            "name": "Unit_RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    elegibility_period: list[TimePeriod] = field(
        default_factory=list,
        metadata={
            "name": "Elegibility_Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )
    period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0",
        },
    )


@dataclass
class ResourceCapacityMarketUnitMarketDocument:
    class Meta:
        name = "ResourceCapacityMarketUnit_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:0"

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
    time_period: Optional[TimePeriod] = field(
        default=None,
        metadata={
            "name": "Time_Period",
            "type": "Element",
            "required": True,
        },
    )
    doc_status: Optional[ActionStatus] = field(
        default=None,
        metadata={
            "name": "docStatus",
            "type": "Element",
        },
    )
    time_series: list[TimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "TimeSeries",
            "type": "Element",
        },
    )

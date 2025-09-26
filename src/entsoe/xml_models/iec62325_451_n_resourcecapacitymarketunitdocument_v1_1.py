from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDateTime, XmlDuration
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    AnalogTypeList,
    AssetTypeList,
    BusinessTypeList,
    CodingSchemeTypeList,
    CoordinateSystemTypeList,
    CurveTypeList,
    EnergyProductTypeList,
    FuelTypeList,
    MarketProductTypeList,
    MessageTypeList,
    ProcessTypeList,
    RoleTypeList,
    StatusTypeList,
    UnitOfMeasureTypeList,
    UnitSymbol,
)

__NAMESPACE__ = (
    "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1"
)


class EsmpDateTimeInterval(BaseModel):
    class Meta:
        name = "ESMP_DateTimeInterval"

    model_config = ConfigDict(defer_build=True)
    start: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )
    end: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )


class ElectronicAddress(BaseModel):
    model_config = ConfigDict(defer_build=True)
    email1: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
            "max_length": 70,
        }
    )


class Point(BaseModel):
    model_config = ConfigDict(defer_build=True)
    position: int = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )
    quantity: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
        }
    )


class StreetDetail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    address_general: Optional[str] = field(
        default=None,
        metadata={
            "name": "addressGeneral",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "max_length": 70,
        },
    )
    address_general2: Optional[str] = field(
        default=None,
        metadata={
            "name": "addressGeneral2",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "max_length": 70,
        },
    )
    address_general3: Optional[str] = field(
        default=None,
        metadata={
            "name": "addressGeneral3",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "max_length": 70,
        },
    )
    floor_identification: str = field(
        metadata={
            "name": "floorIdentification",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
        }
    )


class TelephoneNumber(BaseModel):
    model_config = ConfigDict(defer_build=True)
    itu_phone: str = field(
        metadata={
            "name": "ituPhone",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
            "max_length": 15,
        }
    )


class TownDetail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
            "max_length": 35,
        }
    )
    country: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
            "length": 2,
            "pattern": r"[A-Z]*",
        }
    )


class ActionStatus(BaseModel):
    class Meta:
        name = "Action_Status"

    model_config = ConfigDict(defer_build=True)
    value: StatusTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
        }
    )


class Analog(BaseModel):
    model_config = ConfigDict(defer_build=True)
    measurement_type: AnalogTypeList = field(
        metadata={
            "name": "measurementType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
        }
    )
    unit_symbol: UnitSymbol = field(
        metadata={
            "name": "unitSymbol",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
        }
    )
    analog_values_value: str = field(
        metadata={
            "name": "analogValues.value",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
            "pattern": r"([0-9]*\.?[0-9]*)",
        }
    )


class Fuel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    fuel: FuelTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
        }
    )


class MeasurementPointIdString(BaseModel):
    class Meta:
        name = "MeasurementPointID_String"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 35,
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


class SeriesPeriod(BaseModel):
    class Meta:
        name = "Series_Period"

    model_config = ConfigDict(defer_build=True)
    time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
        }
    )
    resolution: XmlDuration = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
        }
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "min_occurs": 1,
        },
    )


class StreetAddress(BaseModel):
    model_config = ConfigDict(defer_build=True)
    street_detail: StreetDetail = field(
        metadata={
            "name": "streetDetail",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
        }
    )
    postal_code: str = field(
        metadata={
            "name": "postalCode",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
            "max_length": 10,
        }
    )
    town_detail: TownDetail = field(
        metadata={
            "name": "townDetail",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )


class TimePeriod(BaseModel):
    class Meta:
        name = "Time_Period"

    model_config = ConfigDict(defer_build=True)
    time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
        }
    )


class MarketEvaluationPoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: MeasurementPointIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
        }
    )


class ResourceCapacityMarketUnitRegisteredResource(BaseModel):
    class Meta:
        name = "ResourceCapacityMarketUnit_RegisteredResource"

    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
        }
    )
    resource_capacity_maximum_capacity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "resourceCapacity.maximumCapacity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    resource_capacity_unit_symbol: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "resourceCapacity.unitSymbol",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    market_evaluation_point: list[MarketEvaluationPoint] = field(
        default_factory=list,
        metadata={
            "name": "MarketEvaluationPoint",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )


class UnitRegisteredResource(BaseModel):
    class Meta:
        name = "Unit_RegisteredResource"

    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
        }
    )
    resource_capacity_maximum_capacity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "resourceCapacity.maximumCapacity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    resource_capacity_unit_symbol: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "resourceCapacity.unitSymbol",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    street_location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "street_Location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    street_number_location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "streetNumber_Location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    city_location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "city_Location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    postal_code_location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "postalCode_Location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    country_location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "country_Location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    g_ps_location_g_ps_coordinate_system_m_rid: Optional[
        CoordinateSystemTypeList
    ] = field(
        default=None,
        metadata={
            "name": "gPS_Location.gPS_CoordinateSystem.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    g_ps_location_g_ps_position_points_x_position: Optional[str] = field(
        default=None,
        metadata={
            "name": "gPS_Location.gPS_PositionPoints.xPosition",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    g_ps_location_g_ps_position_points_y_position: Optional[str] = field(
        default=None,
        metadata={
            "name": "gPS_Location.gPS_PositionPoints.yPosition",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    g_ps_location_g_ps_position_points_z_position: Optional[str] = field(
        default=None,
        metadata={
            "name": "gPS_Location.gPS_PositionPoints.zPosition",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    technology_psrtype_psr_type: Optional[AssetTypeList] = field(
        default=None,
        metadata={
            "name": "technology_PSRType.psrType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    fuel: list[Fuel] = field(
        default_factory=list,
        metadata={
            "name": "Fuel",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    measurements: list[Analog] = field(
        default_factory=list,
        metadata={
            "name": "Measurements",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    market_evaluation_point: list[MarketEvaluationPoint] = field(
        default_factory=list,
        metadata={
            "name": "MarketEvaluationPoint",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )


class TimeSeries(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
            "max_length": 60,
        }
    )
    business_type: BusinessTypeList = field(
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
        }
    )
    product: EnergyProductTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
        }
    )
    resource_capacity_market_unit_registered_resource: ResourceCapacityMarketUnitRegisteredResource = field(
        metadata={
            "name": "ResourceCapacityMarketUnit_RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            "required": True,
        }
    )
    curve_type: Optional[CurveTypeList] = field(
        default=None,
        metadata={
            "name": "curveType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    resource_provider_market_participant_m_rid: Optional[PartyIdString] = (
        field(
            default=None,
            metadata={
                "name": "resourceProvider_MarketParticipant.mRID",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            },
        )
    )
    resource_provider_market_participant_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "resourceProvider_MarketParticipant.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    resource_provider_market_participant_street_address: Optional[
        StreetAddress
    ] = field(
        default=None,
        metadata={
            "name": "resourceProvider_MarketParticipant.streetAddress",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    resource_provider_market_participant_phone1: Optional[TelephoneNumber] = (
        field(
            default=None,
            metadata={
                "name": "resourceProvider_MarketParticipant.phone1",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    network_operator_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "networkOperator_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    resource_capacity_mechanism_operator_market_participant_m_rid: Optional[
        PartyIdString
    ] = field(
        default=None,
        metadata={
            "name": "resourceCapacityMechanismOperator_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    member_state_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "memberState_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    initial_registration_date_and_or_time_date_time: Optional[XmlDateTime] = (
        field(
            default=None,
            metadata={
                "name": "initialRegistration_DateAndOrTime.dateTime",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            },
        )
    )
    registration_date_and_or_time_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "registration_DateAndOrTime.dateTime",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    last_verification_date_and_or_time_date_time: Optional[XmlDateTime] = (
        field(
            default=None,
            metadata={
                "name": "lastVerification_DateAndOrTime.dateTime",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
            },
        )
    )
    primary_market_participation_market_object_status_status: Optional[
        StatusTypeList
    ] = field(
        default=None,
        metadata={
            "name": "primaryMarketParticipation_MarketObjectStatus.status",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    secondary_market_participation_market_object_status_status: Optional[
        StatusTypeList
    ] = field(
        default=None,
        metadata={
            "name": "secondaryMarketParticipation_MarketObjectStatus.status",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    capacity_mechanism_market_product_market_product_type: Optional[
        MarketProductTypeList
    ] = field(
        default=None,
        metadata={
            "name": "capacityMechanism_MarketProduct.marketProductType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    clearance_number_names_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "clearanceNumber_Names.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    measurement_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "measurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    unit_registered_resource: list[UnitRegisteredResource] = field(
        default_factory=list,
        metadata={
            "name": "Unit_RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    elegibility_period: list[TimePeriod] = field(
        default_factory=list,
        metadata={
            "name": "Elegibility_Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )
    period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1",
        },
    )


class ResourceCapacityMarketUnitMarketDocument(BaseModel):
    class Meta:
        name = "ResourceCapacityMarketUnit_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-n:resourcecapacitymarketunitdocument:1:1"

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
    time_period: TimePeriod = field(
        metadata={
            "name": "Time_Period",
            "type": "Element",
            "required": True,
        }
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

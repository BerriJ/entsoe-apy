from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from .urn_entsoe_eu_wgedi_codelists import (
    AnalogTypeList,
    AssetTypeList,
    BusinessTypeList,
    CodingSchemeTypeList,
    MessageTypeList,
    ProcessTypeList,
    RoleTypeList,
    UnitSymbol,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3"


@dataclass
class Analog:
    measurement_type: Optional[AnalogTypeList] = field(
        default=None,
        metadata={
            "name": "measurementType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "required": True,
        },
    )
    unit_symbol: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "unitSymbol",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "required": True,
        },
    )
    analog_values_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "analogValues.value",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "pattern": r"([0-9]*\.?[0-9]*)",
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
class EsmpActivePower:
    class Meta:
        name = "ESMP_ActivePower"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"([0-9]*\.?[0-9]*)",
        },
    )
    unit: UnitSymbol = field(
        init=False,
        default=UnitSymbol.MAW,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EsmpVoltage:
    class Meta:
        name = "ESMP_Voltage"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"([0-9]*\.?[0-9]*)",
        },
    )
    unit: UnitSymbol = field(
        init=False,
        default=UnitSymbol.KVT,
        metadata={
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
class ControlAreaDomain:
    class Meta:
        name = "ControlArea_Domain"

    m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "required": True,
        },
    )


@dataclass
class MktGeneratingUnit:
    m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "required": True,
        },
    )
    nominal_p: Optional[EsmpActivePower] = field(
        default=None,
        metadata={
            "name": "nominalP",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "required": True,
        },
    )
    generating_unit_location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "generatingUnit_Location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "required": True,
        },
    )
    generating_unit_psrtype_psr_type: Optional[AssetTypeList] = field(
        default=None,
        metadata={
            "name": "generatingUnit_PSRType.psrType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "required": True,
        },
    )


@dataclass
class ProviderMarketParticipant:
    class Meta:
        name = "Provider_MarketParticipant"

    m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "required": True,
        },
    )


@dataclass
class RegisteredResource:
    m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "required": True,
        },
    )
    location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "required": True,
        },
    )
    measurements: list[Analog] = field(
        default_factory=list,
        metadata={
            "name": "Measurements",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
        },
    )


@dataclass
class MktPsrtype:
    class Meta:
        name = "MktPSRType"

    psr_type: Optional[AssetTypeList] = field(
        default=None,
        metadata={
            "name": "psrType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "required": True,
        },
    )
    production_power_system_resources_high_voltage_limit: Optional[
        EsmpVoltage
    ] = field(
        default=None,
        metadata={
            "name": "production_PowerSystemResources.highVoltageLimit",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
        },
    )
    nominal_ip_power_system_resources_nominal_p: Optional[EsmpActivePower] = (
        field(
            default=None,
            metadata={
                "name": "nominalIP_PowerSystemResources.nominalP",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            },
        )
    )
    generating_unit_power_system_resources: list[MktGeneratingUnit] = field(
        default_factory=list,
        metadata={
            "name": "GeneratingUnit_PowerSystemResources",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
        },
    )


@dataclass
class TimeSeries:
    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "required": True,
            "max_length": 60,
        },
    )
    business_type: Optional[BusinessTypeList] = field(
        default=None,
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "required": True,
        },
    )
    implementation_date_and_or_time_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "implementation_DateAndOrTime.date",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "required": True,
        },
    )
    bidding_zone_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "biddingZone_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
        },
    )
    registered_resource: Optional[RegisteredResource] = field(
        default=None,
        metadata={
            "name": "RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "required": True,
        },
    )
    control_area_domain: list[ControlAreaDomain] = field(
        default_factory=list,
        metadata={
            "name": "ControlArea_Domain",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "min_occurs": 1,
        },
    )
    provider_market_participant: list[ProviderMarketParticipant] = field(
        default_factory=list,
        metadata={
            "name": "Provider_MarketParticipant",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "min_occurs": 1,
        },
    )
    mkt_psrtype: Optional[MktPsrtype] = field(
        default=None,
        metadata={
            "name": "MktPSRType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3",
            "required": True,
        },
    )


@dataclass
class ConfigurationMarketDocument:
    class Meta:
        name = "Configuration_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:3"

    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "required": True,
            "max_length": 60,
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
    time_series: list[TimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "TimeSeries",
            "type": "Element",
        },
    )

from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDate
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    AssetTypeList,
    BusinessTypeList,
    CodingSchemeTypeList,
    MessageTypeList,
    ProcessTypeList,
    RoleTypeList,
    UnitSymbol,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0"


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


class EsmpActivePower(BaseModel):
    class Meta:
        name = "ESMP_ActivePower"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"([0-9]+((\.[0-9])*))",
        },
    )
    unit: UnitSymbol = field(
        const=True,
        default=UnitSymbol.MAW,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


class EsmpVoltage(BaseModel):
    class Meta:
        name = "ESMP_Voltage"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"([0-9]+((\.[0-9])*))",
        },
    )
    unit: UnitSymbol = field(
        const=True,
        default=UnitSymbol.KVT,
        metadata={
            "type": "Attribute",
            "required": True,
        },
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


class ControlAreaDomain(BaseModel):
    class Meta:
        name = "ControlArea_Domain"

    model_config = ConfigDict(defer_build=True)
    m_rid: AreaIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
            "required": True,
        }
    )


class MktGeneratingUnit(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
            "required": True,
        }
    )
    nominal_p: EsmpActivePower = field(
        metadata={
            "name": "nominalP",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
            "required": True,
        }
    )
    generating_unit_psrtype_psr_type: AssetTypeList = field(
        metadata={
            "name": "generatingUnit_PSRType.psrType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
            "required": True,
        }
    )
    generating_unit_location_name: str = field(
        metadata={
            "name": "generatingUnit_Location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
            "required": True,
        }
    )


class ProviderMarketParticipant(BaseModel):
    class Meta:
        name = "Provider_MarketParticipant"

    model_config = ConfigDict(defer_build=True)
    m_rid: PartyIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
            "required": True,
        }
    )


class MktPsrtype(BaseModel):
    class Meta:
        name = "MktPSRType"

    model_config = ConfigDict(defer_build=True)
    psr_type: AssetTypeList = field(
        metadata={
            "name": "psrType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
            "required": True,
        }
    )
    production_power_system_resources_high_voltage_limit: Optional[
        EsmpVoltage
    ] = field(
        default=None,
        metadata={
            "name": "production_PowerSystemResources.highVoltageLimit",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
        },
    )
    nominal_ip_power_system_resources_nominal_p: Optional[EsmpActivePower] = (
        field(
            default=None,
            metadata={
                "name": "nominalIP_PowerSystemResources.nominalP",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
            },
        )
    )
    generating_unit_power_system_resources: list[MktGeneratingUnit] = field(
        default_factory=list,
        metadata={
            "name": "GeneratingUnit_PowerSystemResources",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
        },
    )


class TimeSeries(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
            "required": True,
            "max_length": 35,
        }
    )
    business_type: BusinessTypeList = field(
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
            "required": True,
        }
    )
    implementation_date_and_or_time_date: XmlDate = field(
        metadata={
            "name": "implementation_DateAndOrTime.date",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
            "required": True,
        }
    )
    bidding_zone_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "biddingZone_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
        },
    )
    registered_resource_m_rid: ResourceIdString = field(
        metadata={
            "name": "registeredResource.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
            "required": True,
        }
    )
    registered_resource_name: str = field(
        metadata={
            "name": "registeredResource.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
            "required": True,
        }
    )
    registered_resource_location_name: str = field(
        metadata={
            "name": "registeredResource.location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
            "required": True,
        }
    )
    control_area_domain: list[ControlAreaDomain] = field(
        default_factory=list,
        metadata={
            "name": "ControlArea_Domain",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
            "min_occurs": 1,
        },
    )
    provider_market_participant: list[ProviderMarketParticipant] = field(
        default_factory=list,
        metadata={
            "name": "Provider_MarketParticipant",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
            "min_occurs": 1,
        },
    )
    mkt_psrtype: MktPsrtype = field(
        metadata={
            "name": "MktPSRType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0",
            "required": True,
        }
    )


class ConfigurationMarketDocument(BaseModel):
    class Meta:
        name = "Configuration_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-6:configurationdocument:3:0"

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "required": True,
            "max_length": 35,
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
    time_series: list[TimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "TimeSeries",
            "type": "Element",
        },
    )

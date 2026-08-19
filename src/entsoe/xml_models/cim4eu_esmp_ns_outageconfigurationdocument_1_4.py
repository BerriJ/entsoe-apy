from __future__ import annotations

from decimal import Decimal

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDate
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    AssetTypeList,
    CodingSchemeTypeList,
    IndicatorTypeList,
    MessageTypeList,
    ProcessTypeList,
    RoleTypeList,
    StatusTypeList,
    UnitOfMeasureTypeList,
    UnitSymbol,
)

__NAMESPACE__ = "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4"


class AreaIdString(BaseModel):
    class Meta:
        name = "AreaID_String"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "max_length": 18,
        },
    )
    coding_scheme: CodingSchemeTypeList = field(
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
        }
    )


class EsmpVoltage(BaseModel):
    class Meta:
        name = "ESMP_Voltage"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "pattern": r"([0-9]*\.?[0-9]*)",
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
            "max_length": 16,
        },
    )
    coding_scheme: CodingSchemeTypeList = field(
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
        }
    )


class ResourceIdString(BaseModel):
    class Meta:
        name = "ResourceID_String"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "max_length": 60,
        },
    )
    coding_scheme: CodingSchemeTypeList = field(
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
        }
    )


class ConnectedRegisteredResource(BaseModel):
    class Meta:
        name = "Connected_RegisteredResource"

    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        }
    )


class Domain(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: AreaIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        }
    )


class OtherMarketParticipant(BaseModel):
    class Meta:
        name = "Other_MarketParticipant"

    model_config = ConfigDict(defer_build=True)
    m_rid: PartyIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        }
    )


class SpecificRegisteredResource(BaseModel):
    class Meta:
        name = "Specific_RegisteredResource"

    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        }
    )


class RegisteredResource(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        }
    )
    location_name: None | str = field(
        default=None,
        metadata={
            "name": "location.name",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
            "max_length": 200,
        },
    )
    p_srtype_psr_type: AssetTypeList = field(
        metadata={
            "name": "pSRType.psrType",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        }
    )
    p_srtype_power_system_resources_high_voltage_limit: EsmpVoltage = field(
        metadata={
            "name": "pSRType.powerSystemResources.highVoltageLimit",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        }
    )
    p_srtype_power_system_resources_low_voltage_limit: None | EsmpVoltage = (
        field(
            default=None,
            metadata={
                "name": "pSRType.powerSystemResources.lowVoltageLimit",
                "type": "Element",
                "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
            },
        )
    )
    interesting_market_object_status_status: None | StatusTypeList = field(
        default=None,
        metadata={
            "name": "interesting_MarketObjectStatus.status",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        },
    )
    relevant_market_object_status_status: None | StatusTypeList = field(
        default=None,
        metadata={
            "name": "relevant_MarketObjectStatus.status",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        },
    )
    associated_domain: list[Domain] = field(
        default_factory=list,
        metadata={
            "name": "Associated_Domain",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        },
    )
    connected_registered_resource: list[ConnectedRegisteredResource] = field(
        default_factory=list,
        metadata={
            "name": "Connected_RegisteredResource",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        },
    )


class TimeSeries(BaseModel):
    model_config = ConfigDict(defer_build=True)
    registered_resource: RegisteredResource = field(
        metadata={
            "name": "RegisteredResource",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        }
    )
    cancelled_ts: None | IndicatorTypeList = field(
        default=None,
        metadata={
            "name": "cancelledTS",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        },
    )
    owner_market_participant_m_rid: PartyIdString = field(
        metadata={
            "name": "owner_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        }
    )
    implementation_date_and_or_time_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "implementation_DateAndOrTime.date",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        },
    )
    active_measurement_unit_name: None | UnitOfMeasureTypeList = field(
        default=None,
        metadata={
            "name": "active_Measurement_Unit.name",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        },
    )
    installed_generation_quantity_quantity: None | Decimal = field(
        default=None,
        metadata={
            "name": "installedGeneration_Quantity.quantity",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        },
    )
    installed_consumption_quantity_quantity: None | Decimal = field(
        default=None,
        metadata={
            "name": "installedConsumption_Quantity.quantity",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        },
    )
    installed_reactive_quantity_quantity: None | Decimal = field(
        default=None,
        metadata={
            "name": "installedReactive_Quantity.quantity",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        },
    )
    reactive_measurement_unit_name: None | UnitOfMeasureTypeList = field(
        default=None,
        metadata={
            "name": "reactive_Measurement_Unit.name",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        },
    )
    multipod_registered_resource_m_rid: None | ResourceIdString = field(
        default=None,
        metadata={
            "name": "multipod_RegisteredResource.mRID",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        },
    )
    domain: list[Domain] = field(
        default_factory=list,
        metadata={
            "name": "Domain",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
            "min_occurs": 1,
        },
    )
    coordination_market_participant: list[OtherMarketParticipant] = field(
        default_factory=list,
        metadata={
            "name": "Coordination_MarketParticipant",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        },
    )
    interested_market_participant: list[OtherMarketParticipant] = field(
        default_factory=list,
        metadata={
            "name": "Interested_MarketParticipant",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        },
    )
    relevant_market_participant: list[OtherMarketParticipant] = field(
        default_factory=list,
        metadata={
            "name": "Relevant_MarketParticipant",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        },
    )
    specific_registered_resource: list[SpecificRegisteredResource] = field(
        default_factory=list,
        metadata={
            "name": "Specific_RegisteredResource",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        },
    )
    start_lifetime_date_and_or_time_date: XmlDate = field(
        metadata={
            "name": "startLifetime_DateAndOrTime.date",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        }
    )
    end_lifetime_date_and_or_time_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "endLifetime_DateAndOrTime.date",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4",
        },
    )


class OutageConfigurationMarketDocument(BaseModel):
    class Meta:
        name = "OutageConfiguration_MarketDocument"
        namespace = "https://cim4.eu/esmp/ns/outageconfigurationdocument/1-4"

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "max_length": 60,
        }
    )
    type_value: MessageTypeList = field(
        metadata={
            "name": "type",
            "type": "Element",
        }
    )
    process_process_type: ProcessTypeList = field(
        metadata={
            "name": "process.processType",
            "type": "Element",
        }
    )
    sender_market_participant_m_rid: PartyIdString = field(
        metadata={
            "name": "sender_MarketParticipant.mRID",
            "type": "Element",
        }
    )
    sender_market_participant_market_role_type: RoleTypeList = field(
        metadata={
            "name": "sender_MarketParticipant.marketRole.type",
            "type": "Element",
        }
    )
    receiver_market_participant_m_rid: PartyIdString = field(
        metadata={
            "name": "receiver_MarketParticipant.mRID",
            "type": "Element",
        }
    )
    receiver_market_participant_market_role_type: RoleTypeList = field(
        metadata={
            "name": "receiver_MarketParticipant.marketRole.type",
            "type": "Element",
        }
    )
    created_date_time: str = field(
        metadata={
            "name": "createdDateTime",
            "type": "Element",
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)",
        }
    )
    time_series: list[TimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "TimeSeries",
            "type": "Element",
            "min_occurs": 1,
        },
    )

from __future__ import annotations

from decimal import Decimal

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDate, XmlDuration, XmlTime
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    AssetTypeList,
    BusinessTypeList,
    CodingSchemeTypeList,
    CurveTypeList,
    MessageTypeList,
    ProcessTypeList,
    ReasonCodeTypeList,
    RoleTypeList,
    StatusTypeList,
    UnitOfMeasureTypeList,
    UnitSymbol,
)

__NAMESPACE__ = "urn:ebix.eu:ProofOfConcept:1:0"


class EsmpDateTimeInterval(BaseModel):
    class Meta:
        name = "ESMP_DateTimeInterval"

    model_config = ConfigDict(defer_build=True)
    start: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )
    end: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
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
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        }
    )


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


class EsmpActivePower(BaseModel):
    class Meta:
        name = "ESMP_ActivePower"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "pattern": r"([0-9]*\.?[0-9]*)",
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


class Reason(BaseModel):
    model_config = ConfigDict(defer_build=True)
    code: ReasonCodeTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        }
    )
    text: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
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
            "max_length": 60,
        },
    )
    coding_scheme: CodingSchemeTypeList = field(
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
        }
    )


class AssetRegisteredResource(BaseModel):
    class Meta:
        name = "Asset_RegisteredResource"

    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )
    asset_psrtype_psr_type: None | AssetTypeList = field(
        default=None,
        metadata={
            "name": "asset_PSRType.psrType",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )
    location_name: None | str = field(
        default=None,
        metadata={
            "name": "location.name",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )


class PtdfdomainSeries(BaseModel):
    class Meta:
        name = "PTDFDomain_Series"

    model_config = ConfigDict(defer_build=True)
    p_tdf_domain_m_rid: None | AreaIdString = field(
        default=None,
        metadata={
            "name": "pTDF_Domain.mRID",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )
    p_tdf_domain_unavailable_import_capability_quantity_quantity: (
        None | Decimal
    ) = field(
        default=None,
        metadata={
            "name": "pTDF_Domain.unavailableImportCapability_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )
    p_tdf_domain_unavailable_export_capability_quantity_quantity: (
        None | Decimal
    ) = field(
        default=None,
        metadata={
            "name": "pTDF_Domain.unavailableExportCapability_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )


class Point(BaseModel):
    model_config = ConfigDict(defer_build=True)
    position: int = field(
        metadata={
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )
    quantity: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )
    installed_quantity_quantity: None | Decimal = field(
        default=None,
        metadata={
            "name": "installed_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )
    ptdfdomain_series: list[PtdfdomainSeries] = field(
        default_factory=list,
        metadata={
            "name": "PTDFDomain_Series",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
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
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        }
    )
    resolution: XmlDuration = field(
        metadata={
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        }
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
            "min_occurs": 1,
        },
    )


class TimeSeries(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
            "max_length": 60,
        }
    )
    business_type: BusinessTypeList = field(
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        }
    )
    bidding_zone_domain_m_rid: None | AreaIdString = field(
        default=None,
        metadata={
            "name": "biddingZone_Domain.mRID",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )
    in_domain_m_rid: None | AreaIdString = field(
        default=None,
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )
    out_domain_m_rid: None | AreaIdString = field(
        default=None,
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )
    start_date_and_or_time_date: XmlDate = field(
        metadata={
            "name": "start_DateAndOrTime.date",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        }
    )
    start_date_and_or_time_time: XmlTime = field(
        metadata={
            "name": "start_DateAndOrTime.time",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        }
    )
    end_date_and_or_time_date: XmlDate = field(
        metadata={
            "name": "end_DateAndOrTime.date",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        }
    )
    end_date_and_or_time_time: XmlTime = field(
        metadata={
            "name": "end_DateAndOrTime.time",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        }
    )
    quantity_measurement_unit_name: UnitOfMeasureTypeList = field(
        metadata={
            "name": "quantity_Measurement_Unit.name",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        }
    )
    curve_type: CurveTypeList = field(
        metadata={
            "name": "curveType",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        }
    )
    production_registered_resource_m_rid: None | ResourceIdString = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.mRID",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )
    production_registered_resource_name: None | str = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.name",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )
    production_registered_resource_location_name: None | str = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.location.name",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )
    production_registered_resource_p_srtype_psr_type: None | AssetTypeList = (
        field(
            default=None,
            metadata={
                "name": "production_RegisteredResource.pSRType.psrType",
                "type": "Element",
                "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
            },
        )
    )
    production_registered_resource_p_srtype_power_system_resources_m_rid: (
        None | ResourceIdString
    ) = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.pSRType.powerSystemResources.mRID",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )
    production_registered_resource_p_srtype_power_system_resources_name: (
        None | str
    ) = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.pSRType.powerSystemResources.name",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )
    production_registered_resource_p_srtype_power_system_resources_nominal_p: (
        None | EsmpActivePower
    ) = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.pSRType.powerSystemResources.nominalP",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )
    asset_registered_resource: list[AssetRegisteredResource] = field(
        default_factory=list,
        metadata={
            "name": "Asset_RegisteredResource",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )
    available_period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Available_Period",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )
    wind_power_feedin_period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "WindPowerFeedin_Period",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:ebix.eu:ProofOfConcept:1:0",
        },
    )


class UnavailabilityMarketDocument(BaseModel):
    class Meta:
        name = "Unavailability_MarketDocument"
        namespace = "urn:ebix.eu:ProofOfConcept:1:0"

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "max_length": 60,
        }
    )
    revision_number: str = field(
        metadata={
            "name": "revisionNumber",
            "type": "Element",
            "pattern": r"[1-9]([0-9]){0,2}",
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
    created_date_time: str = field(
        metadata={
            "name": "createdDateTime",
            "type": "Element",
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)",
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
    unavailability_time_period_time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "unavailability_Time_Period.timeInterval",
            "type": "Element",
        }
    )
    doc_status: None | ActionStatus = field(
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
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
        },
    )

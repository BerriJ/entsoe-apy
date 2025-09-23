from decimal import Decimal
from typing import Optional

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

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1"


class EsmpDateTimeInterval(BaseModel):
    class Meta:
        name = "ESMP_DateTimeInterval"

    model_config = ConfigDict(defer_build=True)
    start: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )
    end: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )


class Point(BaseModel):
    model_config = ConfigDict(defer_build=True)
    position: int = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )
    quantity: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
            "required": True,
        }
    )


class ActionStatus(BaseModel):
    class Meta:
        name = "Action_Status"

    model_config = ConfigDict(defer_build=True)
    value: StatusTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
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


class EsmpActivePower(BaseModel):
    class Meta:
        name = "ESMP_ActivePower"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
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
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
            "required": True,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
            "required": True,
        }
    )
    resolution: XmlDuration = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
            "required": True,
        }
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
            "min_occurs": 1,
        },
    )


class AssetRegisteredResource(BaseModel):
    class Meta:
        name = "Asset_RegisteredResource"

    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
        },
    )
    asset_psrtype_psr_type: Optional[AssetTypeList] = field(
        default=None,
        metadata={
            "name": "asset_PSRType.psrType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
        },
    )
    location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
        },
    )


class TimeSeries(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
            "required": True,
            "max_length": 60,
        }
    )
    business_type: BusinessTypeList = field(
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
            "required": True,
        }
    )
    bidding_zone_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "biddingZone_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
        },
    )
    in_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
        },
    )
    out_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
        },
    )
    start_date_and_or_time_date: XmlDate = field(
        metadata={
            "name": "start_DateAndOrTime.date",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
            "required": True,
        }
    )
    start_date_and_or_time_time: XmlTime = field(
        metadata={
            "name": "start_DateAndOrTime.time",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
            "required": True,
        }
    )
    end_date_and_or_time_date: XmlDate = field(
        metadata={
            "name": "end_DateAndOrTime.date",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
            "required": True,
        }
    )
    end_date_and_or_time_time: XmlTime = field(
        metadata={
            "name": "end_DateAndOrTime.time",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
            "required": True,
        }
    )
    quantity_measurement_unit_name: UnitOfMeasureTypeList = field(
        metadata={
            "name": "quantity_Measurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
            "required": True,
        }
    )
    curve_type: CurveTypeList = field(
        metadata={
            "name": "curveType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
            "required": True,
        }
    )
    production_registered_resource_m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
        },
    )
    production_registered_resource_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
        },
    )
    production_registered_resource_location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.location.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
        },
    )
    production_registered_resource_p_srtype_psr_type: Optional[
        AssetTypeList
    ] = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.pSRType.psrType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
        },
    )
    production_registered_resource_p_srtype_power_system_resources_m_rid: Optional[
        ResourceIdString
    ] = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.pSRType.powerSystemResources.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
        },
    )
    production_registered_resource_p_srtype_power_system_resources_name: Optional[
        str
    ] = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.pSRType.powerSystemResources.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
        },
    )
    production_registered_resource_p_srtype_power_system_resources_nominal_p: Optional[
        EsmpActivePower
    ] = field(
        default=None,
        metadata={
            "name": "production_RegisteredResource.pSRType.powerSystemResources.nominalP",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
        },
    )
    asset_registered_resource: list[AssetRegisteredResource] = field(
        default_factory=list,
        metadata={
            "name": "Asset_RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
        },
    )
    available_period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Available_Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
        },
    )
    wind_power_feedin_period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "WindPowerFeedin_Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1",
        },
    )


class UnavailabilityMarketDocument(BaseModel):
    class Meta:
        name = "Unavailability_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-6:outagedocument:4:1"

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
    created_date_time: str = field(
        metadata={
            "name": "createdDateTime",
            "type": "Element",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)",
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
    unavailability_time_period_time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "unavailability_Time_Period.timeInterval",
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
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
        },
    )

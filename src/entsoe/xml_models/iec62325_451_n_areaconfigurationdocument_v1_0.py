from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDateTime
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    AssetTypeList,
    CodingSchemeTypeList,
    MessageTypeList,
    ObjectAggregationTypeList,
    ProcessTypeList,
    RoleTypeList,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0"


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


class ConnectedDomain(BaseModel):
    class Meta:
        name = "Connected_Domain"

    model_config = ConfigDict(defer_build=True)
    m_rid: AreaIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
        },
    )


class ConnectionDetailRegisteredResource(BaseModel):
    class Meta:
        name = "ConnectionDetail_RegisteredResource"

    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
            "required": True,
        }
    )
    area_identification_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "areaIdentification_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
        },
    )
    component_type_mkt_psrtype_psr_type: Optional[AssetTypeList] = field(
        default=None,
        metadata={
            "name": "componentType_MktPSRType.psrType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
        },
    )


class ConsistOfDomain(BaseModel):
    class Meta:
        name = "ConsistOf_Domain"

    model_config = ConfigDict(defer_build=True)
    m_rid: AreaIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
        },
    )


class BorderConnectionSeries(BaseModel):
    class Meta:
        name = "BorderConnection_Series"

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
            "required": True,
            "max_length": 60,
        }
    )
    border_component_type_mkt_psrtype_psr_type: AssetTypeList = field(
        metadata={
            "name": "borderComponentType_MktPSRType.psrType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
            "required": True,
        }
    )
    connection_detail_registered_resource: list[
        ConnectionDetailRegisteredResource
    ] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionDetail_RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
            "max_occurs": 2,
        },
    )


class AreaSpecificationSeries(BaseModel):
    class Meta:
        name = "AreaSpecification_Series"

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
            "required": True,
            "max_length": 60,
        }
    )
    market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "marketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
        },
    )
    market_participant_market_role_type: Optional[RoleTypeList] = field(
        default=None,
        metadata={
            "name": "marketParticipant.marketRole.type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
        },
    )
    area_domain_m_rid: AreaIdString = field(
        metadata={
            "name": "area_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
            "required": True,
        }
    )
    area_domain_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "area_Domain.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
        },
    )
    object_aggregation: Optional[ObjectAggregationTypeList] = field(
        default=None,
        metadata={
            "name": "objectAggregation",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
        },
    )
    country_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "country_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
        },
    )
    area_characteristics_domain_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "areaCharacteristics_Domain.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
        },
    )
    validity_start_date_and_or_time_date_time: XmlDateTime = field(
        metadata={
            "name": "validityStart_DateAndOrTime.dateTime",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
            "required": True,
        }
    )
    validity_end_date_and_or_time_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "validityEnd_DateAndOrTime.dateTime",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
        },
    )
    consist_of_domain: list[ConsistOfDomain] = field(
        default_factory=list,
        metadata={
            "name": "ConsistOf_Domain",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
        },
    )
    connected_domain: list[ConnectedDomain] = field(
        default_factory=list,
        metadata={
            "name": "Connected_Domain",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
        },
    )
    border_connection_series: list[BorderConnectionSeries] = field(
        default_factory=list,
        metadata={
            "name": "BorderConnection_Series",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
        },
    )
    area_connection_detail_registered_resource: list[
        ConnectionDetailRegisteredResource
    ] = field(
        default_factory=list,
        metadata={
            "name": "AreaConnectionDetail_RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0",
        },
    )


class AreaConfigurationMarketDocument(BaseModel):
    class Meta:
        name = "AreaConfiguration_MarketDocument"
        namespace = (
            "urn:iec62325.351:tc57wg16:451-n:areaconfigurationdocument:1:0"
        )

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "required": True,
            "max_length": 60,
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
    area_specification_series: list[AreaSpecificationSeries] = field(
        default_factory=list,
        metadata={
            "name": "AreaSpecification_Series",
            "type": "Element",
        },
    )

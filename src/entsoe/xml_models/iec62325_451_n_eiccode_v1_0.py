from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDate
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    CodingSchemeTypeList,
    MessageTypeList,
    RoleTypeList,
    StatusTypeList,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0"


class ElectronicAddress(BaseModel):
    model_config = ConfigDict(defer_build=True)
    email1: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            "required": True,
            "max_length": 70,
        }
    )


class FunctionName(BaseModel):
    class Meta:
        name = "Function_Name"

    model_config = ConfigDict(defer_build=True)
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            "required": True,
            "max_length": 70,
        }
    )


class StreetDetail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    address_general: Optional[str] = field(
        default=None,
        metadata={
            "name": "addressGeneral",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            "max_length": 70,
        },
    )
    address_general2: Optional[str] = field(
        default=None,
        metadata={
            "name": "addressGeneral2",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            "max_length": 70,
        },
    )
    address_general3: Optional[str] = field(
        default=None,
        metadata={
            "name": "addressGeneral3",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            "max_length": 70,
        },
    )


class TelephoneNumber(BaseModel):
    model_config = ConfigDict(defer_build=True)
    itu_phone: str = field(
        metadata={
            "name": "ituPhone",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            "required": True,
            "max_length": 15,
        }
    )


class TownDetail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            "max_length": 35,
        },
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            "length": 2,
            "pattern": r"[A-Z]*",
        },
    )


class ActionStatus(BaseModel):
    class Meta:
        name = "Action_Status"

    model_config = ConfigDict(defer_build=True)
    value: StatusTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
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


class StreetAddress(BaseModel):
    model_config = ConfigDict(defer_build=True)
    street_detail: Optional[StreetDetail] = field(
        default=None,
        metadata={
            "name": "streetDetail",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
        },
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "postalCode",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            "max_length": 10,
        },
    )
    town_detail: Optional[TownDetail] = field(
        default=None,
        metadata={
            "name": "townDetail",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
        },
    )


class EiccodeMarketDocument(BaseModel):
    class Meta:
        name = "EICCode_MarketDocument"

    model_config = ConfigDict(defer_build=True)
    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            "length": 16,
            "pattern": r"([A-Z0-9]{2}(([A-Z0-9]|[-]){13})[A-Z0-9])",
        },
    )
    status: Optional[ActionStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
        },
    )
    doc_status: Optional[ActionStatus] = field(
        default=None,
        metadata={
            "name": "docStatus",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
        },
    )
    attribute_instance_component_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeInstanceComponent.attribute",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
        },
    )
    long_names_name: str = field(
        metadata={
            "name": "long_Names.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            "required": True,
            "max_length": 70,
        }
    )
    display_names_name: str = field(
        metadata={
            "name": "display_Names.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            "required": True,
            "max_length": 16,
            "pattern": r"([A-Z\-\+_0-9]+)",
        }
    )
    last_request_date_and_or_time_date: XmlDate = field(
        metadata={
            "name": "lastRequest_DateAndOrTime.date",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            "required": True,
        }
    )
    deactivation_requested_date_and_or_time_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "deactivationRequested_DateAndOrTime.date",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
        },
    )
    e_iccontact_market_participant_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "eICContact_MarketParticipant.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            "max_length": 70,
        },
    )
    e_iccontact_market_participant_phone1: Optional[TelephoneNumber] = field(
        default=None,
        metadata={
            "name": "eICContact_MarketParticipant.phone1",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
        },
    )
    e_iccontact_market_participant_electronic_address: Optional[
        ElectronicAddress
    ] = field(
        default=None,
        metadata={
            "name": "eICContact_MarketParticipant.electronicAddress",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
        },
    )
    e_iccode_market_participant_street_address: Optional[StreetAddress] = (
        field(
            default=None,
            metadata={
                "name": "eICCode_MarketParticipant.streetAddress",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            },
        )
    )
    e_iccode_market_participant_a_cercode_names_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "eICCode_MarketParticipant.aCERCode_Names.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            "length": 12,
            "pattern": r"([A-Za-z0-9_]+\.[A-Z][A-Z])",
        },
    )
    e_iccode_market_participant_v_atcode_names_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "eICCode_MarketParticipant.vATCode_Names.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            "max_length": 14,
            "pattern": r"([A-Z0-9]+)",
        },
    )
    e_icparent_market_document_m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "eICParent_MarketDocument.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            "length": 16,
            "pattern": r"([A-Z0-9]{2}(([A-Z0-9]|[-]){13})[A-Z0-9])",
        },
    )
    e_icresponsible_market_participant_m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "eICResponsible_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            "length": 16,
            "pattern": r"([A-Z0-9]{2}(([A-Z0-9]|[-]){13})[A-Z0-9])",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
            "max_length": 700,
        },
    )
    function_names: list[FunctionName] = field(
        default_factory=list,
        metadata={
            "name": "Function_Names",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0",
        },
    )


class EicMarketDocument(BaseModel):
    class Meta:
        name = "EIC_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:0"

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
    sender_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "sender_MarketParticipant.mRID",
            "type": "Element",
        },
    )
    sender_market_participant_market_role_type: Optional[RoleTypeList] = field(
        default=None,
        metadata={
            "name": "sender_MarketParticipant.marketRole.type",
            "type": "Element",
        },
    )
    receiver_market_participant_m_rid: Optional[PartyIdString] = field(
        default=None,
        metadata={
            "name": "receiver_MarketParticipant.mRID",
            "type": "Element",
        },
    )
    receiver_market_participant_market_role_type: Optional[RoleTypeList] = (
        field(
            default=None,
            metadata={
                "name": "receiver_MarketParticipant.marketRole.type",
                "type": "Element",
            },
        )
    )
    created_date_time: str = field(
        metadata={
            "name": "createdDateTime",
            "type": "Element",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)",
        }
    )
    eiccode_market_document: list[EiccodeMarketDocument] = field(
        default_factory=list,
        metadata={
            "name": "EICCode_MarketDocument",
            "type": "Element",
        },
    )

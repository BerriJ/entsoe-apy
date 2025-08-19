from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from .urn_entsoe_eu_wgedi_codelists import (
    CodingSchemeTypeList,
    MessageTypeList,
    RoleTypeList,
    StatusTypeList,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1"


@dataclass
class ElectronicAddress:
    email1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            "required": True,
            "max_length": 70,
        },
    )


@dataclass
class FunctionName:
    class Meta:
        name = "Function_Name"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            "required": True,
            "max_length": 70,
        },
    )


@dataclass
class StreetDetail:
    address_general: Optional[str] = field(
        default=None,
        metadata={
            "name": "addressGeneral",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            "max_length": 70,
        },
    )
    address_general2: Optional[str] = field(
        default=None,
        metadata={
            "name": "addressGeneral2",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            "max_length": 70,
        },
    )
    address_general3: Optional[str] = field(
        default=None,
        metadata={
            "name": "addressGeneral3",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            "max_length": 70,
        },
    )
    floor_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "floorIdentification",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            "required": True,
            "max_length": 35,
        },
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
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
class StreetAddress:
    street_detail: Optional[StreetDetail] = field(
        default=None,
        metadata={
            "name": "streetDetail",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            "required": True,
        },
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "postalCode",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            "required": True,
            "max_length": 10,
        },
    )
    town_detail: Optional[TownDetail] = field(
        default=None,
        metadata={
            "name": "townDetail",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            "required": True,
        },
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
        },
    )


@dataclass
class EiccodeMarketDocument:
    class Meta:
        name = "EICCode_MarketDocument"

    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            "length": 16,
            "pattern": r"([A-Z0-9]{2}(([A-Z0-9]|[-]){13})[A-Z0-9])",
        },
    )
    status: Optional[ActionStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
        },
    )
    doc_status: Optional[ActionStatus] = field(
        default=None,
        metadata={
            "name": "docStatus",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
        },
    )
    attribute_instance_component_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeInstanceComponent.attribute",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
        },
    )
    long_names_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "long_Names.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            "required": True,
            "max_length": 70,
        },
    )
    display_names_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "display_Names.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            "required": True,
            "max_length": 16,
            "pattern": r"([A-Z\-\+_0-9]+)",
        },
    )
    last_request_date_and_or_time_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "lastRequest_DateAndOrTime.date",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            "required": True,
        },
    )
    deactivation_requested_date_and_or_time_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "deactivationRequested_DateAndOrTime.date",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
        },
    )
    e_iccontact_market_participant_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "eICContact_MarketParticipant.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            "max_length": 70,
        },
    )
    e_iccontact_market_participant_phone1: Optional[TelephoneNumber] = field(
        default=None,
        metadata={
            "name": "eICContact_MarketParticipant.phone1",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
        },
    )
    e_iccontact_market_participant_electronic_address: Optional[ElectronicAddress] = (
        field(
            default=None,
            metadata={
                "name": "eICContact_MarketParticipant.electronicAddress",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            },
        )
    )
    e_iccode_market_participant_street_address: Optional[StreetAddress] = field(
        default=None,
        metadata={
            "name": "eICCode_MarketParticipant.streetAddress",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
        },
    )
    e_iccode_market_participant_a_cercode_names_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "eICCode_MarketParticipant.aCERCode_Names.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            "length": 12,
            "pattern": r"([A-Za-z0-9_]+\.[A-Z][A-Z])",
        },
    )
    e_iccode_market_participant_v_atcode_names_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "eICCode_MarketParticipant.vATCode_Names.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            "max_length": 25,
            "pattern": r"([A-Z0-9]+)",
        },
    )
    e_icparent_market_document_m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "eICParent_MarketDocument.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            "length": 16,
            "pattern": r"([A-Z0-9]{2}(([A-Z0-9]|[-]){13})[A-Z0-9])",
        },
    )
    e_icresponsible_market_participant_m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "eICResponsible_MarketParticipant.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            "length": 16,
            "pattern": r"([A-Z0-9]{2}(([A-Z0-9]|[-]){13})[A-Z0-9])",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
            "max_length": 700,
        },
    )
    function_names: list[FunctionName] = field(
        default_factory=list,
        metadata={
            "name": "Function_Names",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1",
        },
    )


@dataclass
class EicMarketDocument:
    class Meta:
        name = "EIC_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-n:eicdocument:1:1"

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
    receiver_market_participant_market_role_type: Optional[RoleTypeList] = field(
        default=None,
        metadata={
            "name": "receiver_MarketParticipant.marketRole.type",
            "type": "Element",
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
    eiccode_market_document: list[EiccodeMarketDocument] = field(
        default_factory=list,
        metadata={
            "name": "EICCode_MarketDocument",
            "type": "Element",
        },
    )

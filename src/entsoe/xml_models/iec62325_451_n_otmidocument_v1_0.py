from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDateTime
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    CodingSchemeTypeList,
    MessageTypeList,
    ReasonCodeTypeList,
    RoleTypeList,
    StatusTypeList,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-n:otmidocument:1:0"


class ActionStatus(BaseModel):
    class Meta:
        name = "Action_Status"

    model_config = ConfigDict(defer_build=True)
    value: StatusTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:otmidocument:1:0",
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


class OtherTransparencyMarketInformationMarketDocument(BaseModel):
    class Meta:
        name = "OtherTransparencyMarketInformation_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-n:otmidocument:1:0"

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
    doc_status: ActionStatus = field(
        metadata={
            "name": "docStatus",
            "type": "Element",
            "required": True,
        }
    )
    publication_date_and_or_time_date_time: XmlDateTime = field(
        metadata={
            "name": "publication_DateAndOrTime.dateTime",
            "type": "Element",
            "required": True,
        }
    )
    start_date_and_or_time_date_time: XmlDateTime = field(
        metadata={
            "name": "start_DateAndOrTime.dateTime",
            "type": "Element",
            "required": True,
        }
    )
    end_date_and_or_time_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "end_DateAndOrTime.dateTime",
            "type": "Element",
        },
    )
    reason_code: ReasonCodeTypeList = field(
        metadata={
            "name": "reason.code",
            "type": "Element",
            "required": True,
        }
    )
    reason_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "reason.text",
            "type": "Element",
            "max_length": 512,
        },
    )

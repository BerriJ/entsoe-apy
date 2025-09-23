from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlTime
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    AnalogTypeList,
    AssetTypeList,
    BusinessTypeList,
    CodingSchemeTypeList,
    CurrencyTypeList,
    CurveTypeList,
    IndicatorTypeList,
    MessageTypeList,
    ProcessTypeList,
    QualityTypeList,
    ReasonCodeTypeList,
    RoleTypeList,
    StatusTypeList,
    UnitOfMeasureTypeList,
    UnitSymbol,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3"


class EsmpDateTimeInterval(BaseModel):
    class Meta:
        name = "ESMP_DateTimeInterval"

    model_config = ConfigDict(defer_build=True)
    start: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )
    end: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )


class MarketDocument(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
            "max_length": 35,
        }
    )
    revision_number: str = field(
        metadata={
            "name": "revisionNumber",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
            "pattern": r"[1-9]([0-9]){0,2}",
        }
    )


class ActionStatus(BaseModel):
    class Meta:
        name = "Action_Status"

    model_config = ConfigDict(defer_build=True)
    value: StatusTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )


class Analog(BaseModel):
    model_config = ConfigDict(defer_build=True)
    measurement_type: AnalogTypeList = field(
        metadata={
            "name": "measurementType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )
    unit_symbol: UnitSymbol = field(
        metadata={
            "name": "unitSymbol",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )
    positive_flow_in: Optional[IndicatorTypeList] = field(
        default=None,
        metadata={
            "name": "positiveFlowIn",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    analog_values_value: str = field(
        metadata={
            "name": "analogValues.value",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
            "pattern": r"([0-9]*\.?[0-9]*)",
        }
    )
    analog_values_time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "analogValues.timeStamp",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    analog_values_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "analogValues.description",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
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
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "max_length": 512,
        },
    )


class RegisteredResourceReason(BaseModel):
    class Meta:
        name = "RegisteredResource_Reason"

    model_config = ConfigDict(defer_build=True)
    code: ReasonCodeTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
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


class SeriesReason(BaseModel):
    class Meta:
        name = "Series_Reason"

    model_config = ConfigDict(defer_build=True)
    code: ReasonCodeTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "max_length": 512,
        },
    )


class AdditionalConstraintRegisteredResource(BaseModel):
    class Meta:
        name = "AdditionalConstraint_RegisteredResource"

    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    in_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    out_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    market_object_status_status: Optional[StatusTypeList] = field(
        default=None,
        metadata={
            "name": "marketObjectStatus.status",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    reason: list[RegisteredResourceReason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )


class ContingencyRegisteredResource(BaseModel):
    class Meta:
        name = "Contingency_RegisteredResource"

    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    in_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    out_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    reason: list[RegisteredResourceReason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )


class PtdfDomain(BaseModel):
    class Meta:
        name = "PTDF_Domain"

    model_config = ConfigDict(defer_build=True)
    m_rid: AreaIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )
    p_tdf_quantity_quantity: Decimal = field(
        metadata={
            "name": "pTDF_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )
    p_tdf_quantity_quality: Optional[QualityTypeList] = field(
        default=None,
        metadata={
            "name": "pTDF_Quantity.quality",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )


class PartyMarketParticipant(BaseModel):
    class Meta:
        name = "Party_MarketParticipant"

    model_config = ConfigDict(defer_build=True)
    m_rid: PartyIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )


class RemedialActionRegisteredResource(BaseModel):
    class Meta:
        name = "RemedialAction_RegisteredResource"

    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    p_srtype_psr_type: AssetTypeList = field(
        metadata={
            "name": "pSRType.psrType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )
    in_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    out_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    in_aggregate_node_m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "in_AggregateNode.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    out_aggregate_node_m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "out_AggregateNode.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    market_object_status_status: StatusTypeList = field(
        metadata={
            "name": "marketObjectStatus.status",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )
    resource_capacity_maximum_capacity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "resourceCapacity.maximumCapacity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    resource_capacity_minimum_capacity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "resourceCapacity.minimumCapacity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    resource_capacity_default_capacity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "resourceCapacity.defaultCapacity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    resource_capacity_unit_symbol: Optional[UnitSymbol] = field(
        default=None,
        metadata={
            "name": "resourceCapacity.unitSymbol",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    reason: list[RegisteredResourceReason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )


class SharedDomain(BaseModel):
    class Meta:
        name = "Shared_Domain"

    model_config = ConfigDict(defer_build=True)
    m_rid: AreaIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )


class AdditionalConstraintSeries(BaseModel):
    class Meta:
        name = "AdditionalConstraint_Series"

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
            "max_length": 35,
        }
    )
    business_type: Optional[BusinessTypeList] = field(
        default=None,
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    party_market_participant: list[PartyMarketParticipant] = field(
        default_factory=list,
        metadata={
            "name": "Party_MarketParticipant",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    in_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    out_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    measurement_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "measurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    quantity_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    registered_resource: list[AdditionalConstraintRegisteredResource] = field(
        default_factory=list,
        metadata={
            "name": "RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    reason: list[SeriesReason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )


class ContingencySeries(BaseModel):
    class Meta:
        name = "Contingency_Series"

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
            "max_length": 35,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    party_market_participant: list[PartyMarketParticipant] = field(
        default_factory=list,
        metadata={
            "name": "Party_MarketParticipant",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    registered_resource: list[ContingencyRegisteredResource] = field(
        default_factory=list,
        metadata={
            "name": "RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    reason: list[SeriesReason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )


class MonitoredRegisteredResource(BaseModel):
    class Meta:
        name = "Monitored_RegisteredResource"

    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    in_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    out_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    in_aggregate_node_m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "in_AggregateNode.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    out_aggregate_node_m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "out_AggregateNode.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    flow_based_study_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "flowBasedStudy_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    flow_based_study_domain_flow_based_margin_quantity_quantity: Optional[
        Decimal
    ] = field(
        default=None,
        metadata={
            "name": "flowBasedStudy_Domain.flowBasedMargin_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    flow_based_study_domain_flow_based_margin_quantity_quality: Optional[
        QualityTypeList
    ] = field(
        default=None,
        metadata={
            "name": "flowBasedStudy_Domain.flowBasedMargin_Quantity.quality",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    market_coupling_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "marketCoupling_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    market_coupling_domain_shadow_price_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "marketCoupling_Domain.shadow_Price.amount",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "total_digits": 17,
        },
    )
    ptdf_domain: list[PtdfDomain] = field(
        default_factory=list,
        metadata={
            "name": "PTDF_Domain",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    measurements: list[Analog] = field(
        default_factory=list,
        metadata={
            "name": "Measurements",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    reason: list[RegisteredResourceReason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )


class RemedialActionSeries(BaseModel):
    class Meta:
        name = "RemedialAction_Series"

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
            "max_length": 35,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    business_type: Optional[BusinessTypeList] = field(
        default=None,
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    application_mode_market_object_status_status: Optional[StatusTypeList] = (
        field(
            default=None,
            metadata={
                "name": "applicationMode_MarketObjectStatus.status",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            },
        )
    )
    party_market_participant: list[PartyMarketParticipant] = field(
        default_factory=list,
        metadata={
            "name": "Party_MarketParticipant",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    in_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    out_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    measurement_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "measurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    quantity_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    registered_resource: list[RemedialActionRegisteredResource] = field(
        default_factory=list,
        metadata={
            "name": "RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    shared_domain: list[SharedDomain] = field(
        default_factory=list,
        metadata={
            "name": "Shared_Domain",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    reason: list[SeriesReason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )


class BorderSeries(BaseModel):
    class Meta:
        name = "Border_Series"

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
            "max_length": 35,
        }
    )
    business_type: BusinessTypeList = field(
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )
    in_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    out_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    flow_quantity_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "flow_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    connecting_line_registered_resource: list[MonitoredRegisteredResource] = (
        field(
            default_factory=list,
            metadata={
                "name": "ConnectingLine_RegisteredResource",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            },
        )
    )


class MonitoredSeries(BaseModel):
    class Meta:
        name = "Monitored_Series"

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
            "max_length": 35,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    party_market_participant: list[PartyMarketParticipant] = field(
        default_factory=list,
        metadata={
            "name": "Party_MarketParticipant",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    registered_resource: list[MonitoredRegisteredResource] = field(
        default_factory=list,
        metadata={
            "name": "RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    reason: list[SeriesReason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )


class ConstraintSeries(BaseModel):
    class Meta:
        name = "Constraint_Series"

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
            "max_length": 35,
        }
    )
    business_type: BusinessTypeList = field(
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    reference_calculation_date_and_or_time_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "referenceCalculation_DateAndOrTime.date",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    reference_calculation_date_and_or_time_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "referenceCalculation_DateAndOrTime.time",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    quantity_measurement_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "quantity_Measurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    external_constraint_quantity_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "externalConstraint_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    external_constraint_quantity_quality: Optional[QualityTypeList] = field(
        default=None,
        metadata={
            "name": "externalConstraint_Quantity.quality",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    p_tdf_measurement_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "pTDF_Measurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    shadow_price_measurement_unit_name: Optional[UnitOfMeasureTypeList] = (
        field(
            default=None,
            metadata={
                "name": "shadowPrice_Measurement_Unit.name",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            },
        )
    )
    currency_unit_name: Optional[CurrencyTypeList] = field(
        default=None,
        metadata={
            "name": "currency_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    party_market_participant: list[PartyMarketParticipant] = field(
        default_factory=list,
        metadata={
            "name": "Party_MarketParticipant",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    optimization_market_object_status_status: Optional[StatusTypeList] = field(
        default=None,
        metadata={
            "name": "optimization_MarketObjectStatus.status",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    additional_constraint_series: list[AdditionalConstraintSeries] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalConstraint_Series",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    contingency_series: list[ContingencySeries] = field(
        default_factory=list,
        metadata={
            "name": "Contingency_Series",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    monitored_series: list[MonitoredSeries] = field(
        default_factory=list,
        metadata={
            "name": "Monitored_Series",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    remedial_action_series: list[RemedialActionSeries] = field(
        default_factory=list,
        metadata={
            "name": "RemedialAction_Series",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )


class Point(BaseModel):
    model_config = ConfigDict(defer_build=True)
    position: int = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )
    border_series: list[BorderSeries] = field(
        default_factory=list,
        metadata={
            "name": "Border_Series",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    constraint_series: list[ConstraintSeries] = field(
        default_factory=list,
        metadata={
            "name": "Constraint_Series",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )
    resolution: XmlDuration = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "min_occurs": 1,
        },
    )


class TimeSeries(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
            "max_length": 35,
        }
    )
    business_type: BusinessTypeList = field(
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )
    in_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    out_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )
    curve_type: CurveTypeList = field(
        metadata={
            "name": "curveType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "required": True,
        }
    )
    period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
            "min_occurs": 1,
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3",
        },
    )


class CriticalNetworkElementMarketDocument(BaseModel):
    class Meta:
        name = "CriticalNetworkElement_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-n:cnedocument:2:3"

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
    doc_status: Optional[ActionStatus] = field(
        default=None,
        metadata={
            "name": "docStatus",
            "type": "Element",
        },
    )
    received_market_document: Optional[MarketDocument] = field(
        default=None,
        metadata={
            "name": "Received_MarketDocument",
            "type": "Element",
        },
    )
    related_market_document: list[MarketDocument] = field(
        default_factory=list,
        metadata={
            "name": "Related_MarketDocument",
            "type": "Element",
        },
    )
    time_period_time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "time_Period.timeInterval",
            "type": "Element",
            "required": True,
        }
    )
    domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "domain.mRID",
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

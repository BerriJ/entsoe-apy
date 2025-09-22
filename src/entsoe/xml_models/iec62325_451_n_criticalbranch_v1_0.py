from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDateTime, XmlDuration
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
)

__NAMESPACE__ = (
    "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0"
)


class AnalogValue(BaseModel):
    model_config = ConfigDict(defer_build=True)
    value: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
            "pattern": r"([0-9]+(\.[0-9]*))",
        }
    )
    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )


class EsmpDateTimeInterval(BaseModel):
    class Meta:
        name = "ESMP_DateTimeInterval"

    model_config = ConfigDict(defer_build=True)
    start: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )
    end: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )


class UnitSymbol(Enum):
    """
    :cvar AMPERE: The unit of electrical current in the International
        system of Units (SI) equivalent to one Coulomb per second.
    :cvar K_V: The symbol of kV
    :cvar MW: The symbol of MW
    :cvar ONE: A unit for dimensionless quantities, also called
        quantities of dimension one.
    :cvar PERCENT: A unit of proportion equal to 0.01.
    """

    AMPERE = "Ampere"
    K_V = "kV"
    MW = "MW"
    ONE = "One"
    PERCENT = "Percent"


class Analog(BaseModel):
    model_config = ConfigDict(defer_build=True)
    measurement_type: AnalogTypeList = field(
        metadata={
            "name": "measurementType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
        }
    )
    unit_symbol: UnitSymbol = field(
        metadata={
            "name": "unitSymbol",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
        }
    )
    positive_flow_in: Optional[IndicatorTypeList] = field(
        default=None,
        metadata={
            "name": "positiveFlowIn",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    analog_values: list[AnalogValue] = field(
        default_factory=list,
        metadata={
            "name": "AnalogValues",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "min_occurs": 1,
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


class MeasurementPointIdString(BaseModel):
    class Meta:
        name = "MeasurementPointID_String"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 35,
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
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
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


class OutageRegisteredResource(BaseModel):
    class Meta:
        name = "Outage_RegisteredResource"

    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    in_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    out_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    in_aggregate_node_m_rid: Optional[MeasurementPointIdString] = field(
        default=None,
        metadata={
            "name": "in_AggregateNode.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    out_aggregate_node_m_rid: Optional[MeasurementPointIdString] = field(
        default=None,
        metadata={
            "name": "out_AggregateNode.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
        }
    )
    p_tdf_quantity_quantity: Decimal = field(
        metadata={
            "name": "pTDF_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
        }
    )
    p_tdf_quantity_quality: Optional[QualityTypeList] = field(
        default=None,
        metadata={
            "name": "pTDF_Quantity.quality",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    in_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    out_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    in_aggregate_node_m_rid: Optional[MeasurementPointIdString] = field(
        default=None,
        metadata={
            "name": "in_AggregateNode.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    out_aggregate_node_m_rid: Optional[MeasurementPointIdString] = field(
        default=None,
        metadata={
            "name": "out_AggregateNode.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    p_srtype_psr_type: AssetTypeList = field(
        metadata={
            "name": "pSRType.psrType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
        }
    )
    market_object_status_status: StatusTypeList = field(
        metadata={
            "name": "marketObjectStatus.status",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
        }
    )


class MonitoredRegisteredResource(BaseModel):
    class Meta:
        name = "Monitored_RegisteredResource"

    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    in_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    out_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    in_aggregate_node_m_rid: Optional[MeasurementPointIdString] = field(
        default=None,
        metadata={
            "name": "in_AggregateNode.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    out_aggregate_node_m_rid: Optional[MeasurementPointIdString] = field(
        default=None,
        metadata={
            "name": "out_AggregateNode.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    measurements: list[Analog] = field(
        default_factory=list,
        metadata={
            "name": "Measurements",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    flow_based_study_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "flowBasedStudy_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    flow_based_study_domain_flow_based_margin_quantity_quantity: Optional[
        Decimal
    ] = field(
        default=None,
        metadata={
            "name": "flowBasedStudy_Domain.flowBasedMargin_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    flow_based_study_domain_flow_based_margin_quantity_quality: Optional[
        QualityTypeList
    ] = field(
        default=None,
        metadata={
            "name": "flowBasedStudy_Domain.flowBasedMargin_Quantity.quality",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    market_coupling_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "marketCoupling_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    market_coupling_domain_shadow_price_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "marketCoupling_Domain.shadow_Price.amount",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "total_digits": 17,
        },
    )
    ptdf_domain: list[PtdfDomain] = field(
        default_factory=list,
        metadata={
            "name": "PTDF_Domain",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )


class ConstraintTimeSeries(BaseModel):
    class Meta:
        name = "Constraint_TimeSeries"

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
            "max_length": 35,
        }
    )
    business_type: BusinessTypeList = field(
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    quantity_measurement_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "quantity_Measurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    external_constraint_quantity_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "externalConstraint_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    external_constraint_quantity_quality: Optional[QualityTypeList] = field(
        default=None,
        metadata={
            "name": "externalConstraint_Quantity.quality",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    p_tdf_measurement_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "pTDF_Measurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    shadow_price_measurement_unit_name: Optional[UnitOfMeasureTypeList] = (
        field(
            default=None,
            metadata={
                "name": "shadowPrice_Measurement_Unit.name",
                "type": "Element",
                "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            },
        )
    )
    currency_unit_name: Optional[CurrencyTypeList] = field(
        default=None,
        metadata={
            "name": "currency_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    party_market_participant: list[PartyMarketParticipant] = field(
        default_factory=list,
        metadata={
            "name": "Party_MarketParticipant",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "min_occurs": 1,
        },
    )
    outage_registered_resource: list[OutageRegisteredResource] = field(
        default_factory=list,
        metadata={
            "name": "Outage_RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    remedial_action_registered_resource: list[
        RemedialActionRegisteredResource
    ] = field(
        default_factory=list,
        metadata={
            "name": "RemedialAction_RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    monitored_registered_resource: list[MonitoredRegisteredResource] = field(
        default_factory=list,
        metadata={
            "name": "Monitored_RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )


class Point(BaseModel):
    model_config = ConfigDict(defer_build=True)
    position: int = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )
    constraint_time_series: list[ConstraintTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "Constraint_TimeSeries",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
        }
    )
    resolution: XmlDuration = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
        }
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "min_occurs": 1,
        },
    )


class TimeSeries(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
            "max_length": 35,
        }
    )
    business_type: BusinessTypeList = field(
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
        }
    )
    in_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    out_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )
    curve_type: CurveTypeList = field(
        metadata={
            "name": "curveType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "required": True,
        }
    )
    period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
            "min_occurs": 1,
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0",
        },
    )


class CriticalNetworkElementMarketDocument(BaseModel):
    class Meta:
        name = "CriticalNetworkElement_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-n:criticalnetworkelementdocument:1:0"

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

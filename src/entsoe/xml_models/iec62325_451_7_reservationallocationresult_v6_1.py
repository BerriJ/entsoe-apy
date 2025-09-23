from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDuration
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    BusinessTypeList,
    CodingSchemeTypeList,
    ContractTypeList,
    CurrencyTypeList,
    DirectionTypeList,
    MessageTypeList,
    ProcessTypeList,
    ReasonCodeTypeList,
    RoleTypeList,
    UnitOfMeasureTypeList,
)

__NAMESPACE__ = (
    "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1"
)


class AttributeInstanceComponent(BaseModel):
    model_config = ConfigDict(defer_build=True)
    position: int = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )


class Auction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
            "max_length": 60,
        }
    )


class BidTimeSeries(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
            "max_length": 60,
        }
    )


class ConstraintDuration(BaseModel):
    model_config = ConfigDict(defer_build=True)
    duration: XmlDuration = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )


class EsmpDateTimeInterval(BaseModel):
    class Meta:
        name = "ESMP_DateTimeInterval"

    model_config = ConfigDict(defer_build=True)
    start: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )
    end: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )


class Price(BaseModel):
    model_config = ConfigDict(defer_build=True)
    amount: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
            "total_digits": 17,
        }
    )


class Quantity(BaseModel):
    model_config = ConfigDict(defer_build=True)
    quantity: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
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


class ContractMarketAgreement(BaseModel):
    class Meta:
        name = "Contract_MarketAgreement"

    model_config = ConfigDict(defer_build=True)
    type_value: ContractTypeList = field(
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
            "max_length": 60,
        }
    )
    created_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "createdDateTime",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)",
        },
    )


class CurrencyUnit(BaseModel):
    class Meta:
        name = "Currency_Unit"

    model_config = ConfigDict(defer_build=True)
    name: CurrencyTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )


class FlowDirection(BaseModel):
    model_config = ConfigDict(defer_build=True)
    direction: DirectionTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )


class MarketRole(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type_value: RoleTypeList = field(
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )


class MeasureUnit(BaseModel):
    class Meta:
        name = "Measure_Unit"

    model_config = ConfigDict(defer_build=True)
    name: UnitOfMeasureTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
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


class Process(BaseModel):
    model_config = ConfigDict(defer_build=True)
    process_type: ProcessTypeList = field(
        metadata={
            "name": "processType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )


class Reason(BaseModel):
    model_config = ConfigDict(defer_build=True)
    code: ReasonCodeTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
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


class TimePeriod(BaseModel):
    class Meta:
        name = "Time_Period"

    model_config = ConfigDict(defer_build=True)
    time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )


class Domain(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: AreaIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )


class MarketParticipant(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: PartyIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )
    market_role: MarketRole = field(
        metadata={
            "name": "MarketRole",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )


class Point(BaseModel):
    model_config = ConfigDict(defer_build=True)
    position: int = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )
    quantity: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )
    price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    secondary_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "secondaryQuantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    bid_price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "Bid_Price",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    bid_energy_price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "BidEnergy_Price",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    energy_price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "Energy_Price",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )


class RegisteredResource(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )


class TenderingMarketParticipant(BaseModel):
    class Meta:
        name = "Tendering_MarketParticipant"

    model_config = ConfigDict(defer_build=True)
    m_rid: PartyIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )


class OriginalMarketDocument(BaseModel):
    class Meta:
        name = "Original_MarketDocument"

    model_config = ConfigDict(defer_build=True)
    m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "max_length": 60,
        },
    )
    revision_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "revisionNumber",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "pattern": r"[1-9]([0-9]){0,2}",
        },
    )
    bid_bid_time_series: Optional[BidTimeSeries] = field(
        default=None,
        metadata={
            "name": "Bid_BidTimeSeries",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    tendering_market_participant: TenderingMarketParticipant = field(
        metadata={
            "name": "Tendering_MarketParticipant",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )
    resolution: XmlDuration = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "min_occurs": 1,
        },
    )


class TimeSeries(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
            "max_length": 60,
        }
    )
    bid_original_market_document: OriginalMarketDocument = field(
        metadata={
            "name": "Bid_Original_MarketDocument",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )
    auction: Auction = field(
        metadata={
            "name": "Auction",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )
    business_type: BusinessTypeList = field(
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )
    acquiring_domain: Domain = field(
        metadata={
            "name": "Acquiring_Domain",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )
    connecting_domain: Domain = field(
        metadata={
            "name": "Connecting_Domain",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )
    market_agreement: ContractMarketAgreement = field(
        metadata={
            "name": "MarketAgreement",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )
    quantity_measure_unit: MeasureUnit = field(
        metadata={
            "name": "Quantity_Measure_Unit",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )
    currency_unit: Optional[CurrencyUnit] = field(
        default=None,
        metadata={
            "name": "Currency_Unit",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    price_measure_unit: Optional[MeasureUnit] = field(
        default=None,
        metadata={
            "name": "Price_Measure_Unit",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    energy_measurement_unit: Optional[MeasureUnit] = field(
        default=None,
        metadata={
            "name": "Energy_Measurement_Unit",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    registered_resource: Optional[RegisteredResource] = field(
        default=None,
        metadata={
            "name": "RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    flow_direction: FlowDirection = field(
        metadata={
            "name": "FlowDirection",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "required": True,
        }
    )
    minimum_activation_quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "MinimumActivation_Quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    step_increment_quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "StepIncrement_Quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    order_number_attribute_instance_component: Optional[
        AttributeInstanceComponent
    ] = field(
        default=None,
        metadata={
            "name": "OrderNumber_AttributeInstanceComponent",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    activation_constraint_duration: Optional[ConstraintDuration] = field(
        default=None,
        metadata={
            "name": "Activation_ConstraintDuration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    resting_constraint_duration: Optional[ConstraintDuration] = field(
        default=None,
        metadata={
            "name": "Resting_ConstraintDuration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    minimum_constraint_duration: Optional[ConstraintDuration] = field(
        default=None,
        metadata={
            "name": "Minimum_ConstraintDuration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    maximum_constraint_duration: Optional[ConstraintDuration] = field(
        default=None,
        metadata={
            "name": "Maximum_ConstraintDuration",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )
    period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
            "min_occurs": 1,
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1",
        },
    )


class ReserveAllocationResultMarketDocument(BaseModel):
    class Meta:
        name = "ReserveAllocationResult_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-7:reserveallocationresultdocument:6:1"

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
    process: Optional[Process] = field(
        default=None,
        metadata={
            "name": "Process",
            "type": "Element",
        },
    )
    sender_market_participant: MarketParticipant = field(
        metadata={
            "name": "Sender_MarketParticipant",
            "type": "Element",
            "required": True,
        }
    )
    receiver_market_participant: MarketParticipant = field(
        metadata={
            "name": "Receiver_MarketParticipant",
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
    reserve_bid_period: TimePeriod = field(
        metadata={
            "name": "ReserveBid_Period",
            "type": "Element",
            "required": True,
        }
    )
    domain: Domain = field(
        metadata={
            "name": "Domain",
            "type": "Element",
            "required": True,
        }
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

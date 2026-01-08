from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDateTime, XmlDuration
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    BusinessTypeList,
    CodingSchemeTypeList,
    ContractTypeList,
    CurveTypeList,
    DirectionTypeList,
    EnergyProductTypeList,
    FlowCommodityOptionTypeList,
    MessageTypeList,
    ObjectAggregationTypeList,
    ProcessTypeList,
    QualityTypeList,
    ReasonCodeTypeList,
    RoleTypeList,
    UnitOfMeasureTypeList,
)

__NAMESPACE__ = "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1"


class EsmpDateTimeInterval(BaseModel):
    class Meta:
        name = "ESMP_DateTimeInterval"

    model_config = ConfigDict(defer_build=True)
    start: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )
    end: str = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "required": True,
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )


class Reading(BaseModel):
    model_config = ConfigDict(defer_build=True)
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    time_stamp: Optional[str] = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)",
        },
    )
    tou_tier_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "touTierName",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    value_missing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "valueMissing",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "required": True,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
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
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "required": True,
        }
    )


class AccountingPoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: Optional[MeasurementPointIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    flow_commodity_option: Optional[FlowCommodityOptionTypeList] = field(
        default=None,
        metadata={
            "name": "flowCommodityOption",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    connection_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "connectionCategory",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    usage_point_location_geo_info_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "usagePointLocation.geoInfoReference",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )


class ExchangePoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: Optional[MeasurementPointIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )


class MarketParticipant(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: PartyIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "required": True,
        }
    )
    market_role_type: RoleTypeList = field(
        metadata={
            "name": "marketRole.type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "required": True,
        }
    )


class MeterReading(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    readings: list[Reading] = field(
        default_factory=list,
        metadata={
            "name": "Readings",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )


class Point(BaseModel):
    model_config = ConfigDict(defer_build=True)
    position: int = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )
    quantity: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "required": True,
        }
    )
    quality: Optional[QualityTypeList] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    delta_quantity_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "delta_Quantity.quantity",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )


class RegisteredResource(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "required": True,
        }
    )


class SeriesPeriod(BaseModel):
    class Meta:
        name = "Series_Period"

    model_config = ConfigDict(defer_build=True)
    resolution: XmlDuration = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "required": True,
        }
    )
    time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "required": True,
        }
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "min_occurs": 1,
        },
    )


class TimeSeries(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "required": True,
            "max_length": 60,
        }
    )
    original_market_document_m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "original_MarketDocument.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "max_length": 60,
        },
    )
    original_transaction_series_m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "originalTransaction_Series.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "max_length": 60,
        },
    )
    business_type: BusinessTypeList = field(
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "required": True,
        }
    )
    object_aggregation: Optional[ObjectAggregationTypeList] = field(
        default=None,
        metadata={
            "name": "objectAggregation",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    product: EnergyProductTypeList = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "required": True,
        }
    )
    accounting_point: list[AccountingPoint] = field(
        default_factory=list,
        metadata={
            "name": "AccountingPoint",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    exchange_point: list[ExchangePoint] = field(
        default_factory=list,
        metadata={
            "name": "ExchangePoint",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    in_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    out_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    market_agreement_m_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "marketAgreement.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "max_length": 60,
        },
    )
    market_agreement_type: Optional[ContractTypeList] = field(
        default=None,
        metadata={
            "name": "marketAgreement.type",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    accounting_point_party_market_participant: list[MarketParticipant] = field(
        default_factory=list,
        metadata={
            "name": "AccountingPointParty_MarketParticipant",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    registered_resource: list[RegisteredResource] = field(
        default_factory=list,
        metadata={
            "name": "RegisteredResource",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    registration_date_and_or_time_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "registration_DateAndOrTime.dateTime",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    flow_direction_direction: Optional[DirectionTypeList] = field(
        default=None,
        metadata={
            "name": "flowDirection.direction",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    measurement_unit_name: Optional[UnitOfMeasureTypeList] = field(
        default=None,
        metadata={
            "name": "measurement_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    curve_type: CurveTypeList = field(
        metadata={
            "name": "curveType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "required": True,
        }
    )
    period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
            "min_occurs": 1,
        },
    )
    meter_reading: list[MeterReading] = field(
        default_factory=list,
        metadata={
            "name": "MeterReading",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1",
        },
    )


class MeasurementDataMarketDocument(BaseModel):
    class Meta:
        name = "MeasurementData_MarketDocument"
        namespace = (
            "urn:iec62325.351:tc57wg16:451-n:measurementdatadocument:1:1"
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
    revision_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "revisionNumber",
            "type": "Element",
            "pattern": r"[1-9]([0-9]){0,2}",
        },
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
    domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "domain.mRID",
            "type": "Element",
        },
    )
    period: TimePeriod = field(
        metadata={
            "name": "Period",
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

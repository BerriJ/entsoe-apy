from __future__ import annotations

from decimal import Decimal

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

__NAMESPACE__ = "https://cim4.eu/esmp/ns/measurementdatadocument/1-2"


class EsmpDateTimeInterval(BaseModel):
    class Meta:
        name = "ESMP_DateTimeInterval"

    model_config = ConfigDict(defer_build=True)
    start: str = field(
        metadata={
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )
    end: str = field(
        metadata={
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)",
        }
    )


class Reading(BaseModel):
    model_config = ConfigDict(defer_build=True)
    position: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    value: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    time_stamp: None | str = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)",
        },
    )
    tou_tier_name: None | str = field(
        default=None,
        metadata={
            "name": "touTierName",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    value_missing: None | bool = field(
        default=None,
        metadata={
            "name": "valueMissing",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
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


class MeasurementPointIdString(BaseModel):
    class Meta:
        name = "MeasurementPointID_String"

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
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        }
    )
    text: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
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


class TimePeriod(BaseModel):
    class Meta:
        name = "Time_Period"

    model_config = ConfigDict(defer_build=True)
    time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        }
    )


class AccountingPoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: None | MeasurementPointIdString = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    flow_commodity_option: None | FlowCommodityOptionTypeList = field(
        default=None,
        metadata={
            "name": "flowCommodityOption",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    connection_category: None | str = field(
        default=None,
        metadata={
            "name": "connectionCategory",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    usage_point_location_geo_info_reference: None | str = field(
        default=None,
        metadata={
            "name": "usagePointLocation.geoInfoReference",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )


class ExchangePoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: MeasurementPointIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        }
    )


class MarketParticipant(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: PartyIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        }
    )
    market_role_type: None | RoleTypeList = field(
        default=None,
        metadata={
            "name": "marketRole.type",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )


class MeterReading(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: None | ResourceIdString = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    readings: list[Reading] = field(
        default_factory=list,
        metadata={
            "name": "Readings",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )


class Point(BaseModel):
    model_config = ConfigDict(defer_build=True)
    position: int = field(
        metadata={
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )
    quantity: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    quality: None | QualityTypeList = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    delta_quantity_quantity: None | Decimal = field(
        default=None,
        metadata={
            "name": "delta_Quantity.quantity",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )


class RegisteredResource(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: ResourceIdString = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        }
    )


class SeriesPeriod(BaseModel):
    class Meta:
        name = "Series_Period"

    model_config = ConfigDict(defer_build=True)
    resolution: XmlDuration = field(
        metadata={
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        }
    )
    time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        }
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
            "min_occurs": 1,
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )


class TimeSeries(BaseModel):
    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
            "max_length": 60,
        }
    )
    business_type: None | BusinessTypeList = field(
        default=None,
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    product: None | EnergyProductTypeList = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    object_aggregation: None | ObjectAggregationTypeList = field(
        default=None,
        metadata={
            "name": "objectAggregation",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    curve_type: None | CurveTypeList = field(
        default=None,
        metadata={
            "name": "curveType",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    in_domain_m_rid: None | AreaIdString = field(
        default=None,
        metadata={
            "name": "in_Domain.mRID",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    out_domain_m_rid: None | AreaIdString = field(
        default=None,
        metadata={
            "name": "out_Domain.mRID",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    domain_m_rid: None | AreaIdString = field(
        default=None,
        metadata={
            "name": "domain.mRID",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    original_market_document_m_rid: None | str = field(
        default=None,
        metadata={
            "name": "original_MarketDocument.mRID",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
            "max_length": 60,
        },
    )
    market_agreement_m_rid: None | str = field(
        default=None,
        metadata={
            "name": "marketAgreement.mRID",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
            "max_length": 60,
        },
    )
    market_agreement_type: None | ContractTypeList = field(
        default=None,
        metadata={
            "name": "marketAgreement.type",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    accounting_point_party_market_participant: list[MarketParticipant] = field(
        default_factory=list,
        metadata={
            "name": "AccountingPointParty_MarketParticipant",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    period: list[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
            "min_occurs": 1,
        },
    )
    original_transaction_series_m_rid: None | str = field(
        default=None,
        metadata={
            "name": "originalTransaction_Series.mRID",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
            "max_length": 60,
        },
    )
    measurement_unit_name: None | UnitOfMeasureTypeList = field(
        default=None,
        metadata={
            "name": "measurement_Unit.name",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    registration_date_and_or_time_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "registration_DateAndOrTime.dateTime",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    accounting_point: list[AccountingPoint] = field(
        default_factory=list,
        metadata={
            "name": "AccountingPoint",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    reason: list[Reason] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    meter_reading: list[MeterReading] = field(
        default_factory=list,
        metadata={
            "name": "MeterReading",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    flow_direction_direction: None | DirectionTypeList = field(
        default=None,
        metadata={
            "name": "flowDirection.direction",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    exchange_point: list[ExchangePoint] = field(
        default_factory=list,
        metadata={
            "name": "ExchangePoint",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )
    registered_resource: list[RegisteredResource] = field(
        default_factory=list,
        metadata={
            "name": "RegisteredResource",
            "type": "Element",
            "namespace": "https://cim4.eu/esmp/ns/measurementdatadocument/1-2",
        },
    )


class MeasurementDataMarketDocument(BaseModel):
    class Meta:
        name = "MeasurementData_MarketDocument"
        namespace = "https://cim4.eu/esmp/ns/measurementdatadocument/1-2"

    model_config = ConfigDict(defer_build=True)
    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "max_length": 60,
        }
    )
    revision_number: None | str = field(
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
        }
    )
    process_process_type: None | ProcessTypeList = field(
        default=None,
        metadata={
            "name": "process.processType",
            "type": "Element",
        },
    )
    sender_market_participant: None | MarketParticipant = field(
        default=None,
        metadata={
            "name": "Sender_MarketParticipant",
            "type": "Element",
        },
    )
    receiver_market_participant: None | MarketParticipant = field(
        default=None,
        metadata={
            "name": "Receiver_MarketParticipant",
            "type": "Element",
        },
    )
    created_date_time: str = field(
        metadata={
            "name": "createdDateTime",
            "type": "Element",
            "pattern": r"((([0-9]{4})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])Z)",
        }
    )
    domain_m_rid: None | AreaIdString = field(
        default=None,
        metadata={
            "name": "domain.mRID",
            "type": "Element",
        },
    )
    period: None | TimePeriod = field(
        default=None,
        metadata={
            "name": "Period",
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

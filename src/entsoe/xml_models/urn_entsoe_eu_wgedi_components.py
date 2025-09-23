from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlTime
from xsdata_pydantic.fields import field

from .urn_entsoe_eu_wgedi_codelists import (
    AllocationModeTypeList,
    AssetTypeList,
    AuctionTypeList,
    BusinessTypeList,
    CategoryTypeList,
    ClassificationTypeList,
    CodingSchemeType,
    ContractTypeList,
    CurrencyTypeList,
    CurveTypeList,
    DirectionTypeList,
    DocumentTypeList,
    EicTypeList,
    EnergyProductTypeList,
    IndicatorTypeList,
    ObjectAggregationTypeList,
    PaymentTermsTypeList,
    PriceCategoryTypeList,
    PriceDirectionTypeList,
    ProcessTypeList,
    QualityTypeList,
    ReasonCodeTypeList,
    RightsTypeList,
    RoleTypeList,
    StatusTypeList,
    TarifTypeTypeList,
    UnitOfMeasureTypeList,
)

__NAMESPACE__ = "urn:entsoe.eu:wgedi:components"


class AmountType(BaseModel):
    """
    <Uid xmlns="">ET0022</Uid> <Definition xmlns="">The monetary value of an
    object</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: Decimal = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "total_digits": 17,
        }
    )


class CodeType(BaseModel):
    """
    <Uid xmlns="">ET0023</Uid> <Definition xmlns="">the coded representation of an
    object.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 3,
        }
    )


class ComponentNameType(BaseModel):
    """
    <Uid xmlns="">ET0046</Uid> <Definition xmlns="">The identification of an
    attribute for a given Component.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 70,
        }
    )


class DateTimeType(BaseModel):
    """<Uid xmlns="">ET0044</Uid> <Definition xmlns="">Date and time of a given
    time point.

    The time must be expressed in UTC as: YYYY-MM-DDTHH:MM:SSZ</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class DateType(BaseModel):
    """
    <Uid xmlns="">ET0035</Uid> <Definition xmlns=""> The gregorian date   that must
    be expressed as: YYYY-MM-DD</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: XmlDate = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class DocumentDateTimeType(BaseModel):
    """<Uid xmlns="">ET0006</Uid> <Definition xmlns=""> (Synonym "Message Date
    Time") Date and time of the preparation of a document.

    The time must be expressed in UTC as: YYYY-MM-DDTHH:MM:SSZ</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class IdentificationType(BaseModel):
    """
    <Uid xmlns="">ET0001</Uid> <Definition xmlns="">A code to uniquely distinguish
    one occurrence of an entity from another</Definition>.
    """

    model_config = ConfigDict(defer_build=True)
    v: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 35,
        }
    )


class LongIdentificationType(BaseModel):
    """
    <Uid xmlns="">ET0043</Uid> <Definition xmlns="">A code to uniquely distinguish
    one occurrence of an entity from another with a long identifier</Definition>.
    """

    model_config = ConfigDict(defer_build=True)
    v: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 150,
        }
    )


class PositionType(BaseModel):
    """
    <Uid xmlns="">ET0021</Uid> <Definition xmlns="">(Synonym "pos") A sequential
    value representing the relative position of an entity within a space such as a
    time interval</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )


class QuantityType(BaseModel):
    """<Uid xmlns="">ET0012</Uid> <Definition xmlns="">(Synonym "qty") The quantity
    of an energy product.

    Positive quantities shall not have a sign.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: Decimal = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class ReasonTextType(BaseModel):
    """
    <Uid xmlns="">ET0016</Uid> <Definition xmlns="">The textual explanation of an
    act.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 512,
        }
    )


class ResolutionType(BaseModel):
    """<Uid xmlns="">ET0019</Uid> <Definition xmlns="">Defines the number of units
    of time that compose an individual step within a period.

    The resolution is expressed in compliance with ISO 8601 in the
    following format:PnYnMnDTnHnMnS.Where nY expresses a number of
    years, nM a number of months, nD a number of days.The letter "T"
    separates the date expression from the time expression and after it
    nH identifies a number of hours, nM a number of minutes and nS a
    number of seconds.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: XmlDuration = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class TextType(BaseModel):
    """
    <Uid xmlns="">ET0032</Uid> <Definition xmlns="">A textual string</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 700,
        }
    )


class TimeIntervalType(BaseModel):
    """<Uid xmlns="">ET0007</Uid> <Definition xmlns="">The start date and time and
    the end date and time of an event.

    The time interval must be expressed in a form respecting ISO 8601 : YYYY-MM-DDTHH:MMZ/YYYY-MM-DDTHH:MMZ.ISO 8601 rules for reduction may apply. The time must always be expressed in UTC.</Definition>

    :ivar v: ISO 8601 time intervals are always expressed in the form
        yyyy-mm-ddThh:mmZ/yyyy-mm-ddThh:mmZ Note: The minimum XML form
        of dateTime is yyyy-mm-ddThh:mm:ssZ
    """

    model_config = ConfigDict(defer_build=True)
    v: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"(((((20[0-9]{2})[\-](0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z/)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z/)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z/))(((([0-9]{4})-(0[13578]|1[02])[\-](0[1-9]|[12][0-9]|3[01])|([0-9]{4})[\-]((0[469])|(11))[\-](0[1-9]|[12][0-9]|30))T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][048]|[13579][01345789](0)[48]|[13579][01345789][2468][048]|[02468][048][02468][048]|[02468][1235679](0)[48]|[02468][1235679][2468][048]|[0-9][0-9][13579][26])[\-](02)[\-](0[1-9]|1[0-9]|2[0-9])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)|(([13579][26][02468][1235679]|[13579][01345789](0)[01235679]|[13579][01345789][2468][1235679]|[02468][048][02468][1235679]|[02468][1235679](0)[01235679]|[02468][1235679][2468][1235679]|[0-9][0-9][13579][01345789])[\-](02)[\-](0[1-9]|1[0-9]|2[0-8])T(([01][0-9]|2[0-3]):[0-5][0-9])Z)))",
        }
    )


class TimeType(BaseModel):
    """
    <Uid xmlns="">ET0033</Uid> <Definition xmlns=""> The time within a 24 hour day
    that must be expressed as: HH:MM:SS</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: XmlTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class VersionType(BaseModel):
    """<Uid xmlns="">ET0002</Uid> <Definition xmlns="">A code that distinguishes
    one evolution of an identified object from another.

    Information about a specific object may be sent several times, each
    transmission being identified by a different version
    number.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999,
        }
    )


class AllocationModeType(BaseModel):
    """
    <Uid xmlns="">ET0040</Uid> <Definition xmlns="">Identification of the method of
    allocation in an auction.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: AllocationModeTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class AreaType(BaseModel):
    """
    <Uid xmlns="">ET0009</Uid> <Definition xmlns="">A domain covering a number of
    related objects, such as balance area, grid area, etc.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 18,
        }
    )
    coding_scheme: CodingSchemeType = field(
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
            "required": True,
        }
    )


class AssetType(BaseModel):
    """
    <Uid xmlns="">ET0031</Uid> <Definition xmlns="">Identification of the type of
    asset </Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: AssetTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class AuctionType(BaseModel):
    """
    <Uid xmlns="">ET0030</Uid> <Definition xmlns="">The coded representation of
    different types of auction.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: AuctionTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class BusinessType(BaseModel):
    """<Uid xmlns="">ET0017</Uid> <Definition xmlns="">The exact business nature
    identifying the principal characteristic of a time series.

    </Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: BusinessTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class CategoryType(BaseModel):
    """
    <Uid xmlns="">ET0037</Uid> <Definition xmlns="">The product category of an
    auction.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: CategoryTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class ClassificationType(BaseModel):
    """<Uid xmlns="">ET0013 </Uid> <Definition xmlns="">Indicates the
    classification mechanism used to group a set of objects together.

    The grouping may be of a detailed or a summary nature</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: ClassificationTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class ComponentValueType(BaseModel):
    """
    <Uid xmlns="">ET0047</Uid> <Definition xmlns="">The value of a given
    component.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 150,
        }
    )
    coding_scheme: Optional[CodingSchemeType] = field(
        default=None,
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
        },
    )


class ContractType(BaseModel):
    """<Uid xmlns="">ET0010</Uid> <Definition xmlns="">The contract type defines
    the conditions under which the capacity is allocated and handled.

    EG: daily auction, weekly auction, monthly auction, yearly auction, etc. The significance of this type is dependent on area specific coded working methods</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: ContractTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class CurrencyType(BaseModel):
    """
    <Uid xmlns="">ET0024 </Uid> <Definition xmlns="">The coded identification of
    legal tender using ISO 4217 3 alpha codes</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: CurrencyTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class CurveType(BaseModel):
    """
    <Uid xmlns="">ET0042</Uid> <Definition xmlns="">The type of curve being defined
    in the time series.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: CurveTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class DirectionType(BaseModel):
    """<Uid xmlns="">ET0026</Uid> <Definition xmlns="">The coded identification of
    the direction of energy flow.

    </Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: DirectionTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class DocumentType(BaseModel):
    """<Uid xmlns="">ET0003 </Uid> <Definition xmlns=""> (Synonym "Document Type")
    The coded type of a document.

    The document type describes the principal characteristic of a
    document. note this code is decrecated and should no longer be used
    in new messages (use documentType instead))</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: DocumentTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class EicType(BaseModel):
    """<Uid xmlns="">ET0028</Uid> <Definition xmlns="">The coded identification of
    the type of an EIC code.

    </Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: EicTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class EnergyProductType(BaseModel):
    """
    <Uid xmlns="">ET0008 </Uid> <Definition xmlns="">The identification of the
    nature of an energy product such as Power, energy, reactive power,
    etc.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: EnergyProductTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class IndicatorType(BaseModel):
    """
    <Uid xmlns="">ET0029</Uid> <Definition xmlns="">A boolean indicator to express
    Yes or No or True or False</Definition>.
    """

    model_config = ConfigDict(defer_build=True)
    v: IndicatorTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class LineType(BaseModel):
    """
    <Uid xmlns="">ET0050</Uid> <Definition xmlns="">the identification of a line
    that may be physical or virtual.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 35,
        }
    )
    coding_scheme: CodingSchemeType = field(
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
            "required": True,
        }
    )


class MessageType(BaseModel):
    """<Uid xmlns="">ET0045 </Uid> <Definition xmlns=""> (Synonym "Document Type")
    The coded type of a document.

    The document type describes the principal characteristic of a
    document</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: DocumentTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class MeteringPointType(BaseModel):
    """
    <Uid xmlns="">ET0027</Uid> <Definition xmlns="">A domain covering a number of
    related objects, such as metering point and accounting point, etc.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 35,
        }
    )
    coding_scheme: CodingSchemeType = field(
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
            "required": True,
        }
    )


class ObjectAggregationType(BaseModel):
    """
    <Uid xmlns="">ET0018</Uid> <Definition xmlns="">The identification of the
    domain that is the common dominator used to aggregate a time
    series.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: ObjectAggregationTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class PartyType(BaseModel):
    """
    <Uid xmlns="">ET0014</Uid> <Definition xmlns="">The identification of an actor
    in the Energy market.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 16,
        }
    )
    coding_scheme: CodingSchemeType = field(
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
            "required": True,
        }
    )


class PaymentTermsType(BaseModel):
    """
    <Uid xmlns="">ET0041</Uid> <Definition xmlns="">The terms which dictate the
    determination of the bid payment price.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: PaymentTermsTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class PriceCategory(BaseModel):
    """<Uid xmlns="">ET0048</Uid> <Definition xmlns="">The category of a price to
    be used in a price calculation.

    Note: the price category is mutually agreed between System Operators</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: PriceCategoryTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class PriceDirection(BaseModel):
    """
    <Uid xmlns="">ET0049</Uid> <Definition xmlns="">The nature of a price (i.e.an
    Impacted Area System Operator pays to internal Market Parties or
    inverse).</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: PriceDirectionTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class ProcessType(BaseModel):
    """
    <Uid xmlns="">ET0020</Uid> <Definition xmlns="">Indicates the nature of process
    that the document addresses.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: ProcessTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class QualityType(BaseModel):
    """
    <Uid xmlns="">ET0036</Uid> <Definition xmlns="">The quality of an
    object.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: QualityTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class ReasonCodeType(BaseModel):
    """
    <Uid xmlns="">ET0015 </Uid> <Definition xmlns="">The coded motivation of an
    act.</Definition>&gt;
    """

    model_config = ConfigDict(defer_build=True)
    v: ReasonCodeTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class ResourceObjectType(BaseModel):
    """
    <Uid xmlns="">ET0034</Uid> <Definition xmlns="">The identification of a
    resource object in the Energy market.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 18,
        }
    )
    coding_scheme: CodingSchemeType = field(
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
            "required": True,
        }
    )


class RightsType(BaseModel):
    """
    <Uid xmlns="">ET0038</Uid> <Definition xmlns="">The rights of use that is
    accorded to what is acquired in an auction..</Definition>&gt;
    """

    model_config = ConfigDict(defer_build=True)
    v: RightsTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class RoleType(BaseModel):
    """<Uid xmlns="">ET0005</Uid> <Definition xmlns="">Identification of the role
    played by a party.

    </Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: RoleTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class StatusType(BaseModel):
    """
    <Uid xmlns="">ET0025</Uid> <Definition xmlns="">The condition or position of an
    object with regard to its standing.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: StatusTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class TarifTypeType(BaseModel):
    """
    <Uid xmlns="">ET0039</Uid> <Definition xmlns="">The standard tarif types as
    defined in the UCTE policies.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: TarifTypeTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class UnitOfMeasureType(BaseModel):
    """<Uid xmlns="">ET0011</Uid> <Definition xmlns="">(synonym MeasurementUnit)
    The unit of measure that is applied to a quantity.

    The measurement units shall be in compliance with UN/ECE
    Recommendation 20.</Definition>
    """

    model_config = ConfigDict(defer_build=True)
    v: UnitOfMeasureTypeList = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

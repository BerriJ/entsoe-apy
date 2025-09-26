"""Base parameter classes for ENTSO-E Transparency Platform API."""

from typing import Any, Dict, Optional

from pydantic import BaseModel

from ..query.query_api import query_api
from ..utils.mappings_dict import mappings


class ValidationError(ValueError):
    """Custom exception for parameter validation errors."""

    pass


class Base:
    """Base class for ENTSO-E Transparency Platform query parameters."""

    # Maximum days for date range queries (can be overridden by subclasses)
    max_days_limit: int = 365

    def __init__(
        self,
        document_type: str,
        period_start: Optional[int] = None,
        period_end: Optional[int] = None,
        offset: int | None = None,
    ):
        """
        Initialize base parameters for ENTSO-E Transparency Platform queries.

        Args:
            document_type: Document type identifier
            period_start: Start period (YYYYMMDDHHMM format, optional)
            period_end: End period (YYYYMMDDHHMM format, optional)
            offset: Offset for pagination

        Raises:
            ValidationError: If any input parameter is invalid


        """

        # Initialize the base parameters dictionary
        self.params: Dict[str, Any] = {
            "documentType": document_type,
        }

        # Add period parameters using the proper method
        self.add_period_params(period_start=period_start, period_end=period_end)

        if offset is not None:
            self.add_optional_param("offset", offset)

    def validate_eic_code(self, eic_code: Optional[str], parameter_name: str) -> None:
        """
        Validate EIC code against the mappings dictionary.

        Args:
            eic_code: The EIC code to validate
            parameter_name: Name of the parameter for error messages

        Raises:
            ValidationError: If the EIC code is not found in mappings
        """
        if eic_code is None:
            return

        if eic_code not in mappings:
            raise ValidationError(
                f"Invalid EIC code '{eic_code}' for parameter '{parameter_name}'. "
                f"EIC code not found in mappings."
            )

    def add_optional_param(self, key: str, value: Any) -> None:
        """
        Add an optional parameter to the params dictionary if value is not None.

        Args:
            key: Parameter key
            value: Parameter value
        """
        if value is not None:
            self.params[key] = value

    def add_domain_params(
        self,
        in_domain: Optional[str] = None,
        out_domain: Optional[str] = None,
        domain_mrid: Optional[str] = None,
        bidding_zone_domain: Optional[str] = None,
        out_bidding_zone_domain: Optional[str] = None,
        acquiring_domain: Optional[str] = None,
        connecting_domain: Optional[str] = None,
        control_area_domain: Optional[str] = None,
        area_domain: Optional[str] = None,
        domain: Optional[str] = None,
    ) -> None:
        """
        Add domain-related parameters to the params dictionary.

        Args:
            in_domain: Input domain/bidding zone (EIC code)
            out_domain: Output domain/bidding zone (EIC code)
            domain_mrid: Domain mRID for specific queries (EIC code)
            bidding_zone_domain: Bidding zone domain (EIC code)
            out_bidding_zone_domain: Output bidding zone domain (EIC code)
            acquiring_domain: Acquiring domain (EIC code)
            connecting_domain: Connecting domain (EIC code)
            control_area_domain: Control area domain (EIC code)
            area_domain: Area domain (EIC code)
            domain: Domain (EIC code)
        """
        # Validate EIC codes before adding them
        self.validate_eic_code(in_domain, "in_domain")
        self.validate_eic_code(out_domain, "out_domain")
        self.validate_eic_code(domain_mrid, "domain_mrid")
        self.validate_eic_code(bidding_zone_domain, "bidding_zone_domain")
        self.validate_eic_code(out_bidding_zone_domain, "out_bidding_zone_domain")
        self.validate_eic_code(acquiring_domain, "acquiring_domain")
        self.validate_eic_code(connecting_domain, "connecting_domain")
        self.validate_eic_code(control_area_domain, "control_area_domain")
        self.validate_eic_code(area_domain, "area_domain")
        self.validate_eic_code(domain, "domain")

        self.add_optional_param("in_Domain", in_domain)
        self.add_optional_param("out_Domain", out_domain)
        self.add_optional_param("domain.mRID", domain_mrid)
        self.add_optional_param("biddingZone_Domain", bidding_zone_domain)
        self.add_optional_param("outBiddingZone_Domain", out_bidding_zone_domain)
        self.add_optional_param("acquiring_Domain", acquiring_domain)
        self.add_optional_param("connecting_Domain", connecting_domain)
        self.add_optional_param("controlArea_Domain", control_area_domain)
        self.add_optional_param("area_Domain", area_domain)
        self.add_optional_param("Domain", domain)

    def add_business_params(
        self,
        business_type: Optional[str] = None,
        process_type: Optional[str] = None,
        psr_type: Optional[str] = None,
    ) -> None:
        """
        Add business-related parameters to the params dictionary.

        Args:
            business_type: Business type
            process_type: Process type
            psr_type: Power system resource type
        """
        self.add_optional_param("businessType", business_type)
        self.add_optional_param("processType", process_type)
        self.add_optional_param("psrType", psr_type)

    def add_market_params(
        self,
        contract_market_agreement_type: Optional[str] = None,
        auction_type: Optional[str] = None,
        auction_category: Optional[str] = None,
        type_marketplace_agreement_type: Optional[str] = None,
    ) -> None:
        """
        Add market-related parameters to the params dictionary.

        Args:
            contract_market_agreement_type: Contract market agreement type
            auction_type: Auction type
            auction_category: Auction category
            type_marketplace_agreement_type: Type marketplace agreement
        """
        self.add_optional_param(
            "contract_MarketAgreement.Type", contract_market_agreement_type
        )
        self.add_optional_param("auction.Type", auction_type)
        self.add_optional_param("auction.category", auction_category)
        self.add_optional_param(
            "type_MarketAgreement.Type", type_marketplace_agreement_type
        )

    def add_balancing_params(
        self,
        standard_market_product: Optional[str] = None,
        original_market_product: Optional[str] = None,
        direction: Optional[str] = None,
        export_type: Optional[str] = None,
    ) -> None:
        """
        Add balancing-specific parameters to the params dictionary.

        Args:
            standard_market_product: Standard market product
            original_market_product: Original market product
            direction: Direction (A01=Up, A02=Down)
            export_type: Export type (zip)
        """
        self.add_optional_param("Standard_MarketProduct", standard_market_product)
        self.add_optional_param("Original_MarketProduct", original_market_product)
        self.add_optional_param("Direction", direction)
        self.add_optional_param("ExportType", export_type)

    def add_resource_params(
        self,
        registered_resource: Optional[str] = None,
        subject_party_name: Optional[str] = None,
        subject_party_market_role: Optional[str] = None,
    ) -> None:
        """
        Add resource-related parameters to the params dictionary.

        Args:
            registered_resource: Registered resource identifier (EIC code)
            subject_party_name: Subject party name
            subject_party_market_role: Subject party market role
        """
        # Validate EIC code for registered_resource
        self.validate_eic_code(registered_resource, "registered_resource")

        self.add_optional_param("registeredResource", registered_resource)
        self.add_optional_param("subject_Party.name", subject_party_name)
        self.add_optional_param(
            "subject_Party.marketRole.type", subject_party_market_role
        )

    def add_period_params(
        self,
        period_start: Optional[int] = None,
        period_end: Optional[int] = None,
    ) -> None:
        """
        Add period parameters to the params dictionary.

        Args:
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
        """
        self.add_optional_param("periodStart", period_start)
        self.add_optional_param("periodEnd", period_end)

    def add_update_params(
        self,
        updated_date_and_or_time: Optional[str] = None,
        implementation_date_and_or_time: Optional[str] = None,
        period_start_update: Optional[int] = None,
        period_end_update: Optional[int] = None,
        time_interval_update: Optional[str] = None,
    ) -> None:
        """
        Add update-related parameters to the params dictionary.

        Args:
            updated_date_and_or_time: Updated date and/or time
            implementation_date_and_or_time: Implementation date and/or time
            period_start_update: Period start update (for outages)
            period_end_update: Period end update (for outages)
            time_interval_update: Time interval update (can be used instead of
                                period_start_update & period_end_update)
        """
        self.add_optional_param("updatedDateAndOrTime", updated_date_and_or_time)
        self.add_optional_param(
            "implementation_DateAndOrTime", implementation_date_and_or_time
        )
        self.add_optional_param("periodStartUpdate", period_start_update)
        self.add_optional_param("periodEndUpdate", period_end_update)
        self.add_optional_param("TimeIntervalUpdate", time_interval_update)

    def query_api(self) -> list[BaseModel]:
        """
        Query the ENTSO-E API with the specified parameters.

        Returns:
            List of Pydantic BaseModel instances containing the API responses.
            Multiple models may be returned when the query spans multiple time
            periods or when the API returns multiple documents in response to
            a single request. Each model preserves its associated metadata.
        """
        response = query_api(self.params, max_days_limit=self.max_days_limit)
        return response

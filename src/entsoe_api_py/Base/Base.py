"""Base parameter classes for ENTSO-E Transparency Platform API."""

from typing import Any, Dict, Optional


class Base:
    """Base class for ENTSO-E Transparency Platform query parameters."""

    def __init__(
        self,
        document_type: str,
        security_token: str,
        period_start: int,
        period_end: int,
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize base parameters for ENTSO-E Transparency Platform queries.

        Args:
            document_type: Document type identifier
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            timeout: Request timeout in seconds
            offset: Offset for pagination

        Raises:
            ValidationError: If any input parameter is invalid
        """
        # Initialize the base parameters dictionary
        self.params: Dict[str, Any] = {
            "documentType": document_type,
            "securityToken": security_token,
            "periodStart": period_start,
            "periodEnd": period_end,
        }

        # Add optional parameters if provided
        if offset is not None:
            self.params["offset"] = offset

        # Store timeout for potential use in derived classes
        self.timeout = timeout

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
    ) -> None:
        """
        Add domain-related parameters to the params dictionary.

        Args:
            in_domain: Input domain/bidding zone
            out_domain: Output domain/bidding zone
            domain_mrid: Domain mRID for specific queries
            bidding_zone_domain: Bidding zone domain
            out_bidding_zone_domain: Output bidding zone domain
            acquiring_domain: Acquiring domain
            connecting_domain: Connecting domain
            control_area_domain: Control area domain
        """
        self.add_optional_param("in_Domain", in_domain)
        self.add_optional_param("out_Domain", out_domain)
        self.add_optional_param("domain.mRID", domain_mrid)
        self.add_optional_param("biddingZone_Domain", bidding_zone_domain)
        self.add_optional_param("outBiddingZone_Domain", out_bidding_zone_domain)
        self.add_optional_param("acquiring_Domain", acquiring_domain)
        self.add_optional_param("connecting_Domain", connecting_domain)
        self.add_optional_param("controlArea_Domain", control_area_domain)

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

    def add_resource_params(
        self,
        registered_resource: Optional[str] = None,
        subject_party_name: Optional[str] = None,
        subject_party_market_role: Optional[str] = None,
    ) -> None:
        """
        Add resource-related parameters to the params dictionary.

        Args:
            registered_resource: Registered resource identifier
            subject_party_name: Subject party name
            subject_party_market_role: Subject party market role
        """
        self.add_optional_param("registeredResource", registered_resource)
        self.add_optional_param("subject_Party.name", subject_party_name)
        self.add_optional_param(
            "subject_Party.marketRole.type", subject_party_market_role
        )

    def add_update_params(
        self,
        updated_date_and_or_time: Optional[str] = None,
        implementation_date_and_or_time: Optional[str] = None,
        period_start_update: Optional[int] = None,
        period_end_update: Optional[int] = None,
    ) -> None:
        """
        Add update-related parameters to the params dictionary.

        Args:
            updated_date_and_or_time: Updated date and/or time
            implementation_date_and_or_time: Implementation date and/or time
            period_start_update: Period start update (for outages)
            period_end_update: Period end update (for outages)
        """
        self.add_optional_param("updatedDateAndOrTime", updated_date_and_or_time)
        self.add_optional_param(
            "implementation_DateAndOrTime", implementation_date_and_or_time
        )
        self.add_optional_param("periodStartUpdate", period_start_update)
        self.add_optional_param("periodEndUpdate", period_end_update)

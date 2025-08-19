from typing import Optional


class BalancingParams:
    """Balancing data parameters for ENTSO-E Transparency Platform queries."""

    def __init__(
        self,
        document_type: str,
        security_token: str,
        period_start: int,
        period_end: int,
        # Domain parameters - required based on query type
        acquiring_domain: Optional[str] = None,
        connecting_domain: Optional[str] = None,
        control_area_domain: Optional[str] = None,
        bidding_zone_domain: Optional[str] = None,
        # Optional parameters for balancing queries
        business_type: Optional[str] = None,
        process_type: Optional[str] = None,
        psr_type: Optional[str] = None,
        type_marketplace_agreement_type: Optional[str] = None,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize balancing data parameters for ENTSO-E Transparency Platform.

        Args:
            document_type: Document type (e.g., A81, A82, A83, A84, A85, A86,
                          A87, A88, A89, A90, A91, A92, A93, A95, A96, A97, B33)
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            acquiring_domain: EIC code of Market Balancing Area (acquiring area)
                            - required for cross-border balancing queries
            connecting_domain: EIC code of Market Balancing Area (connecting area)
                             - required for cross-border balancing queries
            control_area_domain: EIC code of Control Area or Market Balancing Area
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            business_type: Business type (e.g., A06, A25, A29, A46, A53, A95,
                          B05, B07, B08, B09, B10, B11, B33, B95)
            process_type: Process type (e.g., A01, A02, A16, A18, A31, A32, A33,
                         A39, A40, A44, A46, A47, A51, A52)
            psr_type: Power system resource type (A03, A04, A05, B01-B24)
            type_marketplace_agreement_type: Type marketplace agreement (A01-A07)
            timeout: Request timeout in seconds
            offset: Offset for pagination

        Raises:
            ValidationError: If any input parameter is invalid

        Notes:
            - For cross-border balancing: Use A88 document type with acquiring_domain
              and connecting_domain
            - For aggregated offers: Use A94 document type
            - For imbalance prices: Use A85 document type
            - For system imbalance volumes: Use A86 document type
            - For activated reserves: Use A96 document type
            - For procured reserves: Use A95 document type
        """
        # Build query parameters
        self.params = {
            "documentType": document_type,
            "securityToken": security_token,
            "periodStart": period_start,
            "periodEnd": period_end,
        }

        # Add domain parameters based on query type
        if acquiring_domain:
            self.params["acquiring_Domain"] = acquiring_domain
        if connecting_domain:
            self.params["connecting_Domain"] = connecting_domain
        if control_area_domain:
            self.params["controlArea_Domain"] = control_area_domain
        if bidding_zone_domain:
            self.params["biddingZone_Domain"] = bidding_zone_domain

        # Add optional parameters if provided
        if business_type:
            self.params["businessType"] = business_type
        if process_type:
            self.params["processType"] = process_type
        if psr_type:
            self.params["psrType"] = psr_type
        if type_marketplace_agreement_type:
            self.params["type_MarketAgreement.type"] = type_marketplace_agreement_type
        if offset:
            self.params["offset"] = offset

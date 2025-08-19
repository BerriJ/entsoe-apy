from typing import Optional


class TransmissionParams:
    """Transmission data parameters for ENTSO-E Transparency Platform queries."""

    def __init__(
        self,
        document_type: str,
        security_token: str,
        period_start: int,
        period_end: int,
        # Domain parameters - typically required
        in_domain: Optional[str] = None,
        out_domain: Optional[str] = None,
        bidding_zone_domain: Optional[str] = None,
        # Optional parameters for transmission queries
        business_type: Optional[str] = None,
        process_type: Optional[str] = None,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize transmission data parameters for ENTSO-E Transparency Platform.

        Args:
            document_type: Document type (e.g., A11, A59, A60, A61, A63, A64,
                          A65, A67, A70, A75, A85, A86, A87, A89, A90, A91,
                          A92, A93)
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: Input domain/bidding zone (e.g., 10YBE----------2)
            out_domain: Output domain/bidding zone (e.g., 10YGB----------A)
            bidding_zone_domain: Bidding zone domain (for some queries)
            business_type: Business type (e.g., A29, A31, A34, A37, A43, B05,
                          B07, B08, B10, B11)
            process_type: Process type (e.g., A01, A02, A16, A18, A31, A32, A33,
                         A39, A40, A44, A46)
            timeout: Request timeout in seconds
            offset: Offset for pagination

        Raises:
            ValidationError: If any input parameter is invalid

        Notes:
            - For cross-border physical flows: Use A11 document type
            - For forecasted capacity: Use A61 document type
            - For offered capacity: Use A29 document type
            - For already allocated capacity: Use A29 document type
            - For day-ahead prices: Use A44 document type
            - Unlike Web GUI, API responds not netted values as data is requested
              per direction
        """
        # Build query parameters
        self.params = {
            "documentType": document_type,
            "securityToken": security_token,
            "periodStart": period_start,
            "periodEnd": period_end,
        }

        # Add domain parameters - at least one typically required
        if in_domain:
            self.params["in_Domain"] = in_domain
        if out_domain:
            self.params["out_Domain"] = out_domain
        if bidding_zone_domain:
            self.params["biddingZone_Domain"] = bidding_zone_domain

        # Add optional parameters if provided
        if business_type:
            self.params["businessType"] = business_type
        if process_type:
            self.params["processType"] = process_type
        if offset:
            self.params["offset"] = offset

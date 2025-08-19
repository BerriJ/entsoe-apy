from typing import Optional

from .Base import BaseParams


class LoadParams(BaseParams):
    """Load data parameters for ENTSO-E Transparency Platform queries."""

    def __init__(
        self,
        document_type: str,
        out_bidding_zone_domain: str,
        security_token: str,
        period_start: int,
        period_end: int,
        # Optional parameters for load queries
        process_type: Optional[str] = None,
        business_type: Optional[str] = None,
        psr_type: Optional[str] = None,
        type_marketplace_agreement_type: Optional[str] = None,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize load data parameters for ENTSO-E Transparency Platform.

        Args:
            document_type: Document type (e.g., A65, A68, A69, A74, A75, A76, A77, A78)
            out_bidding_zone_domain: Bidding zone domain (e.g., 10YCZ-CEPS-----N)
                                    or area domain
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            process_type: Process type (e.g., A01, A02, A16, A18, A31, A32, A33,
                         A39, A40, A44, A46)
            business_type: Business type (e.g., A29, A43, A46, B07, B08, B09,
                          B10, B11, B17, B18, B19)
            psr_type: Power system resource type (A03, A04, A05, B01-B24)
            type_marketplace_agreement_type: Type marketplace agreement (A01-A07)
            timeout: Request timeout in seconds
            offset: Offset for pagination

        Raises:
            ValidationError: If any input parameter is invalid
        """

        # Initialize base parameters
        super().__init__(
            document_type=document_type,
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            timeout=timeout,
            offset=offset,
        )

        # Add domain parameters
        self.add_domain_params(out_bidding_zone_domain=out_bidding_zone_domain)

        # Add business parameters
        self.add_business_params(
            business_type=business_type,
            process_type=process_type,
            psr_type=psr_type,
        )

        # Add market parameters
        self.add_market_params(
            type_marketplace_agreement_type=type_marketplace_agreement_type
        )

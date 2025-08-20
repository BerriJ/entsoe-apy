from typing import Optional

from .Base import Base


class Load(Base):
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
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize load data parameters for ENTSO-E Transparency Platform.

        Args:
            document_type: Document type (A65 for System total load,
                          A70 for Load forecast margin)
            out_bidding_zone_domain: EIC code of a Control Area, Bidding Zone or Country
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            process_type: Process type (A01=Day ahead, A16=Realised, A31=Week ahead,
                         A32=Month ahead, A33=Year ahead)
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

        # Add business parameters (only process_type is used for load endpoints)
        self.add_business_params(process_type=process_type)

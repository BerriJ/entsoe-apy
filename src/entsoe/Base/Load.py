from .Base import Base


class Load(Base):
    """Load data parameters for ENTSO-E Transparency Platform queries."""

    def __init__(
        self,
        document_type: str,
        process_type: str,
        out_bidding_zone_domain: str,
        period_start: int,
        period_end: int,
        # Additional common parameters
        offset: int | None = None,
    ):
        """
        Initialize load data parameters for ENTSO-E Transparency Platform.

        Args:
            document_type: Document type (A65 for System total load,
                          A70 for Load forecast margin)
            process_type: Process type (A01=Day ahead, A16=Realised, A31=Week ahead,
                         A32=Month ahead, A33=Year ahead)
            out_bidding_zone_domain: EIC code of a Control Area, Bidding Zone or Country
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            offset: Offset for pagination

        Raises:
            ValidationError: If any input parameter is invalid


        """

        # Initialize base parameters
        super().__init__(
            document_type=document_type,
            period_start=period_start,
            period_end=period_end,
            offset=offset,
        )

        # Add domain parameters with EIC code validation
        self.add_domain_params(out_bidding_zone_domain=out_bidding_zone_domain)

        # Add business parameters (process_type is mandatory for load endpoints)
        self.add_business_params(process_type=process_type)

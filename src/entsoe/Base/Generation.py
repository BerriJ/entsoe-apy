from typing import Optional

from .Base import Base


class Generation(Base):
    """Generation data parameters for ENTSO-E Transparency Platform queries."""

    def __init__(
        self,
        document_type: str,
        period_start: int,
        period_end: int,
        # Domain parameters - typically required
        in_domain: Optional[str] = None,
        bidding_zone_domain: Optional[str] = None,
        # Optional parameters for generation queries
        process_type: Optional[str] = None,
        business_type: Optional[str] = None,
        psr_type: Optional[str] = None,
        registered_resource: Optional[str] = None,
        # Additional common parameters
        offset: int | None = None,
    ):
        """
        Initialize generation data parameters for ENTSO-E Transparency Platform.

        Args:
            document_type: Document type (e.g., A68, A73, A74, A75, A76, A77,
                          A78, A85, A87, A91, A92, A93, A95, A96, A97, A98)
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: Input domain/bidding zone (e.g., 10YBE----------2)
            bidding_zone_domain: Bidding zone domain (alternative to in_domain)
            process_type: Process type (e.g., A01, A02, A16, A18, A31, A32, A33,
                         A39, A40, A44, A46)
            business_type: Business type (e.g., A29, A37, A43, A46, B05, B07,
                          B08, B09, B10, B11, B17, B18, B19)
            psr_type: Power system resource type (B01-B25: different generation
                     types like Biomass, Nuclear, Wind, Solar, etc.)
            registered_resource: EIC Code of specific production unit or resource
            offset: Offset for pagination

        Raises:
            ValidationError: If any input parameter is invalid



        Notes:
            - For installed capacity queries: Use A68 with processType A33 (Year ahead)
            - For actual generation: Use A75 with appropriate PSR types
            - For generation forecasts: Use A71 (Day ahead), A72 (Week ahead),
              A73 (Month ahead), A74 (Year ahead)
            - For water reservoirs: Use A72 document type
            - PSR Types: B01=Biomass, B02=Brown coal, B04=Gas, B05=Hard coal,
              B06=Oil, B10=Hydro Pumped Storage, B11=Hydro Run-of-river,
              B12=Hydro Water Reservoir, B14=Nuclear, B16=Solar,
              B18=Wind Offshore, B19=Wind Onshore, etc.
        """
        # Initialize base parameters
        super().__init__(
            document_type=document_type,
            period_start=period_start,
            period_end=period_end,
            offset=offset,
        )

        # Add domain parameters
        self.add_domain_params(
            in_domain=in_domain,
            bidding_zone_domain=bidding_zone_domain,
        )

        # Add business parameters
        self.add_business_params(
            business_type=business_type,
            process_type=process_type,
            psr_type=psr_type,
        )

        # Add resource parameters
        self.add_resource_params(registered_resource=registered_resource)

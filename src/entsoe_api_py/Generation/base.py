from typing import Optional


def Generation_params(
    document_type: str,
    security_token: str,
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
    timeout: int = 60,
    offset: Optional[int] = None,
) -> object:
    """
    Request generation data from ENTSO-E Transparency Platform.

    Args:
        document_type: Document type (e.g., A68, A73, A74, A75, A76, A77, A78,
                      A85, A87, A91, A92, A93, A95, A96, A97, A98)
        security_token: API security token
        period_start: Start period (YYYYMMDDHHMM format)
        period_end: End period (YYYYMMDDHHMM format)
        in_domain: Input domain/bidding zone (e.g., 10YBE----------2)
        bidding_zone_domain: Bidding zone domain (alternative to in_domain)
        process_type: Process type (e.g., A01, A02, A16, A18, A31, A32, A33,
                     A39, A40, A44, A46)
        business_type: Business type (e.g., A29, A37, A43, A46, B05, B07, B08,
                      B09, B10, B11, B17, B18, B19)
        psr_type: Power system resource type (B01-B25: different generation
                 types like Biomass, Nuclear, Wind, Solar, etc.)
        registered_resource: EIC Code of specific production unit or resource
        timeout: Request timeout in seconds
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
    # Build query parameters
    params = {
        "documentType": document_type,
        "securityToken": security_token,
        "periodStart": period_start,
        "periodEnd": period_end,
    }

    # Add domain parameters - at least one typically required
    if in_domain:
        params["in_Domain"] = in_domain
    if bidding_zone_domain:
        params["biddingZone_Domain"] = bidding_zone_domain

    # Add optional parameters if provided
    if process_type:
        params["processType"] = process_type
    if business_type:
        params["businessType"] = business_type
    if psr_type:
        params["psrType"] = psr_type
    if registered_resource:
        params["registeredResource"] = registered_resource
    if offset:
        params["offset"] = offset

    return params

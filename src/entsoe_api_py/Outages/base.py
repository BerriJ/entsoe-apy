from typing import Optional


def Outages_params(
    document_type: str,
    security_token: str,
    period_start: Optional[int] = None,
    period_end: Optional[int] = None,
    # Domain parameters - typically required
    bidding_zone_domain: Optional[str] = None,
    # Alternative period parameters for update-based queries
    period_start_update: Optional[int] = None,
    period_end_update: Optional[int] = None,
    # Optional parameters for outage queries
    business_type: Optional[str] = None,
    doc_status: Optional[str] = None,
    registered_resource: Optional[str] = None,
    m_rid: Optional[str] = None,
    # Additional common parameters
    timeout: int = 60,
    offset: Optional[int] = None,
) -> object:
    """
    Request outage data from ENTSO-E Transparency Platform.

    Args:
        document_type: Document type (e.g., A77, A78, A79, A80, A81, A82, A83)
        security_token: API security token
        period_start: Start period (YYYYMMDDHHMM format, optional if
                     period_start_update is defined)
        period_end: End period (YYYYMMDDHHMM format, optional if
                   period_end_update is defined)
        bidding_zone_domain: EIC code of Control Area, Bidding Zone
                           (optional if mRID is present)
        period_start_update: Start of update period (YYYYMMDDHHMM format,
                           mandatory if period_start and period_end not defined)
        period_end_update: End of update period (YYYYMMDDHHMM format,
                         mandatory if period_start and period_end not defined)
        business_type: Business type (e.g., A53=Planned maintenance,
                      A54=Forced unavailability/unplanned outage)
        doc_status: Document status (A05=Active, A09=Cancelled, A13=Withdrawn;
                   when not defined only Active and Cancelled outages returned)
        registered_resource: EIC Code of Production Unit or Transmission Element
        m_rid: Message ID - older versions of outage returned only when used
        timeout: Request timeout in seconds
        offset: Offset for pagination (allows downloading more than 200 docs,
               offset ∈ [0,4800] so paging restricted to 5000 docs max)

    Raises:
        ValidationError: If any input parameter is invalid

    Notes:
        - For production unit unavailability: Use A77 document type
        - For transmission unavailability: Use A78 document type
        - Time range limited to 1 year for period_start & period_end
        - If using update parameters, time range limit applies only to
          period_start_update & period_end_update
        - TimeIntervalUpdate corresponds to 'Updated(UTC)' timestamp in
          platform value details
    """
    # Build query parameters
    params = {
        "documentType": document_type,
        "securityToken": security_token,
    }

    # Add time period parameters
    if period_start is not None:
        params["periodStart"] = period_start
    if period_end is not None:
        params["periodEnd"] = period_end
    if period_start_update is not None:
        params["periodStartUpdate"] = period_start_update
    if period_end_update is not None:
        params["periodEndUpdate"] = period_end_update

    # Add domain parameters
    if bidding_zone_domain:
        params["biddingZone_Domain"] = bidding_zone_domain

    # Add optional parameters if provided
    if business_type:
        params["businessType"] = business_type
    if doc_status:
        params["docStatus"] = doc_status
    if registered_resource:
        params["registeredResource"] = registered_resource
    if m_rid:
        params["mRID"] = m_rid
    if offset:
        params["offset"] = offset

    return params

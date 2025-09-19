from typing import Optional

from .Base import Base


class Outages(Base):
    """Outages data parameters for ENTSO-E Transparency Platform queries."""

    def __init__(
        self,
        document_type: str,
        period_start: Optional[int] = None,
        period_end: Optional[int] = None,
        # Domain parameters - typically required
        bidding_zone_domain: Optional[str] = None,
        # Alternative period parameters for update-based queries
        period_start_update: Optional[int] = None,
        period_end_update: Optional[int] = None,
        time_interval_update: Optional[str] = None,
        # Optional parameters for outage queries
        business_type: Optional[str] = None,
        doc_status: Optional[str] = None,
        registered_resource: Optional[str] = None,
        m_rid: Optional[str] = None,
        # Additional common parameters
        offset: int | None = None,
    ):
        """
        Initialize outage data parameters for ENTSO-E Transparency Platform.

        Args:
            document_type: Document type (e.g., A77, A78, A79, A80, A81, A82, A83)
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
            time_interval_update: Time interval update (can be used instead of
                                period_start_update & period_end_update)
            business_type: Business type (e.g., A53=Planned maintenance,
                          A54=Forced unavailability/unplanned outage)
            doc_status: Document status (A05=Active, A09=Cancelled, A13=Withdrawn;
                       when not defined only Active and Cancelled outages returned)
            registered_resource: EIC Code of Production Unit or Transmission Element
            m_rid: Message ID - older versions of outage returned only when used
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
        # Initialize base parameters using proper encapsulation
        super().__init__(
            document_type=document_type,
            period_start=period_start,
            period_end=period_end,
            offset=offset,
        )

        # Add update period parameters
        self.add_update_params(
            period_start_update=period_start_update,
            period_end_update=period_end_update,
            time_interval_update=time_interval_update,
        )

        # Add domain parameters
        self.add_domain_params(bidding_zone_domain=bidding_zone_domain)

        # Add business parameters
        self.add_business_params(business_type=business_type)

        # Add resource parameters
        self.add_resource_params(registered_resource=registered_resource)

        # Add outage-specific parameters
        self.add_optional_param("docStatus", doc_status)
        self.add_optional_param("mRID", m_rid)

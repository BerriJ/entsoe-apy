from typing import Optional


class OMIParams:
    """Other Market Information (OMI) parameters for ENTSO-E Transparency
    Platform queries."""

    def __init__(
        self,
        document_type: str,
        security_token: str,
        period_start: Optional[int] = None,
        period_end: Optional[int] = None,
        # Domain parameters - required based on query type
        control_area_domain: Optional[str] = None,
        # Alternative period parameters for update-based queries
        period_start_update: Optional[int] = None,
        period_end_update: Optional[int] = None,
        # Optional parameters for OMI queries
        doc_status: Optional[str] = None,
        m_rid: Optional[str] = None,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize Other Market Information parameters for ENTSO-E Transparency
        Platform.

        Args:
            document_type: Document type (e.g., B47 = Other market information)
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format, optional if
                         period_start_update is defined)
            period_end: End period (YYYYMMDDHHMM format, optional if
                       period_end_update is defined)
            control_area_domain: EIC code of Scheduling Area (typically required)
            period_start_update: Start of update period (YYYYMMDDHHMM format,
                               mandatory if period_start and period_end not defined)
            period_end_update: End of update period (YYYYMMDDHHMM format,
                             mandatory if period_start and period_end not defined)
            doc_status: Document status (A05=Active, A09=Cancelled, A13=Withdrawn)
            m_rid: Message ID - if included, individual versions of particular
                  event are queried using rest of parameters
            timeout: Request timeout in seconds
            offset: Offset for pagination (allows downloading more than 200 docs,
                   offset ∈ [0,4800] so paging restricted to 5000 docs max)

        Raises:
            ValidationError: If any input parameter is invalid

        Notes:
            - Primary document type is B47 for Other Market Information
            - Used for various market notifications and information not covered
              by other specific document types
            - Supports both standard period queries and update-based queries
            - Time range limitations may apply depending on query type
        """
        # Build query parameters
        self.params = {
            "documentType": document_type,
            "securityToken": security_token,
        }

        # Add time period parameters
        if period_start is not None:
            self.params["periodStart"] = period_start
        if period_end is not None:
            self.params["periodEnd"] = period_end
        if period_start_update is not None:
            self.params["periodStartUpdate"] = period_start_update
        if period_end_update is not None:
            self.params["periodEndUpdate"] = period_end_update

        # Add domain parameters
        if control_area_domain:
            self.params["controlArea_Domain"] = control_area_domain

        # Add optional parameters if provided
        if doc_status:
            self.params["docStatus"] = doc_status
        if m_rid:
            self.params["mRID"] = m_rid
        if offset:
            self.params["offset"] = offset

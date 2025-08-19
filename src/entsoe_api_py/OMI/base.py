from typing import Optional

from ..base_params import BaseParams


class OMIParams(BaseParams):
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
        # Initialize base parameters - handle period parameters separately for OMI
        self.params = {
            "documentType": document_type,
            "securityToken": security_token,
        }
        self.timeout = timeout

        # Add time period parameters (optional for OMI)
        if period_start is not None:
            self.params["periodStart"] = period_start
        if period_end is not None:
            self.params["periodEnd"] = period_end

        # Add update period parameters
        self.add_update_params(
            period_start_update=period_start_update,
            period_end_update=period_end_update,
        )

        # Add domain parameters
        self.add_domain_params(control_area_domain=control_area_domain)

        # Add OMI-specific parameters
        self.add_optional_param("docStatus", doc_status)
        self.add_optional_param("mRID", m_rid)
        self.add_optional_param("offset", offset)

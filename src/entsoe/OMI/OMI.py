from typing import Literal, Optional

from ..Base.Base import Base


class OMI(Base):
    """Other Market Information (OMI) parameters for ENTSO-E Transparency
    Platform queries."""

    def __init__(
        self,
        security_token: str,
        period_start: Optional[int] = None,
        period_end: Optional[int] = None,
        # Domain parameters - required based on query type
        control_area_domain: Optional[str] = None,
        # Alternative period parameters for update-based queries
        period_start_update: Optional[int] = None,
        period_end_update: Optional[int] = None,
        # Optional parameters for OMI queries
        doc_status: Optional[Literal["A05", "A09", "A13"]] = None,
        m_rid: Optional[str] = None,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize Other Market Information parameters for ENTSO-E Transparency
        Platform.

        Args:
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
            ValueError: If doc_status is not one of A05, A09, A13

        Notes:
            - Document type is fixed to B47 (Other Market Information)
            - Used for various market notifications and information not covered
              by other specific document types
            - Supports both standard period queries and update-based queries
            - Time range limitations may apply depending on query type
        """
        # Validate doc_status if provided
        if doc_status is not None:
            valid_statuses = ["A05", "A09", "A13"]
            if doc_status not in valid_statuses:
                raise ValueError(
                    f"doc_status must be one of {valid_statuses}, got: {doc_status}"
                )

        # Initialize base parameters using proper encapsulation
        super().__init__(
            document_type="B47",  # Fixed to B47 for Other Market Information
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            timeout=timeout,
            offset=offset,
        )

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

from typing import Literal, Optional

from ..Base.Base import Base


class OMI(Base):
    """Other Market Information (OMI) parameters for ENTSO-E Transparency
    Platform queries."""

    def __init__(
        self,
        control_area_domain: str,  # Required - EIC code of Scheduling Area
        period_start: Optional[int] = None,
        period_end: Optional[int] = None,
        # Alternative period parameters for update-based queries
        period_start_update: Optional[int] = None,
        period_end_update: Optional[int] = None,
        # Optional parameters for OMI queries
        doc_status: Optional[Literal["A05", "A09", "A13"]] = None,
        m_rid: Optional[str] = None,
        # Additional common parameters
        offset: int = 0,
    ):
        """
        Initialize Other Market Information parameters for ENTSO-E Transparency
        Platform.

        Args:
            control_area_domain: EIC code of Scheduling Area (required)
            period_start: Start period (YYYYMMDDHHMM format, optional if
                         period_start_update and period_end_update are defined)
            period_end: End period (YYYYMMDDHHMM format, optional if
                       period_start_update and period_end_update are defined)
            period_start_update: Start of update period (YYYYMMDDHHMM format,
                               mandatory if period_start and period_end not defined)
            period_end_update: End of update period (YYYYMMDDHHMM format,
                             mandatory if period_start and period_end not defined)
            doc_status: Document status (A05=Active, A09=Cancelled, A13=Withdrawn)
            m_rid: Message ID - if included, individual versions of particular
                  event are queried using rest of parameters
            offset: Offset for pagination (allows downloading more than 200 docs,
                   offset ∈ [0,4800] so paging restricted to 5000 docs max)

        Raises:
            ValueError: If doc_status is not one of A05, A09, A13
            ValueError: If neither (period_start, period_end) nor
                       (period_start_update, period_end_update) are provided



        Notes:
            - Document type is fixed to B47 (Other Market Information)
            - Used for various market notifications and information not covered
              by other specific document types
            - Supports both standard period queries and update-based queries
            - Time range limitations may apply depending on query type
            - Either (period_start, period_end) OR (period_start_update,
              period_end_update) must be provided
        """
        # Validate doc_status if provided
        if doc_status is not None:
            valid_statuses = ["A05", "A09", "A13"]
            if doc_status not in valid_statuses:
                raise ValueError(
                    f"doc_status must be one of {valid_statuses}, got: {doc_status}"
                )

        # Validate that either (period_start, period_end) or
        # (period_start_update, period_end_update) are provided
        has_period = period_start is not None and period_end is not None
        has_update_period = (
            period_start_update is not None and period_end_update is not None
        )

        if not has_period and not has_update_period:
            raise ValueError(
                "Either (period_start, period_end) or "
                "(period_start_update, period_end_update) must be provided"
            )

        # Initialize base parameters using proper encapsulation
        super().__init__(
            document_type="B47",  # Fixed to B47 for Other Market Information
            period_start=period_start,
            period_end=period_end,
            offset=0,  # Don't pass offset to base, we'll handle it with correct name
        )

        # Add OMI-specific parameters using exact JSON parameter names
        self.add_optional_param("ControlArea_Domain", control_area_domain)
        self.add_optional_param("DocStatus", doc_status)
        self.add_optional_param("PeriodStartUpdate", period_start_update)
        self.add_optional_param("PeriodEndUpdate", period_end_update)
        self.add_optional_param("Offset", offset)
        self.add_optional_param("mRID", m_rid)

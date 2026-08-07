"""Specific parameter classes for ENTSO-E OMI endpoints.

This module contains specialized parameter classes for different OMI data
endpoints, each inheriting from OMI and providing preset values for
fixed parameters based on the ENTSO-E Transparency Platform API specification.
"""

from typing import Optional

from .OMI import OMI


class OtherMarketInformation(OMI):
    """Parameters for Other Market Information.

    Data view:
    https://transparency.entsoe.eu/omi-domain/r2/otherMarketInformation/show

    Fixed parameters:

    - documentType: B47 (Other market information)

    Notes:
    - Returns other market information data
    - Can be filtered by document status (A05=Active, A09=Cancelled, A13=Withdrawn)
    - Supports update-based queries with PeriodStartUpdate/PeriodEndUpdate
    """

    code = "Other Market"

    def __init__(
        self,
        control_area_domain: str,
        period_start: Optional[int] = None,
        period_end: Optional[int] = None,
        # Optional filtering parameters
        doc_status: Optional[str] = None,
        period_start_update: Optional[int] = None,
        period_end_update: Optional[int] = None,
        m_rid: Optional[str] = None,
        # Additional common parameters
        offset: int = 0,
    ):
        """
        Initialize other market information parameters.

        Args:
            control_area_domain: EIC code of Scheduling Area
            period_start: Start period (YYYYMMDDHHMM format, optional if
                         period_start_update and period_end_update are defined)
            period_end: End period (YYYYMMDDHHMM format, optional if
                       period_start_update and period_end_update are defined)
            doc_status: Document status (A05=Active, A09=Cancelled, A13=Withdrawn)
            period_start_update: Start of update period (YYYYMMDDHHMM format,
                               mandatory if period_start and period_end not defined)
            period_end_update: End of update period (YYYYMMDDHHMM format,
                             mandatory if period_start and period_end not defined)
            m_rid: Message ID for specific information versions
            offset: Offset for pagination

        Note:
            Either (period_start, period_end) or
            (period_start_update, period_end_update)
            must be provided. The parent OMI class validates this requirement.
        """
        super().__init__(
            control_area_domain=control_area_domain,
            period_start=period_start,
            period_end=period_end,
            period_start_update=period_start_update,
            period_end_update=period_end_update,
            doc_status=doc_status,
            m_rid=m_rid,
            offset=offset,
        )

        # Set the fixed document type for Other Market Information
        self.add_optional_param("documentType", "B47")

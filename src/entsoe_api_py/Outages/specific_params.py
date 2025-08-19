"""Specific parameter classes for ENTSO-E Outages endpoints.

This module contains specialized parameter classes for different Outages data
endpoints, each inheriting from OutagesParams and providing preset values for
fixed parameters.
"""

from typing import Optional

from ..Base.Outages import Outages


class PlannedProductionUnitUnavailability(Outages):
    """Parameters for 7.1.A Planned Production Unit Unavailability.

    Data view:
    https://transparency.entsoe.eu/outages/r2/unavailabilityOfProductionAndGenerationUnits/show

    Fixed parameters:
    - documentType: A77 (Production unit unavailability)
    - businessType: A53 (Planned maintenance)

    Notes:
    - Returns planned outages and maintenance schedules for generation units
    - Includes detailed information about planned maintenance periods
    - Can be filtered by specific production units or bidding zones
    """

    code = "7.1.A"

    def __init__(
        self,
        security_token: str,
        bidding_zone_domain: str,
        # Time period parameters (at least one set required)
        period_start: Optional[int] = None,
        period_end: Optional[int] = None,
        period_start_update: Optional[int] = None,
        period_end_update: Optional[int] = None,
        # Optional filtering parameters
        registered_resource: Optional[str] = None,
        doc_status: Optional[str] = None,
        m_rid: Optional[str] = None,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize planned production unit unavailability parameters.

        Args:
            security_token: API security token
            bidding_zone_domain: EIC code of Control Area, Bidding Zone
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            period_start_update: Start of update period (YYYYMMDDHHMM format)
            period_end_update: End of update period (YYYYMMDDHHMM format)
            registered_resource: EIC Code of Production Unit
            doc_status: Document status (A05=Active, A09=Cancelled, A13=Withdrawn)
            m_rid: Message ID for specific outage versions
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset business type for planned maintenance
        super().__init__(
            document_type="A77",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            period_start_update=period_start_update,
            period_end_update=period_end_update,
            business_type="A53",  # Planned maintenance
            doc_status=doc_status,
            registered_resource=registered_resource,
            m_rid=m_rid,
            timeout=timeout,
            offset=offset,
        )


class ForcedProductionUnitUnavailability(Outages):
    """Parameters for 7.1.B Forced Production Unit Unavailability.

    Data view:
    https://transparency.entsoe.eu/outages/r2/unavailabilityOfProductionAndGenerationUnits/show

    Fixed parameters:
    - documentType: A77 (Production unit unavailability)
    - businessType: A54 (Forced unavailability/unplanned outage)

    Notes:
    - Returns unplanned outages and forced unavailability for generation units
    - Includes emergency shutdowns and unexpected equipment failures
    - Critical for real-time market operations and grid stability
    """

    code = "7.1.B"

    def __init__(
        self,
        security_token: str,
        bidding_zone_domain: str,
        # Time period parameters (at least one set required)
        period_start: Optional[int] = None,
        period_end: Optional[int] = None,
        period_start_update: Optional[int] = None,
        period_end_update: Optional[int] = None,
        # Optional filtering parameters
        registered_resource: Optional[str] = None,
        doc_status: Optional[str] = None,
        m_rid: Optional[str] = None,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize forced production unit unavailability parameters.

        Args:
            security_token: API security token
            bidding_zone_domain: EIC code of Control Area, Bidding Zone
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            period_start_update: Start of update period (YYYYMMDDHHMM format)
            period_end_update: End of update period (YYYYMMDDHHMM format)
            registered_resource: EIC Code of Production Unit
            doc_status: Document status (A05=Active, A09=Cancelled, A13=Withdrawn)
            m_rid: Message ID for specific outage versions
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset business type for forced unavailability
        super().__init__(
            document_type="A77",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            period_start_update=period_start_update,
            period_end_update=period_end_update,
            business_type="A54",  # Forced unavailability/unplanned outage
            doc_status=doc_status,
            registered_resource=registered_resource,
            m_rid=m_rid,
            timeout=timeout,
            offset=offset,
        )


class PlannedTransmissionUnavailability(Outages):
    """Parameters for 7.1.C Planned Transmission Unavailability.

    Data view:
    https://transparency.entsoe.eu/outages/r2/unavailabilityTransmissionInfrastructure/show

    Fixed parameters:
    - documentType: A78 (Transmission unavailability)
    - businessType: A53 (Planned maintenance)

    Notes:
    - Returns planned outages for transmission infrastructure
    - Includes maintenance schedules for transmission lines, transformers
    - Essential for understanding planned network topology changes
    """

    code = "7.1.C"

    def __init__(
        self,
        security_token: str,
        bidding_zone_domain: str,
        # Time period parameters (at least one set required)
        period_start: Optional[int] = None,
        period_end: Optional[int] = None,
        period_start_update: Optional[int] = None,
        period_end_update: Optional[int] = None,
        # Optional filtering parameters
        registered_resource: Optional[str] = None,
        doc_status: Optional[str] = None,
        m_rid: Optional[str] = None,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize planned transmission unavailability parameters.

        Args:
            security_token: API security token
            bidding_zone_domain: EIC code of Control Area, Bidding Zone
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            period_start_update: Start of update period (YYYYMMDDHHMM format)
            period_end_update: End of update period (YYYYMMDDHHMM format)
            registered_resource: EIC Code of Transmission Element
            doc_status: Document status (A05=Active, A09=Cancelled, A13=Withdrawn)
            m_rid: Message ID for specific outage versions
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset business type for planned maintenance
        super().__init__(
            document_type="A78",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            period_start_update=period_start_update,
            period_end_update=period_end_update,
            business_type="A53",  # Planned maintenance
            doc_status=doc_status,
            registered_resource=registered_resource,
            m_rid=m_rid,
            timeout=timeout,
            offset=offset,
        )


class ForcedTransmissionUnavailability(Outages):
    """Parameters for 7.1.D Forced Transmission Unavailability.

    Data view:
    https://transparency.entsoe.eu/outages/r2/unavailabilityTransmissionInfrastructure/show

    Fixed parameters:
    - documentType: A78 (Transmission unavailability)
    - businessType: A54 (Forced unavailability/unplanned outage)

    Notes:
    - Returns unplanned outages for transmission infrastructure
    - Includes emergency shutdowns and equipment failures
    - Critical for real-time grid management and contingency analysis
    """

    code = "7.1.D"

    def __init__(
        self,
        security_token: str,
        bidding_zone_domain: str,
        # Time period parameters (at least one set required)
        period_start: Optional[int] = None,
        period_end: Optional[int] = None,
        period_start_update: Optional[int] = None,
        period_end_update: Optional[int] = None,
        # Optional filtering parameters
        registered_resource: Optional[str] = None,
        doc_status: Optional[str] = None,
        m_rid: Optional[str] = None,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize forced transmission unavailability parameters.

        Args:
            security_token: API security token
            bidding_zone_domain: EIC code of Control Area, Bidding Zone
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            period_start_update: Start of update period (YYYYMMDDHHMM format)
            period_end_update: End of update period (YYYYMMDDHHMM format)
            registered_resource: EIC Code of Transmission Element
            doc_status: Document status (A05=Active, A09=Cancelled, A13=Withdrawn)
            m_rid: Message ID for specific outage versions
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset business type for forced unavailability
        super().__init__(
            document_type="A78",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            period_start_update=period_start_update,
            period_end_update=period_end_update,
            business_type="A54",  # Forced unavailability/unplanned outage
            doc_status=doc_status,
            registered_resource=registered_resource,
            m_rid=m_rid,
            timeout=timeout,
            offset=offset,
        )


class ProductionUnitUnavailability(Outages):
    """Parameters for 7.1.E Production Unit Unavailability (All Types).

    Data view:
    https://transparency.entsoe.eu/outages/r2/unavailabilityOfProductionAndGenerationUnits/show

    Fixed parameters:
    - documentType: A77 (Production unit unavailability)
    - businessType: Not specified (returns all types: planned, forced, etc.)

    Notes:
    - Returns all production unit outages regardless of type
    - Includes both planned maintenance and forced outages
    - Comprehensive view of all generation unit unavailability
    """

    code = "7.1.E"

    def __init__(
        self,
        security_token: str,
        bidding_zone_domain: str,
        # Time period parameters (at least one set required)
        period_start: Optional[int] = None,
        period_end: Optional[int] = None,
        period_start_update: Optional[int] = None,
        period_end_update: Optional[int] = None,
        # Optional filtering parameters
        registered_resource: Optional[str] = None,
        doc_status: Optional[str] = None,
        m_rid: Optional[str] = None,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize production unit unavailability parameters (all types).

        Args:
            security_token: API security token
            bidding_zone_domain: EIC code of Control Area, Bidding Zone
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            period_start_update: Start of update period (YYYYMMDDHHMM format)
            period_end_update: End of update period (YYYYMMDDHHMM format)
            registered_resource: EIC Code of Production Unit
            doc_status: Document status (A05=Active, A09=Cancelled, A13=Withdrawn)
            m_rid: Message ID for specific outage versions
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize without business type filter to get all outage types
        super().__init__(
            document_type="A77",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            period_start_update=period_start_update,
            period_end_update=period_end_update,
            business_type=None,  # No filter - get all business types
            doc_status=doc_status,
            registered_resource=registered_resource,
            m_rid=m_rid,
            timeout=timeout,
            offset=offset,
        )


class TransmissionUnavailability(Outages):
    """Parameters for 7.1.F Transmission Unavailability (All Types).

    Data view:
    https://transparency.entsoe.eu/outages/r2/unavailabilityTransmissionInfrastructure/show

    Fixed parameters:
    - documentType: A78 (Transmission unavailability)
    - businessType: Not specified (returns all types: planned, forced, etc.)

    Notes:
    - Returns all transmission outages regardless of type
    - Includes both planned maintenance and forced outages
    - Comprehensive view of all transmission infrastructure unavailability
    """

    code = "7.1.F"

    def __init__(
        self,
        security_token: str,
        bidding_zone_domain: str,
        # Time period parameters (at least one set required)
        period_start: Optional[int] = None,
        period_end: Optional[int] = None,
        period_start_update: Optional[int] = None,
        period_end_update: Optional[int] = None,
        # Optional filtering parameters
        registered_resource: Optional[str] = None,
        doc_status: Optional[str] = None,
        m_rid: Optional[str] = None,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize transmission unavailability parameters (all types).

        Args:
            security_token: API security token
            bidding_zone_domain: EIC code of Control Area, Bidding Zone
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            period_start_update: Start of update period (YYYYMMDDHHMM format)
            period_end_update: End of update period (YYYYMMDDHHMM format)
            registered_resource: EIC Code of Transmission Element
            doc_status: Document status (A05=Active, A09=Cancelled, A13=Withdrawn)
            m_rid: Message ID for specific outage versions
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize without business type filter to get all outage types
        super().__init__(
            document_type="A78",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            period_start_update=period_start_update,
            period_end_update=period_end_update,
            business_type=None,  # No filter - get all business types
            doc_status=doc_status,
            registered_resource=registered_resource,
            m_rid=m_rid,
            timeout=timeout,
            offset=offset,
        )

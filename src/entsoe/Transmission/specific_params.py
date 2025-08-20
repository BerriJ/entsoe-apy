"""Specific parameter classes for ENTSO-E Transmission endpoints.

This module contains specialized parameter classes for different Transmission data
endpoints, each inheriting from TransmissionParams and providing preset values for
fixed parameters.
"""

from typing import Optional

from ..Base.Transmission import Transmission


class TotalNominatedCapacity(Transmission):
    """Parameters for 12.1.B Total Nominated Capacity.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/scheduledCommercialExchangesDayAhead/show

    Fixed parameters:
    - documentType: A26 (Capacity document)
    - businessType: B08 (Total nominated capacity)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one MTU period
    """

    code = "12.1.B"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        out_domain: str,
        in_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize total nominated capacity parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            out_domain: EIC code of output domain/bidding zone
            in_domain: EIC code of input domain/bidding zone
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A26",
            business_type="B08",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            out_domain=out_domain,
            in_domain=in_domain,
            timeout=timeout,
            offset=offset,
        )


class ImplicitAllocationsOfferedCapacity(Transmission):
    """Parameters for 11.1 Implicit Allocations - Offered Transfer Capacity.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/dayAheadCommercialSchedules/show

    Fixed parameters:
    - documentType: A31 (Agreed capacity)
    - auction.Type: A01 (Implicit)
    - contract_MarketAgreement.Type: A01 (Daily)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one MTU period
    """

    code = "11.1"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        out_domain: str,
        in_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize implicit allocations offered capacity parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            out_domain: EIC code of output domain/bidding zone
            in_domain: EIC code of input domain/bidding zone
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A31",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            out_domain=out_domain,
            in_domain=in_domain,
            timeout=timeout,
            offset=offset,
        )

        # Add specific parameters for implicit allocations
        self.add_optional_param("auction.Type", "A01")
        self.add_optional_param("contract_MarketAgreement.Type", "A01")


class ExplicitAllocationsOfferedCapacity(Transmission):
    """Parameters for 11.1.A Explicit Allocations - Offered Transfer Capacity.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/explicitCapacityAllocations/show

    Fixed parameters:
    - documentType: A31 (Agreed capacity)
    - auction.Type: A02 (Explicit)
    - contract_MarketAgreement.Type: A01 (Daily)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one MTU period
    """

    code = "11.1.A"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        out_domain: str,
        in_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize explicit allocations offered capacity parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            out_domain: EIC code of output domain/bidding zone
            in_domain: EIC code of input domain/bidding zone
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A31",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            out_domain=out_domain,
            in_domain=in_domain,
            timeout=timeout,
            offset=offset,
        )

        # Add specific parameters for explicit allocations
        self.add_optional_param("auction.Type", "A02")
        self.add_optional_param("contract_MarketAgreement.Type", "A01")


class TotalCapacityAlreadyAllocated(Transmission):
    """Parameters for 12.1.C Total Capacity Already Allocated.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/capacityAllocations/show

    Fixed parameters:
    - documentType: A26 (Capacity document)
    - businessType: A29 (Already allocated capacity)
    - contract_MarketAgreement.Type: A01 (Daily)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one MTU period
    """

    code = "12.1.C"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        out_domain: str,
        in_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize total capacity already allocated parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            out_domain: EIC code of output domain/bidding zone
            in_domain: EIC code of input domain/bidding zone
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A26",
            business_type="A29",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            out_domain=out_domain,
            in_domain=in_domain,
            timeout=timeout,
            offset=offset,
        )

        # Add specific parameters
        self.add_optional_param("contract_MarketAgreement.Type", "A01")


class CrossBorderPhysicalFlows(Transmission):
    """Parameters for 12.1.G Cross-Border Physical Flows.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/physicalFlows/show

    Fixed parameters:
    - documentType: A11 (Flow document)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one MTU period
    """

    code = "12.1.G"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        out_domain: str,
        in_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize cross-border physical flows parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            out_domain: EIC code of output domain/bidding zone
            in_domain: EIC code of input domain/bidding zone
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A11",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            out_domain=out_domain,
            in_domain=in_domain,
            timeout=timeout,
            offset=offset,
        )


class CommercialSchedules(Transmission):
    """Parameters for 12.1.F Commercial Schedules.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/dayAheadCommercialSchedules/show

    Fixed parameters:
    - documentType: A09 (Finalised schedule)
    - contract_MarketAgreement.Type: A01 (Daily)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one MTU period
    """

    code = "12.1.F"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        out_domain: str,
        in_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize commercial schedules parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            out_domain: EIC code of output domain/bidding zone
            in_domain: EIC code of input domain/bidding zone
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A09",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            out_domain=out_domain,
            in_domain=in_domain,
            timeout=timeout,
            offset=offset,
        )

        # Add specific parameters
        self.add_optional_param("contract_MarketAgreement.Type", "A01")


class ForecastedTransferCapacities(Transmission):
    """Parameters for 11.1.A Forecasted Transfer Capacities.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/forecastedCapacity/show

    Fixed parameters:
    - documentType: A61 (Estimated Net Transfer Capacity)
    - contract_MarketAgreement.Type: A01 (Daily)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one MTU period
    """

    code = "11.1.A"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        out_domain: str,
        in_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize forecasted transfer capacities parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            out_domain: EIC code of output domain/bidding zone
            in_domain: EIC code of input domain/bidding zone
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A61",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            out_domain=out_domain,
            in_domain=in_domain,
            timeout=timeout,
            offset=offset,
        )

        # Add specific parameters
        self.add_optional_param("contract_MarketAgreement.Type", "A01")


class FlowBasedAllocations(Transmission):
    """Parameters for 11.1.B Flow Based Allocations.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/flowBasedAllocations/show

    Fixed parameters:
    - documentType: B09 (Flow based allocations)
    - processType: A44 (Flow based)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one MTU period
    """

    code = "11.1.B"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize flow based allocations parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of bidding zone domain
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="B09",
            process_type="A44",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            timeout=timeout,
            offset=offset,
        )


class UnavailabilityTransmissionInfrastructure(Transmission):
    """Parameters for 10.1.A&B Unavailability of Transmission Infrastructure.

    Data view:
    https://transparency.entsoe.eu/outages/r2/unavailabilityOfTransmissionInfrastructure/show

    Fixed parameters:
    - documentType: A78 (Unavailability of transmission)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one MTU period
    """

    code = "10.1.A&B"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize unavailability of transmission infrastructure parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of bidding zone domain
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A78",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            timeout=timeout,
            offset=offset,
        )


class UnavailabilityOffshoreGridInfrastructure(Transmission):
    """Parameters for 10.1.C Unavailability of Offshore Grid Infrastructure.

    Data view:
    https://transparency.entsoe.eu/outages/r2/unavailabilityOfOffshoreGridInfrastructure/show

    Fixed parameters:
    - documentType: A79 (Unavailability of offshore grid)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one MTU period
    """

    code = "10.1.C"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize unavailability of offshore grid infrastructure parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of bidding zone domain
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A79",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            timeout=timeout,
            offset=offset,
        )

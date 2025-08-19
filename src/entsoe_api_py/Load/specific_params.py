"""Specific parameter classes for ENTSO-E Load endpoints.

This module contains specialized parameter classes for different Load data endpoints,
each inheriting from LoadParams and providing preset values for fixed parameters.
"""

from typing import Optional

from ..Base.Load import LoadParams


class ActualTotalLoadParams(LoadParams):
    """Parameters for 6.1.A Actual Total Load.

    Data view:
    https://transparency.entsoe.eu/load-domain/r2/totalLoadR2/show

    Fixed parameters:
    - documentType: A65 (System total load)
    - processType: A16 (Realised)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one MTU period
    """

    code = "6.1.A"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        out_bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize actual total load parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            out_bidding_zone_domain: EIC code of a Control Area, Bidding Zone or Country
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A65",
            process_type="A16",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            out_bidding_zone_domain=out_bidding_zone_domain,
            timeout=timeout,
            offset=offset,
        )


class DayAheadTotalLoadForecastParams(LoadParams):
    """Parameters for 6.1.B Day-ahead Total Load Forecast.

    Data view:
    https://transparency.entsoe.eu/load-domain/r2/totalLoadR2/show

    Fixed parameters:
    - documentType: A65 (System total load)
    - processType: A01 (Day ahead)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one day
    """

    code = "6.1.B"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        out_bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize day-ahead total load forecast parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            out_bidding_zone_domain: EIC code of a Control Area, Bidding Zone or Country
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A65",
            process_type="A01",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            out_bidding_zone_domain=out_bidding_zone_domain,
            timeout=timeout,
            offset=offset,
        )


class WeekAheadTotalLoadForecastParams(LoadParams):
    """Parameters for 6.1.C Week-ahead Total Load Forecast.

    Data view:
    https://transparency.entsoe.eu/load-domain/r2/weekLoad/show

    Fixed parameters:
    - documentType: A65 (System total load)
    - processType: A31 (Week ahead)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one week
    """

    code = "6.1.C"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        out_bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize week-ahead total load forecast parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            out_bidding_zone_domain: EIC code of a Control Area, Bidding Zone or Country
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A65",
            process_type="A31",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            out_bidding_zone_domain=out_bidding_zone_domain,
            timeout=timeout,
            offset=offset,
        )


class MonthAheadTotalLoadForecastParams(LoadParams):
    """Parameters for 6.1.D Month-ahead Total Load Forecast.

    Data view:
    https://transparency.entsoe.eu/load-domain/r2/monthLoad/show

    Fixed parameters:
    - documentType: A65 (System total load)
    - processType: A32 (Month ahead)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one month
    """

    code = "6.1.D"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        out_bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize month-ahead total load forecast parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            out_bidding_zone_domain: EIC code of a Control Area, Bidding Zone or Country
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A65",
            process_type="A32",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            out_bidding_zone_domain=out_bidding_zone_domain,
            timeout=timeout,
            offset=offset,
        )


class YearAheadTotalLoadForecastParams(LoadParams):
    """Parameters for 6.1.E Year-ahead Total Load Forecast.

    Data view:
    https://transparency.entsoe.eu/load-domain/r2/yearLoad/show

    Fixed parameters:
    - documentType: A65 (System total load)
    - processType: A33 (Year ahead)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one year
    """

    code = "6.1.E"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        out_bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize year-ahead total load forecast parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            out_bidding_zone_domain: EIC code of a Control Area, Bidding Zone or Country
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A65",
            process_type="A33",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            out_bidding_zone_domain=out_bidding_zone_domain,
            timeout=timeout,
            offset=offset,
        )


class YearAheadForecastMarginParams(LoadParams):
    """Parameters for 8.1 Year-ahead Forecast Margin.

    Data view:
    https://transparency.entsoe.eu/load-domain/r2/marginLoad/show

    Fixed parameters:
    - documentType: A70 (Load forecast margin)
    - processType: A33 (Year ahead)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one year
    """

    code = "8.1"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        out_bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize year-ahead forecast margin parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            out_bidding_zone_domain: EIC code of a Control Area, Bidding Zone or Country
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A70",
            process_type="A33",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            out_bidding_zone_domain=out_bidding_zone_domain,
            timeout=timeout,
            offset=offset,
        )

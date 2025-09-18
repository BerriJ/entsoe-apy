"""Specific parameter classes for ENTSO-E Load endpoints.

This module contains specialized parameter classes for different Load data endpoints,
each inheriting from LoadParams and providing preset values for fixed parameters.
"""

from ..Base.Load import Load


class ActualTotalLoad(Load):
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
        out_bidding_zone_domain: str,
        period_start: int,
        period_end: int,
    ):
        """
        Initialize actual total load parameters.

        Args:
            out_bidding_zone_domain: EIC code of a Control Area, Bidding Zone or Country
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A65",
            process_type="A16",
            out_bidding_zone_domain=out_bidding_zone_domain,
            period_start=period_start,
            period_end=period_end,
        )


class DayAheadTotalLoadForecast(Load):
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
        out_bidding_zone_domain: str,
        period_start: int,
        period_end: int,
    ):
        """
        Initialize day-ahead total load forecast parameters.

        Args:
            out_bidding_zone_domain: EIC code of a Control Area, Bidding Zone or Country
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A65",
            process_type="A01",
            out_bidding_zone_domain=out_bidding_zone_domain,
            period_start=period_start,
            period_end=period_end,
        )


class WeekAheadTotalLoadForecast(Load):
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
        out_bidding_zone_domain: str,
        period_start: int,
        period_end: int,
    ):
        """
        Initialize week-ahead total load forecast parameters.

        Args:
            out_bidding_zone_domain: EIC code of a Control Area, Bidding Zone or Country
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A65",
            process_type="A31",
            out_bidding_zone_domain=out_bidding_zone_domain,
            period_start=period_start,
            period_end=period_end,
        )


class MonthAheadTotalLoadForecast(Load):
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
        out_bidding_zone_domain: str,
        period_start: int,
        period_end: int,
    ):
        """
        Initialize month-ahead total load forecast parameters.

        Args:
            out_bidding_zone_domain: EIC code of a Control Area, Bidding Zone or Country
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A65",
            process_type="A32",
            out_bidding_zone_domain=out_bidding_zone_domain,
            period_start=period_start,
            period_end=period_end,
        )


class YearAheadTotalLoadForecast(Load):
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
        out_bidding_zone_domain: str,
        period_start: int,
        period_end: int,
    ):
        """
        Initialize year-ahead total load forecast parameters.

        Args:
            out_bidding_zone_domain: EIC code of a Control Area, Bidding Zone or Country
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A65",
            process_type="A33",
            out_bidding_zone_domain=out_bidding_zone_domain,
            period_start=period_start,
            period_end=period_end,
        )


class YearAheadForecastMargin(Load):
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
        out_bidding_zone_domain: str,
        period_start: int,
        period_end: int,
    ):
        """
        Initialize year-ahead forecast margin parameters.

        Args:
            out_bidding_zone_domain: EIC code of a Control Area, Bidding Zone or Country
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A70",
            process_type="A33",
            out_bidding_zone_domain=out_bidding_zone_domain,
            period_start=period_start,
            period_end=period_end,
        )

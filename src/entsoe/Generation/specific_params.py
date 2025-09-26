"""Specific parameter classes for ENTSO-E Generation endpoints.

This module contains specialized parameter classes for different Generation data
endpoints, each inheriting from GenerationParams and providing preset values for
fixed parameters.
"""

from typing import Optional

from ..Base.Generation import Generation


class InstalledCapacityPerProductionType(Generation):
    """Parameters for 14.1.A Installed Capacity per Production Type.

    Data view:
    https://transparency.entsoe.eu/generation/r2/installedGenerationCapacityAggregation/show

    Fixed parameters:

    - documentType: A68 (Installed generation per type)
    - processType: A33 (Year ahead)

    Notes:
    - PSR Type is optional - when not specified, all production types are returned
    - Common PSR Types: B01=Biomass, B02=Brown coal, B04=Gas, B05=Hard coal,
      B06=Oil, B10=Hydro Pumped Storage, B11=Hydro Run-of-river,
      B12=Hydro Water Reservoir, B14=Nuclear, B16=Solar,
      B18=Wind Offshore, B19=Wind Onshore, etc.
    """

    code = "14.1.A"

    def __init__(
        self,
        period_start: int,
        period_end: int,
        in_domain: str,
        # Optional generation-specific parameters
        psr_type: Optional[str] = None,
    ):
        """
        Initialize installed capacity per production type parameters.

        Args:
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of a Control Area, Bidding Zone or Country
            psr_type: Power system resource type (B01-B25)
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A68",
            process_type="A33",
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            psr_type=psr_type,
        )


class WaterReservoirsAndHydroStorage(Generation):
    """Parameters for 16.1.D Water Reservoirs and Hydro Storage Plants.

    Data view:
    https://transparency.entsoe.eu/generation/r2/waterReservoirsAndHydroStoragePlants/show

    Fixed parameters:

    - documentType: A72 (Reservoir filling information)
    - processType: A16 (Realised)

    Notes:
    - Returns actual reservoir filling information for hydro storage plants
    - Data represents the actual water levels at specific points in time
    """

    code = "16.1.D"

    def __init__(
        self,
        period_start: int,
        period_end: int,
        in_domain: str,
    ):
        """
        Initialize water reservoirs and hydro storage parameters.

        Args:
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of a Control Area, Bidding Zone or Country
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A72",
            process_type="A16",
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
        )


class ActualGenerationPerProductionType(Generation):
    """Parameters for 16.1.B&C Actual Generation per Production Type.

    Data view:
    https://transparency.entsoe.eu/generation/r2/actualGenerationPerProductionType/show

    Fixed parameters:

    - documentType: A75 (Actual generation per type - all production types)
                   Alternative: A74 (Wind and solar generation only)
    - processType: A16 (Realised)

    Notes:
    - Time series with inBiddingZone_Domain attribute reflects Generation values
    - Time series with outBiddingZone_Domain attribute reflects Consumption values
    - PSR Type is optional - when not specified, all production types are returned
    - API response is same for both A74 and A75 document types
    """

    code = "16.1.B_C"

    def __init__(
        self,
        period_start: int,
        period_end: int,
        in_domain: str,
        # Optional generation-specific parameters
        psr_type: Optional[str] = None,
    ):
        """
        Initialize actual generation per production type parameters.

        Args:
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: Control Area, Bidding Zone, Country
            psr_type: Power system resource type (B01-B25)
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A75",
            process_type="A16",
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            psr_type=psr_type,
        )


class ActualGenerationPerGenerationUnit(Generation):
    """Parameters for 16.1.A Actual Generation per Generation Unit.

    Data view:
    https://transparency.entsoe.eu/generation/r2/actualGenerationPerGenerationUnit/show

    Fixed parameters:

    - documentType: A73 (Actual generation)
    - processType: A16 (Realised)

    Notes:
    - Returns actual generation data for individual generation units
    - Can be filtered by PSR Type and/or specific Registered Resource (generation unit)
    - Provides more granular data than per production type endpoints
    - Maximum time interval: 1 day (API limitation)
    """

    code = "16.1.A"
    max_days_limit: int = (
        1  # Override: Maximum time interval is 1 day for this endpoint
    )

    def __init__(
        self,
        period_start: int,
        period_end: int,
        in_domain: str,
        # Optional generation-specific parameters
        psr_type: Optional[str] = None,
        registered_resource: Optional[str] = None,
    ):
        """
        Initialize actual generation per generation unit parameters.

        Args:
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of a Control Area
            psr_type: Power system resource type (B01-B25)
            registered_resource: EIC Code of a specific Generation Unit
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A73",
            process_type="A16",
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            psr_type=psr_type,
            registered_resource=registered_resource,
        )


class GenerationForecastDayAhead(Generation):
    """Parameters for 14.1.C Generation Forecast - Day ahead.

    Data view:
    https://transparency.entsoe.eu/generation/r2/dayAheadAggregatedGeneration/show

    Fixed parameters:

    - documentType: A71 (Generation forecast)
    - processType: A01 (Day ahead)

    Notes:
    - Returns day-ahead forecasts of total generation
    - Provides aggregated generation forecasts for the next day
    - Used for planning and balancing purposes
    """

    code = "14.1.C"

    def __init__(
        self,
        period_start: int,
        period_end: int,
        in_domain: str,
    ):
        """
        Initialize generation forecast day ahead parameters.

        Args:
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: Control Area, Bidding Zone, Country
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A71",
            process_type="A01",
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
        )


class GenerationForecastWindAndSolar(Generation):
    """Parameters for 14.1.D Generation Forecasts for Wind and Solar.

    Data view:
    https://transparency.entsoe.eu/generation/r2/dayAheadGenerationForecastWindAndSolar/show

    Fixed parameters:

    - documentType: A69 (Wind and solar forecast)
    - processType: A01 (Day ahead), A18 (Current), A40 (Intraday)

    Notes:
    - Specific forecasts for wind and solar generation
    - Can be filtered by PSR Type: B16=Solar, B18=Wind Offshore, B19=Wind Onshore
    - Supports multiple process types: Day ahead, Current, Intraday
    """

    code = "14.1.D"

    def __init__(
        self,
        period_start: int,
        period_end: int,
        in_domain: str,
        # Optional generation-specific parameters
        process_type: str = "A01",  # Default to Day ahead
        psr_type: Optional[str] = None,
    ):
        """
        Initialize generation forecast wind and solar parameters.

        Args:
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of a Control Area, Bidding Zone or Country
            process_type: A01=Day ahead, A18=Current, A40=Intraday
            psr_type: B16=Solar, B18=Wind Offshore, B19=Wind Onshore
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A69",
            process_type=process_type,
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            psr_type=psr_type,
        )


class InstalledCapacityPerProductionUnit(Generation):
    """Parameters for 14.1.B Installed Capacity Per Production Unit.

    Data view:
    https://transparency.entsoe.eu/generation/r2/installedCapacityPerProductionUnit/show

    Fixed parameters:

    - documentType: A71 (Generation forecast)
    - processType: A33 (Year ahead)

    Notes:
    - Returns installed capacity data for individual production units
    - More granular than production type aggregation
    - Can be filtered by PSR Type for specific technology types
    - Uses the same document type as generation forecasts but different process type
    """

    code = "14.1.B"

    def __init__(
        self,
        period_start: int,
        period_end: int,
        in_domain: str,
        # Optional generation-specific parameters
        psr_type: Optional[str] = None,
    ):
        """
        Initialize installed capacity per production unit parameters.

        Args:
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of a Control Area or Bidding Zone
            psr_type: Power system resource type (B01-B25)
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A71",
            process_type="A33",
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            psr_type=psr_type,
        )

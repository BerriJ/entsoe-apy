"""Specific parameter classes for ENTSO-E Master Data endpoints.

This module contains specialized parameter classes for different Master Data
endpoints, each inheriting from Base and providing preset values for fixed
parameters.
"""

from typing import Literal

from ..Base.Base import Base


class ProductionandGenerationUnits(Base):
    """Parameters for Configuration Document (Production Unit).

    This endpoint retrieves configuration information for production units.

    Fixed parameters:

    - documentType: A95 (Configuration document)
    - businessType: B11 (Production unit)

    Notes:
    - PSR Type is optional - filters by production/generation type
    - Available PSR Types:
      B01 = Biomass
      B02 = Fossil Brown coal/Lignite
      B03 = Fossil Coal-derived gas
      B04 = Fossil Gas
      B05 = Fossil Hard coal
      B06 = Fossil Oil
      B07 = Fossil Oil shale
      B08 = Fossil Peat
      B09 = Geothermal
      B10 = Hydro Pumped Storage
      B11 = Hydro Run-of-river and poundage
      B12 = Hydro Water Reservoir
      B13 = Marine
      B14 = Nuclear
      B15 = Other renewable
      B16 = Solar
      B17 = Waste
      B18 = Wind Offshore
      B19 = Wind Onshore
      B20 = Other
    - Implementation date is mandatory and should be in format yyyy-MM-dd (e.g., 2017-01-01)
    - This endpoint does not use period_start/period_end parameters
    """

    code = "A95"
    max_days_limit: int = 36500  # Override: No maximum for this endpoint

    def __init__(
        self,
        bidding_zone_domain: str,
        implementation_date_and_or_time: str,
        psr_type: Literal[
            "B01",  # Biomass
            "B02",  # Fossil Brown coal/Lignite
            "B03",  # Fossil Coal-derived gas
            "B04",  # Fossil Gas
            "B05",  # Fossil Hard coal
            "B06",  # Fossil Oil
            "B07",  # Fossil Oil shale
            "B08",  # Fossil Peat
            "B09",  # Geothermal
            "B10",  # Hydro Pumped Storage
            "B11",  # Hydro Run-of-river and poundage
            "B12",  # Hydro Water Reservoir
            "B13",  # Marine
            "B14",  # Nuclear
            "B15",  # Other renewable
            "B16",  # Solar
            "B17",  # Waste
            "B18",  # Wind Offshore
            "B19",  # Wind Onshore
            "B20",  # Other
        ]
        | None = None,
    ):
        """
        Initialize configuration document parameters.

        Args:
            bidding_zone_domain: EIC code of a Bidding Zone or Control Area (e.g., 10YBE----------2)
            implementation_date_and_or_time: Implementation date in format yyyy-MM-dd (e.g., 2017-01-01)
            psr_type: Power system resource type (B01-B20, optional)
        """
        super().__init__(
            document_type="A95",
            period_start=None,
            period_end=None,
        )

        self.add_business_params(
            business_type="B11",
            psr_type=psr_type,
        )

        self.add_domain_params(bidding_zone_domain=bidding_zone_domain)

        self.add_update_params(
            implementation_date_and_or_time=implementation_date_and_or_time
        )

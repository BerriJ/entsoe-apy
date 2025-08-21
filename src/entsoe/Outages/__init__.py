"""ENTSO-E Outages parameter classes.

This module contains parameter classes for ENTSO-E Outages endpoints,
providing easy-to-use interfaces for different outage data types based on
the ENTSO-E Transparency Platform API specification.
"""

from .specific_params import (
    AggregatedUnavailabilityOfConsumptionUnits,
    Fallbacks,
    UnavailabilityOfGenerationUnits,
    UnavailabilityOfOffshoreGridInfrastructure,
    UnavailabilityOfProductionUnits,
    UnavailabilityOfTransmissionInfrastructure,
)

__all__ = [
    "UnavailabilityOfProductionUnits",
    "UnavailabilityOfGenerationUnits",
    "AggregatedUnavailabilityOfConsumptionUnits",
    "UnavailabilityOfTransmissionInfrastructure",
    "UnavailabilityOfOffshoreGridInfrastructure",
    "Fallbacks",
]

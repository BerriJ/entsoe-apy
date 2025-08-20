"""ENTSO-E Outages parameter classes.

This module contains parameter classes for ENTSO-E Outages endpoints,
providing easy-to-use interfaces for different outage data types.
"""

from .specific_params import (
    ForcedProductionUnitUnavailability,
    ForcedTransmissionUnavailability,
    PlannedProductionUnitUnavailability,
    PlannedTransmissionUnavailability,
    ProductionUnitUnavailability,
    TransmissionUnavailability,
    UnavailabilityTransmissionInfrastructure,
)

__all__ = [
    "PlannedProductionUnitUnavailability",
    "ForcedProductionUnitUnavailability",
    "PlannedTransmissionUnavailability",
    "ForcedTransmissionUnavailability",
    "ProductionUnitUnavailability",
    "TransmissionUnavailability",
    "UnavailabilityTransmissionInfrastructure",
]

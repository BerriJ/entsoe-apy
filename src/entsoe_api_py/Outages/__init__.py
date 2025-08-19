"""ENTSO-E Outages parameter classes.

This module contains parameter classes for ENTSO-E Outages endpoints,
providing easy-to-use interfaces for different outage data types.
"""

from .specific_params import (
    ForcedProductionUnitUnavailabilityParams,
    ForcedTransmissionUnavailabilityParams,
    PlannedProductionUnitUnavailabilityParams,
    PlannedTransmissionUnavailabilityParams,
    ProductionUnitUnavailabilityParams,
    TransmissionUnavailabilityParams,
)

__all__ = [
    "PlannedProductionUnitUnavailabilityParams",
    "ForcedProductionUnitUnavailabilityParams",
    "PlannedTransmissionUnavailabilityParams",
    "ForcedTransmissionUnavailabilityParams",
    "ProductionUnitUnavailabilityParams",
    "TransmissionUnavailabilityParams",
]
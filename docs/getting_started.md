# Getting Started

This guide will help you get started with the ENTSO-E API Python library.

## Prerequisites

- Python 3.8 or higher
- An ENTSO-E Transparency Platform API security token

## Getting Your API Token

1. Register at the [ENTSO-E Transparency Platform](https://transparency.entsoe.eu/)
2. Navigate to your account settings
3. Generate a new security token
4. Keep this token secure - you'll need it for all API requests

## Installation

Install the library using pip:

```bash
pip install entsoe-api-py
```

## Basic Usage

### Traditional Class Import

```python
from entsoe_api_py.Items import AcceptedAggregatedOffers

# Create parameter object
params = AcceptedAggregatedOffers(
    security_token="your-security-token-here",
    period_start=202301010000,  # YYYYMMDDHHMM format
    period_end=202301020000,
    bidding_zone_domain="10Y1001A1001A83F"  # EIC code for bidding zone
)
```

### Code-Based Access

The library provides a unique feature where you can access classes using their ENTSO-E codes:

```python
# Access using ENTSO-E code structure
from entsoe_api_py.Items import _17
AcceptedAggregatedOffers = _17._1.D

# Or for other codes
from entsoe_api_py.Items import _12
CurrentBalancingState = _12._3.A
```

### Using the Utility Function

```python
from entsoe_api_py.Items import get_class_by_code

# Get class by code string
cls = get_class_by_code("17.1.D")
params = cls(
    security_token="your-token",
    period_start=202301010000,
    period_end=202301020000,
    bidding_zone_domain="10Y1001A1001A83F"
)
```

## Understanding EIC Codes

EIC (Energy Identification Code) codes are used to identify different entities in the European energy market:

- **Bidding Zones**: Geographic areas for electricity trading
- **Control Areas**: Areas managed by transmission system operators
- **Market Balance Areas**: Areas for balancing supply and demand

Common EIC codes include:
- `10Y1001A1001A83F` - Germany/Luxembourg
- `10YFR-RTE------C` - France
- `10YGB----------A` - Great Britain

## Time Formats

The API uses a specific time format: `YYYYMMDDHHMM`

Examples:
- `202301010000` - January 1, 2023, 00:00
- `202312311200` - December 31, 2023, 12:00

## Next Steps

- Explore the [API Reference](items.md) for all available parameter classes
- Check out [Examples](examples.md) for more complex use cases
- Learn about [Balancing](balancing.md) parameters specifically

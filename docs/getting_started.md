# Getting Started

This guide will help you get started with the ENTSO-E API Python library.

## Prerequisites

- Python 3.11 or higher
- An ENTSO-E Transparency Platform API security token

## Installation

Install the library using pip:

```sh
pip install entsoe-apy
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

## Understanding EIC Codes

EIC (Energy Identification Code) codes are used to identify different entities in the European energy market:

- **Bidding Zones**: Geographic areas for electricity trading
- **Control Areas**: Areas managed by transmission system operators
- **Market Balance Areas**: Areas for balancing supply and demand
- **Countries**: National boundaries for electricity trading

You can see the complete list of EIC codes [here](https://transparencyplatform.zendesk.com/hc/en-us/articles/15885757676308-Area-List-with-Energy-Identification-Code-EIC).

A python dictionary representing the EIC mapping can be accessed using:

```python
from entsoe-apy import mappings
```

## Time Formats

The API uses a specific time format: `YYYYMMDDHHMM`

Examples:
- `202301010000` - January 1, 2023, 00:00
- `202312311200` - December 31, 2023, 12:00

## Next Steps

- Explore the [API Reference](items.md) for all available parameter classes
- Check out [Examples](examples.md) for more complex use cases
- Learn about [Balancing](balancing.md) parameters specifically

# ENTSO-E API Python

A Python library for accessing ENTSO-E Transparency Platform API endpoints.

## Overview

This library provides a convenient Python interface to the ENTSO-E (European Network of Transmission System Operators for Electricity) Transparency Platform API. It allows you to easily fetch various types of electricity market data including balancing information, generation data, and more.

## Key Features

- **Code-based Access**: Access parameter classes using their ENTSO-E codes (e.g., `17.1.D` for Accepted Aggregated Offers)
- **Type Safety**: Full type hints for better development experience
- **Comprehensive Coverage**: Support for various ENTSO-E data categories
- **Easy to Use**: Simple and intuitive API design

## Quick Start

```python
from entsoe_api_py.Items import AcceptedAggregatedOffers

# Traditional import
params = AcceptedAggregatedOffers(
    security_token="your-token",
    period_start=202301010000,
    period_end=202301020000,
    bidding_zone_domain="10Y1001A1001A83F"
)

# Code-based access
from entsoe_api_py.Items import _17
cls = _17._1.D  # Same as AcceptedAggregatedOffers
```

## Installation

```bash
pip install entsoe-api-py
```

## Next Steps

- [Getting Started](getting_started.md) - Learn how to set up and use the library
- [API Reference](items.md) - Detailed documentation of all available classes
- [Examples](examples.md) - Practical examples and use cases

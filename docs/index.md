# ENTSO-E API Python

A Python library for accessing ENTSO-E Transparency Platform API endpoints.

## Overview

This library provides a convenient Python interface to the ENTSO-E (European Network of Transmission System Operators for Electricity) Transparency Platform API. It allows you to easily fetch the data using a simple and intuitive interface. The retrieved data is automatically validated against the data-models published by ENTSO-E.

## Key Features

- **Intuitive Design**: Highly consistent with the API documentation
- **Comprehensive Coverage**: Support for all ENTSO-E data categories (except MasterData)
- **Easy to Use**: Simple and intuitive design

## Quick Start

The package structure mirrors the [official ENTSO-E API documentation](https://documenter.getpostman.com/view/7009892/2s93JtP3F6).

```python
# Import item from the Market Group
from entsoe_api_py.Market import EnergyPrices

EIC = "10Y1001A1001A82H"

# Initialize
object = EnergyPrices(
    security_token=_ENTSOE_API,
    in_domain=EIC,
    out_domain=EIC,
    period_start=202012312300,
    period_end=202101022300,
)

# Query
result = object.query_api()
```

The structure of the `result` object depends on the `xsd` schmema provided by ENTSO-E.
The Docs will be extended with examples on how to extract the actual data from `result`.

## Installation

```bash
pip install entsoe-apy
```

## Next Steps

- [Getting Started](getting_started.md) - Learn how to set up and use the library
- [Examples](examples.md) - Practical examples and use cases

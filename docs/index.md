# ENTSO-E API Python Package

A Python library for accessing ENTSO-E Transparency Platform API endpoints.

## Highlights

- Easy access to ENTSO-E Transparency Platform API endpoints
- Supports all major API functionalities
- Well-documented, easy to use and highly consistent with the API
- Automatically splits up large requests into multiple smaller calls to the API
- Retries on connection errors
- Returns meaningful error messages if something goes wrong

## Install

Install the package from pypi using pip:

```sh
pip install entsoe-apy
```

## Quick Start

### API Key

You need an ENTSOE API Key (also called token) refer to the [official documentation](https://transparencyplatform.zendesk.com/hc/en-us/articles/12845911031188-How-to-get-security-token) on how to obtain it. The package expects an environment variable called `ENTSOE_API` to be set with your API key. See [Configuration](./configuration.md) for more details and options.

### Query Day-Ahead Prices

The package structure mirrors the [official ENTSO-E API docs](https://documenter.getpostman.com/view/7009892/2s93JtP3F6). So for querying "12.1.D Energy Prices" we need the `entsoe.Market` module and use the `EnergyPrices` class.

After initializing the class, we can query the data using the query_data method.

```python
# Import item from the Market Group
from entsoe.Market import EnergyPrices

EIC = "10Y1001A1001A82H" # DE-AT Biddingzone

period_start = 201512312300
period_end = 202107022300

ep = EnergyPrices(
    in_domain=EIC,
    out_domain=EIC,
    period_start=period_start,
    period_end=period_end,
    contract_market_agreement_type="A01",
)
result = ep.query_api()
```

The structure of the `result` object depends on the queried data. See the [examples](./examples.md) for more details.

## Working with API Results

### JSON Serialization

API results are returned as Pydantic models that support JSON serialization. You can export your data to JSON format using the built-in `model_dump_json()` method:

```python
# Convert the result to JSON string
json_string = result.model_dump_json(indent=2)

# Or convert to Python dict first, then to JSON
result_dict = result.model_dump(mode="json")
```

The `model_dump_json()` method accepts several parameters:
- `indent`: Pretty-print with specified indentation
- `exclude`: Fields to exclude from the output
- `include`: Only include specific fields
- `by_alias`: Use field aliases if defined

For more complex data processing, consider using the `extract_records()` utility function which flattens nested data structures into pandas-compatible records:

```python
from entsoe.utils import extract_records

# Convert to flattened records suitable for pandas DataFrame
records = extract_records(result)
```

## Next Steps

- [ENTSOE](./ENTSOE/index.md) - Class documentation
- [Examples](./examples.md) - Practical examples and use cases


## Contributions

Contributions are welcome! Please open an issue or submit a pull request.
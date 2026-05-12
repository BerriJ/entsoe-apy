# Examples

This page provides practical examples for using the ENTSO-E API Python package.

All available endpoints are listed in [ENTSOE Overview](./ENTSOE/index.md) and a dictionary with EIC codes and their corresponding names and tags can be found in [Mappings](./mappings.md).

## Working with API Results

### Converting Results to DataFrames

All API results are returned as Pydantic models with nested structures. To convert them into flat records suitable for pandas DataFrames, use the `extract_records()` function:

```python
from pandas import DataFrame
from entsoe.Market import EnergyPrices
from entsoe.utils import extract_records, add_timestamps

# Query energy prices
result = EnergyPrices(
    in_domain="10YNL----------L", # Netherlands
    out_domain="10YNL----------L",
    period_start=202012312300,
    period_end=202101022300,
).query_api()

# Convert to DataFrame-ready records
records = extract_records(result)
records = add_timestamps(records)
df = DataFrame(records)
```

!!! note
    The [`extract_records`](utilities.md#entsoe.utils.extract_records) function automatically removes `m_rid` and `time_series.m_rid` metadata fields. This mitigates duplicates due to internal splitting of queries, see [#68](https://github.com/BerriJ/entsoe-apy/issues/68). You may extend the `ignore_fields` parameter as needed (for exampe with `"created_date_time", "time_period_time_interval.start","time_period_time_interval.end"`).
     See [`extract_records`](utilities.md#entsoe.utils.extract_records) for more details.

See also [Utilities](./utilities.md) for more details on the utility functions.

### Working with datetime and timezones

The ENTSO-E API is (usually) expecting UTC timestamps but the European power markets operate on a Europe/Berlin basis. We can use the `format_entsoe_datetime` function to convert `datetime` and `pandas` timestamps in the API interface. The function handles time zone information and parses `datetime` derived types to the respective integer. Timezone-naive timestamps are assumed to be in UTC.

```python
import pandas as pd
from entsoe.Market import EnergyPrices
from entsoe.utils import (
    extract_records, 
    add_timestamps, 
    format_entsoe_datetime
)

period_start = pd.Timestamp("2024-02-01", tz="Europe/Berlin")
period_end = pd.Timestamp("2024-02-02", tz="Europe/Berlin")

# Query energy prices
result = EnergyPrices(
    in_domain="10YNL----------L", # Netherlands
    out_domain="10YNL----------L",
    period_start=format_entsoe_datetime(period_start),
    period_end=format_entsoe_datetime(period_end),
).query_api()

records = extract_records(result)
records = add_timestamps(records)
df = pd.DataFrame(records)
df = df.convert_dtypes()
```


### Extracting Specific Domains

You can extract specific parts of the result by specifying a domain:

```python
# Extract only time series data
time_series_records = extract_records(result, domain="time_series")
time_series_df = DataFrame(time_series_records)
```

### JSON Export and Import

All API result objects are Pydantic models that provide built-in JSON serialization. Use the `model_dump_json()` method to convert results to JSON:

```python
# Convert with indentation for pretty printing
import json

pydantic_model = result[0]
json_dict = pydantic_model.model_dump(mode="json")
pretty_json = json.dumps(json_dict, indent=2)
print(pretty_json)
```

### Advanced JSON Options

The `model_dump_json()` method supports various options for customization:

```python
# Include None values (excluded by default)
json_with_none = pydantic_model.model_dump_json(exclude_none=False)

# Exclude specific fields
json_filtered = pydantic_model.model_dump_json(exclude={"mrid", "created_date_time"})

# Include only specific fields
json_minimal = pydantic_model.model_dump_json(include={"time_series", "period"})

# Use different serialization mode
json_python = pydantic_model.model_dump_json(mode="python")  # Uses Python types
```


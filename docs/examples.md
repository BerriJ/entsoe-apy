# Examples

This page provides practical examples for using the ENTSO-E API Python package.

## Working with API Results

### Converting Results to DataFrames

All API results are returned as Pydantic models with nested structures. To convert them into flat records suitable for pandas DataFrames, use the `extract_records()` function:

```python
from pandas import DataFrame
from entsoe.Market import EnergyPrices
from entsoe.utils import extract_records

# Query energy prices
result = EnergyPrices(
    in_domain="10Y1001A1001A82H",  # DE-LU
    out_domain="10Y1001A1001A82H",
    period_start=202012312300,
    period_end=202101022300,
).query_api()

# Convert to DataFrame-ready records
records = extract_records(result)
df = DataFrame(records)

# Display the DataFrame
print(df.head())
```

The `extract_records()` function:
- Flattens nested dictionary structures using dot notation (e.g., `time_series.period.point.position`)
- Expands lists into multiple records (one per list element)
- Creates cross-products when multiple lists exist at the same level
- Handles complex nested data automatically

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


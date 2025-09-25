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

# Extract only period data (if available)
try:
    period_records = extract_records(result, domain="period")
    period_df = DataFrame(period_records)
except KeyError as e:
    print(f"Domain not found: {e}")
```

### JSON Export and Import

All API result objects are Pydantic models that provide built-in JSON serialization. Use the `model_dump_json()` method to convert results to JSON:

```python
# Convert result to compact JSON string
json_string = result.model_dump_json()

# Convert with indentation for pretty printing
import json
json_dict = result.model_dump()
pretty_json = json.dumps(json_dict, indent=2)
print(pretty_json)

# Save to file
with open("energy_prices.json", "w") as f:
    f.write(result.model_dump_json())

# Load from JSON (requires reconstructing the model)
with open("energy_prices.json", "r") as f:
    data = json.load(f)
    # Note: You'll need to reconstruct the appropriate Pydantic model
```

### Advanced JSON Options

The `model_dump_json()` method supports various options for customization:

```python
# Include None values (excluded by default)
json_with_none = result.model_dump_json(exclude_none=False)

# Exclude specific fields
json_filtered = result.model_dump_json(exclude={"mrid", "created_date_time"})

# Include only specific fields
json_minimal = result.model_dump_json(include={"time_series", "period"})

# Use different serialization mode
json_python = result.model_dump_json(mode="python")  # Uses Python types
```

## Common Patterns

### Handling Large Date Ranges

The package automatically splits large requests into smaller chunks:

```python
from entsoe.Market import EnergyPrices

# This will be automatically split into multiple API calls
result = EnergyPrices(
    in_domain="10Y1001A1001A82H",
    out_domain="10Y1001A1001A82H", 
    period_start=202001010000,  # 1 year range
    period_end=202012312300,
).query_api()

# Convert all results to a single DataFrame
all_records = extract_records(result)
df = DataFrame(all_records)
```

### Error Handling

```python
try:
    result = EnergyPrices(
        in_domain="INVALID_EIC",
        out_domain="10Y1001A1001A82H",
        period_start=202012312300,
        period_end=202101022300,
    ).query_api()
except ValueError as e:
    print(f"Invalid EIC code: {e}")
except Exception as e:
    print(f"API error: {e}")
```

### Working with Different Data Types

```python
from entsoe.Generation import ActualGeneration
from entsoe.Load import DayAheadForecast

# Generation data
gen_result = ActualGeneration(
    in_domain="10Y1001A1001A82H",
    period_start=202012312300,
    period_end=202101022300,
).query_api()

# Load forecast data  
load_result = DayAheadForecast(
    out_domain="10Y1001A1001A82H",
    period_start=202012312300,
    period_end=202101022300,
).query_api()

# Convert both to DataFrames
gen_df = DataFrame(extract_records(gen_result))
load_df = DataFrame(extract_records(load_result))
```
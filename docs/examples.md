# Examples

This page provides practical examples of using the ENTSO-E API Python library.

## Basic Usage Examples

### Fetching Accepted Aggregated Offers

```python
from entsoe_api_py.Items import AcceptedAggregatedOffers

# Create parameters for fetching data
params = AcceptedAggregatedOffers(
    security_token="your-security-token",
    period_start=202301010000,  # January 1, 2023, 00:00
    period_end=202301020000,    # January 2, 2023, 00:00
    bidding_zone_domain="10Y1001A1001A83F",  # Germany/Luxembourg
    business_type="A95"  # Frequency containment reserve
)
```

### Using Code-Based Access

```python
# Access by ENTSO-E code
from entsoe_api_py.Items import _17
AcceptedAggregatedOffers = _17._1.D

params = AcceptedAggregatedOffers(
    security_token="your-token",
    period_start=202301010000,
    period_end=202301020000,
    bidding_zone_domain="10Y1001A1001A83F"
)
```

### Dynamic Class Selection

```python
from entsoe_api_py.Items import get_class_by_code

# Dynamically select class based on code
code = "17.1.D"
param_class = get_class_by_code(code)

params = param_class(
    security_token="your-token",
    period_start=202301010000,
    period_end=202301020000,
    bidding_zone_domain="10Y1001A1001A83F"
)
```

## Advanced Examples

### Working with Multiple Time Periods

```python
from entsoe_api_py.Items import ImbalancePrices
from datetime import datetime, timedelta

def get_imbalance_prices_for_week(start_date, bidding_zone):
    """Fetch imbalance prices for a full week."""
    results = []
    
    current_date = start_date
    for day in range(7):
        period_start = int(current_date.strftime("%Y%m%d0000"))
        period_end = int((current_date + timedelta(days=1)).strftime("%Y%m%d0000"))
        
        params = ImbalancePrices(
            security_token="your-token",
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone
        )
        
        results.append(params)
        current_date += timedelta(days=1)
    
    return results

# Usage
start = datetime(2023, 1, 1)
weekly_params = get_imbalance_prices_for_week(start, "10Y1001A1001A83F")
```

### Cross-Border Balancing

```python
from entsoe_api_py.Items import CrossBorderBalancing

# Fetch cross-border balancing data between two areas
params = CrossBorderBalancing(
    security_token="your-token",
    period_start=202301010000,
    period_end=202301020000,
    acquiring_domain="10Y1001A1001A83F",  # Germany/Luxembourg
    connecting_domain="10YFR-RTE------C"  # France
)
```

### Working with IF Codes

```python
from entsoe_api_py.Items import IF

# Access classes with IF codes
NettedAndExchangedVolumes = IF._3_10_3_16_3_17

params = NettedAndExchangedVolumes(
    security_token="your-token",
    period_start=202301010000,
    period_end=202301020000,
    acquiring_domain="10Y1001A1001A83F",
    connecting_domain="10YFR-RTE------C"
)
```

## Common EIC Codes

Here are some commonly used EIC codes for different bidding zones:

| Country/Region     | EIC Code           | Description                    |
| ------------------ | ------------------ | ------------------------------ |
| Germany/Luxembourg | `10Y1001A1001A83F` | German/Luxembourg bidding zone |
| France             | `10YFR-RTE------C` | French bidding zone            |
| Great Britain      | `10YGB----------A` | Great Britain bidding zone     |
| Netherlands        | `10YNL----------L` | Dutch bidding zone             |
| Belgium            | `10YBE----------2` | Belgian bidding zone           |
| Austria            | `10YAT-APG------L` | Austrian bidding zone          |
| Switzerland        | `10YCH-SWISSGRIDK` | Swiss bidding zone             |
| Italy              | `10YIT-GRTN-----B` | Italian bidding zone           |

## Time Period Helpers

```python
from datetime import datetime

def create_time_period(year, month, day, hour=0, minute=0):
    """Helper function to create time periods in the correct format."""
    dt = datetime(year, month, day, hour, minute)
    return int(dt.strftime("%Y%m%d%H%M"))

# Examples
start_time = create_time_period(2023, 1, 1, 0, 0)    # 202301010000
end_time = create_time_period(2023, 1, 1, 23, 59)    # 202301012359
```

## Error Handling

```python
from entsoe_api_py.Items import get_class_by_code

def safe_get_class(code):
    """Safely get a class by code with error handling."""
    try:
        return get_class_by_code(code)
    except KeyError:
        print(f"Code '{code}' not found. Available codes:")
        from entsoe_api_py.Items import list_available_codes
        list_available_codes()
        return None

# Usage
cls = safe_get_class("17.1.D")
if cls:
    params = cls(
        security_token="your-token",
        period_start=202301010000,
        period_end=202301020000,
        bidding_zone_domain="10Y1001A1001A83F"
    )
```

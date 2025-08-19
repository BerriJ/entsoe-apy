# Items API Reference

The Items module provides access to all ENTSO-E API parameter classes, both through traditional imports and code-based access.

## Overview

The `entsoe_api_py.Items` module contains all parameter classes for accessing ENTSO-E API endpoints. It provides two main ways to access these classes:

1. **Traditional imports**: Import classes by their descriptive names
2. **Code-based access**: Access classes using their ENTSO-E codes

## Code-Based Access

The library provides a unique way to access parameter classes using their ENTSO-E codes. This allows for more intuitive imports when you know the specific ENTSO-E code you need.

### Numerical Codes

For numerical codes like `17.1.D`, you can access them using underscore-prefixed attributes:

```python
from entsoe_api_py.Items import _17
AcceptedAggregatedOffers = _17._1.D
```

### IF Codes

For codes starting with "IF_", you can access them through the `IF` module:

```python
from entsoe_api_py.Items import IF
NettedAndExchangedVolumes = IF._3_10_3_16_3_17
```

## Available Classes

### Balancing Data (17.1.x)

- **AcceptedAggregatedOffers** (`17.1.D`): Accepted aggregated offers for balancing services
- **ActivatedBalancingEnergy** (`17.1.E`): Activated balancing energy data
- **PricesOfActivatedBalancingEnergy** (`17.1.F`): Prices of activated balancing energy
- **ImbalancePrices** (`17.1.G`): Imbalance prices for bidding zones
- **TotalImbalanceVolumes** (`17.1.H`): Total imbalance volumes
- **FinancialExpensesAndIncomeForBalancing** (`17.1.I`): Financial data for balancing
- **CrossBorderBalancing** (`17.1.J`): Cross-border balancing activities

### Capacity Data (12.3.x)

- **CurrentBalancingState** (`12.3.A`): Current balancing state information
- **BalancingEnergyBids** (`12.3.B_C`): Balancing energy bids
- **AggregatedBalancingEnergyBids** (`12.3.E`): Aggregated balancing energy bids
- **ProcuredBalancingCapacity** (`12.3.F`): Procured balancing capacity
- **AllocationAndUseOfCrossZonalBalancingCapacity** (`12.3.H_I`): Cross-zonal balancing capacity

### Reserve Data (18x.x)

- **FCRTotalCapacity** (`187.2`): Total FCR capacity
- **SharesOfFCRCapacity** (`187.2_Shares`): Shares of FCR capacity
- **FRRAndRRCapacityOutlook** (`188.3_189.2`): FRR and RR capacity outlook
- **FRRAndRRActualCapacity** (`188.4_189.3`): Actual FRR and RR capacity

## Utility Functions

### get_class_by_code(code)

Retrieve a parameter class by its ENTSO-E code string.

```python
from entsoe_api_py.Items import get_class_by_code

cls = get_class_by_code("17.1.D")
# Returns AcceptedAggregatedOffers class
```

### list_available_codes()

Print all available ENTSO-E codes and their corresponding class names.

```python
from entsoe_api_py.Items import list_available_codes

list_available_codes()
# Prints a list of all codes and classes
```

## Usage Examples

### Traditional Import

```python
from entsoe_api_py.Items import AcceptedAggregatedOffers

params = AcceptedAggregatedOffers(
    security_token="your-token",
    period_start=202301010000,
    period_end=202301020000,
    bidding_zone_domain="10Y1001A1001A83F"
)
```

### Code-Based Access

```python
from entsoe_api_py.Items import _17
cls = _17._1.D  # AcceptedAggregatedOffers

params = cls(
    security_token="your-token",
    period_start=202301010000,
    period_end=202301020000,
    bidding_zone_domain="10Y1001A1001A83F"
)
```

### Dynamic Access

```python
from entsoe_api_py.Items import get_class_by_code

code = "17.1.D"
cls = get_class_by_code(code)

params = cls(
    security_token="your-token",
    period_start=202301010000,
    period_end=202301020000,
    bidding_zone_domain="10Y1001A1001A83F"
)
```

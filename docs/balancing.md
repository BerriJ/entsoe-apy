# Balancing Parameters

This page provides detailed information about balancing-related parameter classes.

## Overview

The balancing module contains parameter classes for accessing various balancing data from the ENTSO-E Transparency Platform. These classes are designed to handle different types of balancing information including energy bids, capacity data, and pricing information.

## Balancing Categories

### 17.1.x - Balancing Data

These endpoints provide data related to balancing markets and operations:

#### 17.1.D - Accepted Aggregated Offers

Parameters for accessing accepted aggregated offers data.

**Fixed parameters:**
- documentType: A82 (Accepted offers)

**Optional parameters:**
- businessType: A95=FCR, A96=aFRR, A97=mFRR, A98=RR

#### 17.1.E - Activated Balancing Energy

Parameters for accessing activated balancing energy data.

**Fixed parameters:**
- documentType: A83 (Activated balancing quantities)

#### 17.1.F - Prices of Activated Balancing Energy

Parameters for accessing prices of activated balancing energy.

**Fixed parameters:**
- documentType: A84 (Activated balancing prices)

**Required parameters:**
- processType: A16=Realised, A60=Scheduled activation mFRR, A61=Direct activation mFRR, A68=Local Selection aFRR

#### 17.1.G - Imbalance Prices

Parameters for accessing imbalance prices.

**Fixed parameters:**
- documentType: A85 (Imbalance prices)

#### 17.1.H - Total Imbalance Volumes

Parameters for accessing total imbalance volumes.

**Fixed parameters:**
- documentType: A86 (Imbalance volume)

### 12.3.x - Balancing Capacity

These endpoints provide information about balancing capacity and bids:

#### 12.3.A - Current Balancing State

Parameters for accessing current balancing state information.

**Fixed parameters:**
- documentType: A86 (Imbalance volume)
- businessType: B33 (Area Control Error)

#### 12.3.B_C - Balancing Energy Bids

Parameters for accessing balancing energy bids.

**Fixed parameters:**
- documentType: A37 (Reserve bid document)
- businessType: B74 (Offer)

#### 12.3.E - Aggregated Balancing Energy Bids

Parameters for accessing aggregated balancing energy bids.

**Fixed parameters:**
- documentType: A24 (Bid document)

#### 12.3.F - Procured Balancing Capacity

Parameters for accessing procured balancing capacity.

**Fixed parameters:**
- documentType: A15 (Acquiring system operator reserve schedule)

### Reserve Types

The balancing parameters support different types of reserves:

- **FCR** (A95): Frequency Containment Reserve
- **aFRR** (A96): Automatic Frequency Restoration Reserve  
- **mFRR** (A97): Manual Frequency Restoration Reserve
- **RR** (A98): Replacement Reserve

## Common Usage Patterns

### Basic Balancing Data Query

```python
from entsoe_api_py.Items import AcceptedAggregatedOffers

params = AcceptedAggregatedOffers(
    security_token="your-token",
    period_start=202301010000,
    period_end=202301020000,
    bidding_zone_domain="10Y1001A1001A83F",
    business_type="A95"  # FCR
)
```

### Cross-Border Balancing

```python
from entsoe_api_py.Items import CrossBorderBalancing

params = CrossBorderBalancing(
    security_token="your-token",
    period_start=202301010000,
    period_end=202301020000,
    acquiring_domain="10Y1001A1001A83F",
    connecting_domain="10YFR-RTE------C"
)
```

### Process Types for Pricing Data

```python
from entsoe_api_py.Items import PricesOfActivatedBalancingEnergy

# Different process types for different activation mechanisms
params = PricesOfActivatedBalancingEnergy(
    security_token="your-token",
    period_start=202301010000,
    period_end=202301020000,
    bidding_zone_domain="10Y1001A1001A83F",
    process_type="A16",  # Realised
    business_type="A96"  # aFRR
)
```

## Parameter Reference

### Common Parameters

All balancing parameter classes share these common parameters:

- `security_token`: Your ENTSO-E API security token
- `period_start`: Start time in YYYYMMDDHHMM format
- `period_end`: End time in YYYYMMDDHHMM format
- `bidding_zone_domain`: EIC code of the bidding zone
- `timeout`: Request timeout in seconds (default: 60)
- `offset`: Pagination offset (optional)

### Specialized Parameters

Some classes require additional parameters:

- **Cross-border queries**: `acquiring_domain` and `connecting_domain`
- **Process-specific queries**: `process_type` parameter
- **Business type filtering**: `business_type` parameter

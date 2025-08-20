# Base Classes

This page documents the base classes that form the foundation of the ENTSO-E API Python library.

## Overview

The base classes provide common functionality and structure for all parameter classes in the library. They handle common parameters, validation, and provide the foundation for the API interactions.

## Balancing Base Class

The `Balancing` class serves as the base class for all balancing-related parameter classes. It provides:

- Common parameter handling
- Parameter validation
- Consistent initialization patterns
- Shared functionality across all balancing endpoints

### Common Parameters

All classes inheriting from `Balancing` support these parameters:

- `security_token`: ENTSO-E API security token (required)
- `period_start`: Start time in YYYYMMDDHHMM format (required)
- `period_end`: End time in YYYYMMDDHHMM format (required)
- `timeout`: Request timeout in seconds (default: 60)
- `offset`: Pagination offset (optional)

### Domain Parameters

Different endpoints require different domain parameters:

- `bidding_zone_domain`: EIC code for single-zone queries
- `acquiring_domain` and `connecting_domain`: EIC codes for cross-border queries

## Common Patterns

### Parameter Inheritance

All specific parameter classes inherit from the base `Balancing` class:

```python
class AcceptedAggregatedOffers(Balancing):
    """Parameters for 17.1.D Accepted Aggregated Offers."""
    
    code = "17.1.D"
    
    def __init__(self, ...):
        super().__init__(
            document_type="A82",  # Fixed parameter
            # ... other parameters
        )
```

### Fixed Parameters

Each parameter class sets appropriate fixed parameters for its specific endpoint:

- `document_type`: Specifies the type of document being requested
- `business_type`: May be fixed for certain endpoints
- `process_type`: Required for some specific data types

### Parameter Validation

The base classes handle validation of:

- Required parameters
- Time format validation (YYYYMMDDHHMM)
- EIC code format validation
- Parameter type checking

## Development Notes

When extending the library with new parameter classes:

1. Inherit from the appropriate base class
2. Set the `code` attribute to the ENTSO-E code
3. Define fixed parameters in the `__init__` method
4. Call `super().__init__()` with all parameters
5. Add comprehensive docstrings with data view links

### Example Implementation

```python
class NewParameterClass(Balancing):
    """Parameters for X.Y.Z New Endpoint.
    
    Data view:
    https://transparency.entsoe.eu/path/to/view
    
    Fixed parameters:
    - documentType: AXX (Description)
    """
    
    code = "X.Y.Z"
    
    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        timeout: int = 5,
        offset: int = 0,
    ):
        super().__init__(
            document_type="AXX",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            timeout=timeout,
            offset=offset,
        )
```

# Configuration

This page describes how to configure the ENTSO-E API Python library, including API key management and network settings.

## Overview

The library uses a global configuration system that allows you to set common parameters once and reuse them across all API calls. This configuration includes:

- **API Key (Security Token)**: Required for authentication with the ENTSO-E Transparency Platform
- **API Endpoint URL**: The base URL for the ENTSO-E API (configurable via `ENTSOE_ENDPOINT_URL`)
- **Timeout**: HTTP request timeout duration
- **Retries**: Number of retry attempts for failed requests
- **Retry Delay Function**: Function that determines wait time between retry attempts (supports exponential backoff)
- **Log Level**: Configurable logging level for controlling output verbosity
- **Number of Workers**: How many concurrent requests can be made

## API Key Management

### Using Environment Variables (Recommended)

The easiest way to set your API key is using an environment variable:

```bash
export ENTSOE_API="your-security-token-here"
```

When the library is imported, it automatically checks for the `ENTSOE_API` environment variable:

```python
import entsoe
# The library automatically loads the API key from ENTSOE_API environment variable
```

The above is sufficient for most use cases.

### Manual Configuration

You can also set the API key programmatically using the `set_config()` function:

```python
import entsoe

# Set global configuration
entsoe.config.set_config(security_token="your-security-token-here")
```

!!! note "API Key Priority"
    The library checks for API keys in this order:
    1. Global configuration (`entsoe.config.set_config()`)
    2. Environment variable (`ENTSOE_API`)
    
    All parameter classes use the global configuration - there is no per-request API key option.

## API Endpoint Configuration

The library uses `https://web-api.tp.entsoe.eu/api` by default. You can customize this using the `ENTSOE_ENDPOINT_URL` environment variable:

```bash
export ENTSOE_ENDPOINT_URL="https://custom-api.example.com/api"
```

Or programmatically:

```python
entsoe.config.set_config(endpoint_url="https://custom-api.example.com/api")
```

## References:

::: entsoe.config.set_config

::: entsoe.config.get_config

## Related Documentation

- [Examples](examples.md) - Practical usage examples
- [ENTSOE](./ENTSOE/index.md) - Class documentation
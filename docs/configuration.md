# Configuration

This page describes how to configure the ENTSO-E API Python library, including API key management and network settings.

## Overview

The library uses a global configuration system that allows you to set common parameters once and reuse them across all API calls. This configuration includes:

- **API Key (Security Token)**: Required for authentication with the ENTSO-E Transparency Platform
- **Timeout**: HTTP request timeout duration
- **Retries**: Number of retry attempts for failed requests
- **Retry Delay**: Wait time between retry attempts

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

### Manual Configuration

You can also set the API key programmatically using the `set_config()` function:

```python
import entsoe

# Set global configuration
entsoe.set_config(security_token="your-security-token-here")
```

!!! note "API Key Priority"
    The library checks for API keys in this order:
    1. Global configuration (`entsoe.set_config()`)
    2. Environment variable (`ENTSOE_API`)
    
    All parameter classes use the global configuration - there is no per-request API key option.

## Network Configuration

### Timeout Settings

The **timeout** parameter controls how long to wait for HTTP responses from the ENTSO-E API.

**Default**: 5 seconds

```python
import entsoe

# Set a longer timeout for slow connections
entsoe.set_config(
    security_token="your-token",
    timeout=30  # 30 seconds
)
```

**What it does**: If the ENTSO-E API doesn't respond within the specified time, the request will fail with a timeout error.

**When to adjust**: 
- Increase for slow or unreliable internet connections
- Decrease for applications that need fast failure detection

### Retry Configuration

The **retries** parameter controls how many times to retry failed requests.

**Default**: 3 attempts

```python
import entsoe

# Increase retry attempts for better reliability
entsoe.set_config(
    security_token="your-token",
    retries=5  # Retry up to 5 times
)
```

**What it does**: When a request fails due to network issues (connection errors, timeouts), the library automatically retries the request up to the specified number of times.

**When to adjust**:
- Increase for better reliability in unstable network conditions
- Decrease to fail faster when network issues occur

### Retry Delay

The **retry_delay** parameter controls how long to wait between retry attempts.

**Default**: 10 seconds

```python
import entsoe

# Reduce delay between retries for faster responses
entsoe.set_config(
    security_token="your-token",
    retry_delay=5  # Wait 5 seconds between retries
)
```

**What it does**: When a request fails and needs to be retried, the library waits this many seconds before attempting the next retry.

**When to adjust**:
- Increase to be more respectful to the ENTSO-E API servers
- Decrease for faster retry cycles (but be mindful of API rate limits)

## Complete Configuration Examples

### Basic Setup

```python
import entsoe

# Basic configuration with API key
entsoe.set_config(security_token="your-security-token-here")
```

### Production Setup

```python
import entsoe

# Production configuration with increased reliability
entsoe.set_config(
    security_token="your-security-token-here",
    timeout=15,      # 15 second timeout
    retries=5,       # Retry up to 5 times
    retry_delay=15   # Wait 15 seconds between retries
)
```

### Development/Testing Setup

```python
import entsoe

# Development configuration for faster feedback
entsoe.set_config(
    security_token="your-security-token-here",
    timeout=10,      # 10 second timeout
    retries=1,       # Only retry once
    retry_delay=2    # Short delay between retries
)
```

### Environment-Based Configuration

```python
import os
import entsoe

# Configure based on environment
if os.getenv("ENVIRONMENT") == "production":
    entsoe.set_config(
        timeout=20,
        retries=5,
        retry_delay=15
    )
else:
    entsoe.set_config(
        timeout=10,
        retries=2,
        retry_delay=5
    )
```

## Configuration Management

### Checking Current Configuration

```python
import entsoe

# Check if configuration exists
if entsoe.has_config():
    config = entsoe.get_config()
    print(f"Timeout: {config.timeout}")
    print(f"Retries: {config.retries}")
    print(f"Retry Delay: {config.retry_delay}")
    print(f"Has API Key: {config.security_token is not None}")
else:
    print("No configuration set")
```

### Resetting Configuration

```python
import entsoe

# Reset configuration to defaults
entsoe.reset_config()

# Reconfigure with new settings
entsoe.set_config(security_token="new-token")
```

## Best Practices

### Security

- **Never hardcode API keys** in your source code
- Use environment variables or secure configuration files
- Rotate API keys regularly according to your organization's security policy

### Network Settings

- **Start with defaults** and adjust only if needed
- **Monitor API response times** to optimize timeout settings
- **Consider API rate limits** when setting retry delays
- **Log network errors** to understand when retries are occurring

### Error Handling

```python
import entsoe
from entsoe.Balancing.specific_params import AcceptedAggregatedOffers

try:
    # Configure with reasonable settings
    entsoe.set_config(
        security_token="your-token",
        timeout=15,
        retries=3,
        retry_delay=10
    )
    
    # Use the API
    params = AcceptedAggregatedOffers(
        period_start=202301010000,
        period_end=202301020000,
        control_area_domain="10Y1001A1001A83F"
    )
    
except Exception as e:
    print(f"Configuration or API error: {e}")
```

## Troubleshooting

### "No global configuration set" Error

This error occurs when trying to use the API without setting a configuration:

```python
# ❌ This will fail
from entsoe.Balancing.specific_params import AcceptedAggregatedOffers
params = AcceptedAggregatedOffers(...)  # Error: No global configuration set

# ✅ Fix by setting configuration first
import entsoe
entsoe.set_config(security_token="your-token")
params = AcceptedAggregatedOffers(...)  # Now works
```

### Timeout Issues

If you're experiencing timeout errors:

1. **Increase timeout**: `entsoe.set_config(timeout=30)`
2. **Check internet connection**: Ensure stable connectivity
3. **Check ENTSO-E API status**: The API may be experiencing issues

### Excessive Retries

If requests are being retried too frequently:

1. **Reduce retry count**: `entsoe.set_config(retries=1)`
2. **Increase retry delay**: `entsoe.set_config(retry_delay=20)`
3. **Check API rate limits**: You may be hitting rate limits

## Related Documentation

- [Getting Started](getting_started.md) - Basic library usage
- [Examples](examples.md) - Practical usage examples
- [Development](development.md) - Contributing to the library
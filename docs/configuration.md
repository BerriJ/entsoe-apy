# Configuration

This page describes how to configure the ENTSO-E API Python library, including API key management and network settings.

## Overview

The library uses a global configuration system that allows you to set common parameters once and reuse them across all API calls. This configuration includes:

- **API Key (Security Token)**: Required for authentication with the ENTSO-E Transparency Platform
- **Timeout**: HTTP request timeout duration
- **Retries**: Number of retry attempts for failed requests
- **Retry Delay**: Wait time between retry attempts
- **Log Level**: Configurable logging level for controlling output verbosity

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

### Log Level

The **log_level** parameter controls the verbosity of logging output using the loguru library.

**Default**: SUCCESS

**Available levels** (from least to most verbose):
- **CRITICAL**: Only critical errors
- **ERROR**: Error messages and above
- **WARNING**: Warning messages and above  
- **SUCCESS**: Success messages and above (default - shows successful operations and issues)
- **INFO**: Informational messages and above
- **DEBUG**: Debug messages and above (most verbose)
- **TRACE**: All messages including trace information

```python
import entsoe

# Set to DEBUG for detailed troubleshooting
entsoe.set_config(
    security_token="your-token",
    log_level="DEBUG"
)

# Set to ERROR for minimal output (only errors)
entsoe.set_config(
    security_token="your-token", 
    log_level="ERROR"
)

# Default SUCCESS level shows successful operations and any issues
entsoe.set_config(
    security_token="your-token",
    log_level="SUCCESS"  # This is the default
)
```

**What it does**: Controls which log messages are displayed. Lower levels show fewer messages, higher levels show more details.

**When to adjust**:
- Use **DEBUG** or **INFO** when troubleshooting API issues
- Use **ERROR** or **WARNING** for production environments where you only want to see problems
- Use **SUCCESS** (default) for a good balance of useful information without excessive detail

## Complete Configuration Example

```python
import entsoe

# Production configuration with increased reliability and minimal logging
entsoe.set_config(
    security_token="your-security-token-here",
    timeout=15,      # 15 second timeout
    retries=5,       # Retry up to 5 times
    retry_delay=15,  # Wait 15 seconds between retries
    log_level="WARNING"  # Only show warnings and errors
)
```

## Related Documentation

- [Examples](examples.md) - Practical usage examples
- [ENTSOE](./ENTSOE/index.md) - Class documentation
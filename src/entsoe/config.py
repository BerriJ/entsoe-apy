"""Configuration management for ENTSO-E API Python client."""

import os
from typing import Optional
from loguru import logger


class EntsoEConfig:
    """
    Configuration class for ENTSO-E API Python client.

    This class holds global configuration options including:
    - Security token for API authentication
    - Request timeout settings
    - Number of retries for failed requests
    - Delay between retry attempts
    """

    def __init__(
        self,
        security_token: Optional[str] = None,
        timeout: int = 5,
        retries: int = 3,
        retry_delay: int = 10,
    ):
        """
        Initialize configuration with global options.

        Args:
            security_token: API security token. If not provided, will try to get from
                          ENTSOE_API environment variable. If neither is available,
                          raises ValueError.
            timeout: Request timeout in seconds (default: 5)
            retries: Number of retry attempts for failed requests (default: 3)

        Raises:
            ValueError: If security_token is not provided and ENTSOE_API environment
                       variable is not set.
        """
        # Handle security token
        if security_token is None:
            security_token = os.getenv("ENTSOE_API")
            logger.info("Security token found in environment.")

        if security_token is None:
            logger.warning(
                "Security token is required. Please provide it explicitly using"
                'entsoe.set_config("<security_token>") or set '
                "the ENTSOE_API environment variable."
            )

        self.security_token = security_token
        self.timeout = timeout
        self.retries = retries
        self.retry_delay = retry_delay


# Global configuration instance
_global_config: Optional[EntsoEConfig] = None


def get_config() -> EntsoEConfig:
    """
    Get the global configuration instance.

    Returns:
        Global EntsoEConfig instance

    Raises:
        RuntimeError: If no global configuration has been set
    """
    global _global_config
    if _global_config is None:
        raise RuntimeError(
            "No global configuration set. Please call set_config() first or "
            "provide security_token explicitly to parameter classes."
        )
    return _global_config


def set_config(
    security_token: Optional[str] = None,
    timeout: int = 5,
    retries: int = 3,
    retry_delay: int = 10,
) -> None:
    """
    Set the global configuration.

    Args:
        security_token: API security token. If not provided, will try to get from
                      ENTSOE_API environment variable.
        timeout: Request timeout in seconds (default: 5)
        retries: Number of retry attempts for failed requests (default: 3)
    """
    global _global_config
    _global_config = EntsoEConfig(
        security_token=security_token,
        timeout=timeout,
        retries=retries,
        retry_delay=retry_delay,
    )


def has_config() -> bool:
    """
    Check if global configuration has been set.

    Returns:
        True if global configuration exists, False otherwise
    """
    global _global_config
    return _global_config is not None


def reset_config() -> None:
    """Reset the global configuration to None."""
    global _global_config
    _global_config = None

"""Configuration management for ENTSO-E API Python client."""

import os
import sys
from typing import Optional
from uuid import UUID

from loguru import logger


class EntsoEConfig:
    """
    Configuration class for ENTSO-E API Python client.

    This class holds global configuration options including:
    - Security token for API authentication
    - Request timeout settings
    - Number of retries for failed requests
    - Delay between retry attempts
    - Log level for loguru logger
    """

    def __init__(
        self,
        security_token: Optional[str] = None,
        timeout: int = 5,
        retries: int = 3,
        retry_delay: int = 10,
        log_level: str = "SUCCESS",
    ):
        """
        Initialize configuration with global options.

        Args:
            security_token: API security token. If not provided, will try to get from
                          ENTSOE_API environment variable. If neither is available,
                          raises ValueError.
            timeout: Request timeout in seconds (default: 5)
            retries: Number of retry attempts for failed requests (default: 3)
            retry_delay: Delay between retry attempts in seconds (default: 10)
            log_level: Log level for loguru logger. Available levels: TRACE, DEBUG,
                      INFO, SUCCESS, WARNING, ERROR, CRITICAL (default: SUCCESS)

        Raises:
            ValueError: If security_token is not provided and ENTSOE_API environment
                       variable is not set.
        """
        # Validate log level
        valid_levels = [
            "TRACE",
            "DEBUG",
            "INFO",
            "SUCCESS",
            "WARNING",
            "ERROR",
            "CRITICAL",
        ]
        if log_level.upper() not in valid_levels:
            raise ValueError(
                f"Invalid log_level '{log_level}'. Must be one of: {valid_levels}"
            )

        # Configure loguru logger level
        logger.remove()
        logger.add(sink=sys.stdout, level=log_level.upper(), colorize=True)
        # Handle security token
        if security_token is None and os.getenv("ENTSOE_API") is not None:
            security_token = os.getenv("ENTSOE_API")
            logger.success("Security token found in environment.")

        if security_token is None:
            logger.warning(
                "Security token is required. Please provide it explicitly using "
                'entsoe.set_config("<security_token>") or set '
                "the ENTSOE_API environment variable."
            )

        # Validate security token format (UUID)
        if security_token is not None:
            try:
                # Validate UUID format
                UUID(security_token)
                logger.debug("Security token is a valid UUID.")
            except ValueError:
                logger.error("Invalid security_token format. Must be a valid UUID.")

        self.security_token = security_token
        self.timeout = timeout
        self.retries = retries
        self.retry_delay = retry_delay
        self.log_level = log_level.upper()


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
    log_level: str = "SUCCESS",
) -> None:
    """
    Set the global configuration.

    Args:
        security_token: API security token. If not provided, will try to get from
                      ENTSOE_API environment variable.
        timeout: Request timeout in seconds (default: 5)
        retries: Number of retry attempts for failed requests (default: 3)
        retry_delay: Delay between retry attempts in seconds (default: 10)
        log_level: Log level for loguru logger. Available levels: TRACE, DEBUG,
                  INFO, SUCCESS, WARNING, ERROR, CRITICAL (default: SUCCESS)
    """
    global _global_config
    _global_config = EntsoEConfig(
        security_token=security_token,
        timeout=timeout,
        retries=retries,
        retry_delay=retry_delay,
        log_level=log_level,
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

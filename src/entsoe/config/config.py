"""Configuration management for ENTSO-E API Python client."""

import os
import sys
from typing import Callable, Literal, Optional, Union, get_args
from uuid import UUID

from loguru._logger import Core as _Core, Logger as _Logger

LogLevel = Literal["TRACE", "DEBUG", "INFO", "SUCCESS", "WARNING", "ERROR", "CRITICAL"]
LogFormat = (
    "<fg #B0BEC5>{time:YYYY-MM-DD HH:mm:ss.SSS}</fg #B0BEC5> | "
    "<level>{level: <8}</level> | "
    "<fg #E91E63>{process.name: <11}</fg #E91E63> | "
    "<fg #E91E63>{thread.name: <10}</fg #E91E63> | "
    "<fg #2196F3>{name}</fg #2196F3>:"
    "<fg #03A9F4>{function}</fg #03A9F4>:"
    "<fg #009688>{line}</fg #009688> - "
    "<level>{message}</level>"
)

# Create an independent Loguru logger instance for this package
logger = _Logger(
    core=_Core(),
    exception=None,
    depth=0,
    record=False,
    lazy=False,
    colors=False,
    raw=False,
    capture=True,
    patchers=[],
    extra={},
)

# No default sink - will be added by set_log_level() when set_config() is called
_handler_id: Optional[int] = None


def set_log_level(level: LogLevel) -> None:
    """
    Change the log level of the entsoe logger.

    Args:
        level: Log level (TRACE, DEBUG, INFO, SUCCESS, WARNING, ERROR, CRITICAL)

    Raises:
        ValueError: If an invalid log level is provided
    """
    global _handler_id

    # Validate log level (runtime check, as Literal is only for type checking)
    valid_levels = tuple(get_args(LogLevel))
    if level not in valid_levels:
        raise ValueError(f"Invalid log_level '{level}'. Must be one of: {valid_levels}")

    # Remove the current handler if it exists
    if _handler_id is not None:
        try:
            logger.remove(_handler_id)
        except ValueError:
            # Handler doesn't exist, that's fine
            pass

    # Add a new handler with the updated level
    _handler_id = logger.add(
        sink=sys.stderr,
        level=level,
        colorize=True,
        format=LogFormat,
    )


class EntsoEConfig:
    """
    Configuration class for ENTSO-E API Python client.

    This class holds global configuration options including:
    - Security token for API authentication
    - API endpoint URL (configurable via ENTSOE_ENDPOINT_URL environment variable)
    - Request timeout settings
    - Number of retries for failed requests
    - Delay between retry attempts
    - Log level for loguru logger
    """

    def __init__(
        self,
        security_token: Optional[str] = None,
        endpoint_url: Optional[str] = None,
        timeout: int = 5,
        retries: int = 5,
        retry_delay: Union[int, Callable[[int], int]] = lambda attempt: 2**attempt,
        max_workers: int = 4,
        log_level: LogLevel = "SUCCESS",
    ):
        """
        Initialize configuration with global options.

        Args:
            security_token: API security token. If not provided, will try to get from
                          ENTSOE_API environment variable. If neither is available,
                          raises ValueError.
            endpoint_url: API endpoint URL. If not provided, will try to get from
                         ENTSOE_ENDPOINT_URL environment variable. If neither is available,
                         defaults to "https://web-api.tp.entsoe.eu/api".
            timeout: Request timeout in seconds (default: 5)
            retries: Number of retry attempts for failed requests (default: 5)
            retry_delay: Function that takes attempt number and returns delay in seconds,
                        or integer for constant delay (default: exponential backoff 2**attempt)
            max_workers: Maximum number of parallel API calls when splitting large date
                        ranges (default: 4)
            log_level: Log level for loguru logger. Available levels: TRACE, DEBUG,
                      INFO, SUCCESS, WARNING, ERROR, CRITICAL (default: SUCCESS)

        Raises:
            ValueError: If security_token is not provided and ENTSOE_API environment
                       variable is not set.
        """
        # Set the log level using our independent logger's set_log_level function
        set_log_level(log_level)

        # Handle endpoint URL
        env_endpoint_url = os.getenv("ENTSOE_ENDPOINT_URL") or None
        if endpoint_url is None and env_endpoint_url is not None:
            endpoint_url = env_endpoint_url
            logger.success("API endpoint URL loaded from environment.")

        if endpoint_url is None:
            endpoint_url = "https://web-api.tp.entsoe.eu/api"
            logger.debug("Using default API endpoint URL.")

        self.endpoint_url = endpoint_url

        # Handle security token
        env_token = os.getenv("ENTSOE_API") or None
        if security_token is None and env_token is not None:
            security_token = env_token
            logger.success("Security token loaded from environment.")

        if security_token is None:
            logger.warning(
                "Security token not provided. Please provide it explicitly using "
                'entsoe.set_config("<security_token>") or set '
                "the ENTSOE_API environment variable."
            )

        # Validate security token format (UUID)
        if security_token is not None:
            try:
                # Validate UUID format
                UUID(security_token)
                logger.trace("Security token format validated successfully.")
            except ValueError:
                logger.error("Invalid security_token format. Must be a valid UUID.")

        self.security_token = security_token
        self.timeout = timeout
        self.retries = retries
        # Handle retry_delay: support both int and function
        if isinstance(retry_delay, int):
            # Convert integer to constant function
            self.retry_delay = lambda attempt: retry_delay
        else:
            # It's already a callable function (including the default)
            self.retry_delay = retry_delay
        self.max_workers = max_workers
        self.log_level = log_level

    def validate_security_token(self) -> None:
        """
        Validate that the security token is present and valid.

        Raises:
            ValueError: If security token is None or invalid format
        """
        logger.trace("validate_security_token: Enter")
        if self.security_token is None:
            logger.error(
                'Security token is not set. Please provide it explicitly using entsoe.set_config("<security_token>") or set the ENTSOE_API environment variable.'
            )
            raise ValueError(
                "Security token is required but not provided. Please set it explicitly "
                'using entsoe.set_config("<security_token>") or set the ENTSOE_API '
                "environment variable."
            )

        try:
            # Validate UUID format
            UUID(self.security_token)
        except ValueError as e:
            logger.error("Invalid security_token format. Must be a valid UUID.")
            raise ValueError(
                f"Invalid security token format. Must be a valid UUID. Error: {e}"
            ) from e

        logger.trace("validate_security_token: Exit, validation passed")


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
    endpoint_url: Optional[str] = None,
    timeout: int = 5,
    retries: int = 5,
    retry_delay: Union[int, Callable[[int], int]] = lambda attempt: 2**attempt,
    max_workers: int = 4,
    log_level: LogLevel = "SUCCESS",
) -> None:
    """
    Set the global configuration.

    Args:
        security_token: API security token. If not provided, will try to get from
                      ENTSOE_API environment variable.
        endpoint_url: API endpoint URL. If not provided, will try to get from
                     ENTSOE_ENDPOINT_URL environment variable. If neither is available,
                     defaults to "https://web-api.tp.entsoe.eu/api".
        timeout: Request timeout in seconds (default: 5)
        retries: Number of retry attempts for failed requests (default: 5)
        retry_delay: Function that takes attempt number and returns delay in seconds,
                    or integer for constant delay (default: exponential backoff 2**attempt)
        max_workers: Maximum number of parallel API calls when splitting large date
                    ranges (default: 4)
        log_level: Log level for loguru logger. Available levels: TRACE, DEBUG,
                  INFO, SUCCESS, WARNING, ERROR, CRITICAL (default: SUCCESS)
    """
    global _global_config
    _global_config = EntsoEConfig(
        security_token=security_token,
        endpoint_url=endpoint_url,
        timeout=timeout,
        retries=retries,
        retry_delay=retry_delay,
        max_workers=max_workers,
        log_level=log_level,
    )

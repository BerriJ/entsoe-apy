"""Test module for logging configuration functionality."""

from unittest.mock import patch

import pytest

from entsoe.config.config import EntsoEConfig, get_config, reset_config, set_config


class TestLoggingConfig:
    """Test class for logging configuration functionality."""

    def teardown_method(self):
        """Clean up configuration after each test."""
        reset_config()

    def test_config_accepts_log_level_parameter(self):
        """Test that EntsoEConfig accepts log_level parameter."""
        config = EntsoEConfig(security_token="test_token", log_level="DEBUG")
        assert config.log_level == "DEBUG"

    def test_config_defaults_to_success_log_level(self):
        """Test that EntsoEConfig defaults to SUCCESS log level."""
        config = EntsoEConfig(security_token="test_token")
        assert config.log_level == "SUCCESS"

    def test_config_validates_log_level(self):
        """Test that EntsoEConfig validates log_level parameter."""
        with pytest.raises(ValueError, match="Invalid log_level"):
            EntsoEConfig(security_token="test_token", log_level="INVALID")

    def test_config_accepts_valid_log_levels(self):
        """Test that EntsoEConfig accepts all valid log levels."""
        valid_levels = [
            "TRACE",
            "DEBUG",
            "INFO",
            "SUCCESS",
            "WARNING",
            "ERROR",
            "CRITICAL",
        ]

        for level in valid_levels:
            config = EntsoEConfig(security_token="test_token", log_level=level)
            assert config.log_level == level

    def test_config_accepts_case_insensitive_log_levels(self):
        """Test that EntsoEConfig accepts case insensitive log levels."""
        config = EntsoEConfig(security_token="test_token", log_level="debug")
        assert config.log_level == "DEBUG"

        config = EntsoEConfig(security_token="test_token", log_level="Success")
        assert config.log_level == "SUCCESS"

    def test_set_config_accepts_log_level_parameter(self):
        """Test that set_config accepts log_level parameter."""
        set_config(security_token="test_token", log_level="DEBUG")
        config = get_config()
        assert config.log_level == "DEBUG"

    def test_set_config_defaults_to_success_log_level(self):
        """Test that set_config defaults to SUCCESS log level."""
        set_config(security_token="test_token")
        config = get_config()
        assert config.log_level == "SUCCESS"

    @patch("entsoe.config.config.logger")
    def test_loguru_configuration_is_updated(self, mock_logger):
        """Test that loguru logger is configured when EntsoEConfig is created."""
        EntsoEConfig(security_token="test_token", log_level="DEBUG")

        # Verify that logger.remove() was called to remove default handler
        mock_logger.remove.assert_called_once()

        # Verify that logger.add() was called to add new handler with correct level
        mock_logger.add.assert_called_once()
        call_args = mock_logger.add.call_args
        assert call_args[1]["level"] == "DEBUG"

    def test_existing_functionality_preserved(self):
        """Test that existing functionality is preserved with log_level parameter."""

        def custom_retry_delay(attempt):
            return 15

        config = EntsoEConfig(
            security_token="test_token",
            timeout=30,
            retries=5,
            retry_delay=custom_retry_delay,
            log_level="INFO",
        )

        assert config.security_token == "test_token"
        assert config.timeout == 30
        assert config.retries == 5
        assert config.retry_delay(0) == 15  # Test the function call
        assert config.log_level == "INFO"

    def test_retry_delay_integer_support(self):
        """Test that retry_delay accepts integers and converts them to constant functions."""
        config = EntsoEConfig(
            security_token="test_token",
            retry_delay=10,  # Integer value
        )

        # Should return 10 for any attempt
        assert config.retry_delay(0) == 10
        assert config.retry_delay(1) == 10
        assert config.retry_delay(5) == 10

    def test_retry_delay_function_support(self):
        """Test that retry_delay accepts functions."""

        def linear_backoff(attempt):
            return (attempt + 1) * 3

        config = EntsoEConfig(
            security_token="test_token",
            retry_delay=linear_backoff,
        )

        # Should return linear progression: 3, 6, 9, 12...
        assert config.retry_delay(0) == 3
        assert config.retry_delay(1) == 6
        assert config.retry_delay(2) == 9
        assert config.retry_delay(3) == 12

    def test_retry_delay_default_exponential(self):
        """Test that retry_delay defaults to exponential backoff when not specified."""
        config = EntsoEConfig(security_token="test_token")

        # Should return exponential progression: 1, 2, 4, 8...
        assert config.retry_delay(0) == 1  # 2^0
        assert config.retry_delay(1) == 2  # 2^1
        assert config.retry_delay(2) == 4  # 2^2
        assert config.retry_delay(3) == 8  # 2^3

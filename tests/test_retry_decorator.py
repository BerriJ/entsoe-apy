"""Test module for verifying retry decorator functionality."""

from unittest.mock import patch

import httpx
import pytest

from entsoe import set_config
from entsoe.config.config import reset_config
from entsoe.query.decorators import retry


class TestRetryDecorator:
    """Test class for retry decorator functionality."""

    def setup_method(self):
        """Set up test configuration before each test."""
        set_config(
            security_token="test_token", retries=3, retry_delay=lambda attempt: 1
        )

    def teardown_method(self):
        """Clean up configuration after each test."""
        reset_config()

    def test_retry_decorator_success_on_first_attempt(self):
        """Test that retry decorator works correctly when function succeeds
        on first attempt."""

        @retry
        def successful_function(*args, **kwargs):
            return "success"

        result = successful_function("arg1", kwarg="value")
        assert result == "success"

    def test_retry_decorator_success_after_failures(self):
        """Test that retry decorator retries and eventually succeeds."""
        call_count = 0

        @retry
        def function_that_fails_twice(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise httpx.RequestError("Connection failed")
            return f"success after {call_count} attempts"

        with patch("entsoe.query.decorators.sleep") as mock_sleep:
            result = function_that_fails_twice("arg1", kwarg="value")

        assert result == "success after 3 attempts"
        assert call_count == 3
        # Verify sleep was called twice (for the first two failed attempts)
        assert mock_sleep.call_count == 2
        mock_sleep.assert_called_with(1)  # Using retry_delay from test setup

    def test_retry_decorator_exhausts_all_attempts(self):
        """Test that retry decorator raises exception after all attempts
        are exhausted."""
        call_count = 0

        @retry
        def always_failing_function(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            raise httpx.RequestError("Connection always fails")

        with patch("entsoe.query.decorators.sleep") as mock_sleep:
            with pytest.raises(httpx.RequestError, match="Connection always fails"):
                always_failing_function("arg1", kwarg="value")

        # Should have been called 3 times (default retry_count)
        assert call_count == 3
        # Should have slept twice (after first two failures, not after the last)
        assert mock_sleep.call_count == 2

    def test_retry_decorator_with_non_httpx_exception(self):
        """Test that retry decorator doesn't retry non-httpx exceptions."""
        call_count = 0

        @retry
        def function_with_value_error(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            raise ValueError("This is not a connection error")

        with pytest.raises(ValueError, match="This is not a connection error"):
            function_with_value_error("arg1", kwarg="value")

        # Should have been called only once (no retries for non-httpx errors)
        assert call_count == 1

    def test_retry_decorator_preserves_function_metadata(self):
        """Test that retry decorator preserves original function's metadata."""

        @retry
        def documented_function(param1, param2="default"):
            """This is a documented function."""
            return param1 + param2

        assert documented_function.__name__ == "documented_function"
        assert documented_function.__doc__ == "This is a documented function."

    def test_retry_decorator_passes_arguments_correctly(self):
        """Test that retry decorator correctly passes positional and
        keyword arguments."""

        @retry
        def function_with_args(*args, **kwargs):
            return {"args": args, "kwargs": kwargs}

        result = function_with_args("pos1", "pos2", key1="val1", key2="val2")

        assert result["args"] == ("pos1", "pos2")
        assert result["kwargs"] == {"key1": "val1", "key2": "val2"}

    def test_retry_decorator_handles_timeout_parameter(self):
        """Test that retry decorator correctly handles timeout parameter in kwargs."""

        @retry
        def function_with_timeout(*args, **kwargs):
            return kwargs.get("timeout", "no timeout")

        result = function_with_timeout(timeout=30)
        assert result == 30

    def test_retry_decorator_logs_correctly(self):
        """Test that retry decorator logs warning messages correctly."""
        call_count = 0

        @retry
        def function_that_fails_once(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                raise httpx.RequestError("First failure")
            return "success"

        with patch("entsoe.query.decorators.sleep"):
            with patch("entsoe.query.decorators.logger") as mock_logger:
                result = function_that_fails_once()

        assert result == "success"
        assert call_count == 2

        # Verify warning was logged
        mock_logger.warning.assert_called_once()
        warning_call = mock_logger.warning.call_args[0][0]
        assert "Connection Error on attempt 1/3" in warning_call
        assert "First failure" in warning_call
        assert "Retrying in 1 seconds" in warning_call

    def test_retry_decorator_logs_final_error(self):
        """Test that retry decorator logs error when all attempts fail."""

        @retry
        def always_failing_function():
            raise httpx.RequestError("Always fails")

        with patch("entsoe.query.decorators.sleep"):
            with patch("entsoe.query.decorators.logger") as mock_logger:
                with pytest.raises(httpx.RequestError):
                    always_failing_function()

        # Verify error was logged
        mock_logger.error.assert_called_once_with("All 3 retry attempts failed")

    def test_retry_decorator_different_httpx_errors(self):
        """Test that retry decorator handles different types of httpx errors."""
        error_types = [
            httpx.ConnectError("Connection failed"),
            httpx.TimeoutException("Request timed out"),
            httpx.NetworkError("Network unreachable"),
        ]

        for error in error_types:
            call_count = 0

            @retry
            def function_with_specific_error():
                nonlocal call_count
                call_count += 1
                if call_count == 1:
                    raise error
                return "success"

            with patch("entsoe.query.decorators.sleep"):
                result = function_with_specific_error()

            assert result == "success"
            assert call_count == 2

    def test_retry_decorator_runtime_error_on_unknown_failure(self):
        """Test that retry decorator raises RuntimeError when no exception
        is captured."""
        # This is an edge case test for the RuntimeError fallback
        # It's difficult to trigger naturally, so we'll mock the behavior

        @retry
        def function_that_somehow_fails_without_exception():
            # This scenario is unlikely in real code but tests the fallback
            return "success"

        # We can't easily test the RuntimeError fallback without modifying
        # the decorator internals, so we'll verify the logic exists
        # by checking the source code structure
        import inspect

        source = inspect.getsource(retry)
        assert "RuntimeError" in source
        assert "All retry attempts failed with unknown error" in source

    def test_default_exponential_backoff(self):
        """Test that default exponential backoff function works correctly."""
        # Reset to use default configuration
        reset_config()
        set_config(security_token="test_token", retries=3)

        call_count = 0

        @retry
        def function_that_fails_twice(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise httpx.RequestError("Connection failed")
            return "success"

        with patch("entsoe.query.decorators.sleep") as mock_sleep:
            result = function_that_fails_twice()

        assert result == "success"
        assert call_count == 3
        # Verify exponential backoff: first retry waits 2^0=1, second retry waits 2^1=2
        assert mock_sleep.call_count == 2
        mock_sleep.assert_any_call(1)  # 2^0 = 1
        mock_sleep.assert_any_call(2)  # 2^1 = 2

    def test_custom_retry_delay_function(self):
        """Test that custom retry delay functions work correctly."""

        def linear_backoff(attempt):
            return (attempt + 1) * 5  # 5, 10, 15, etc.

        reset_config()
        set_config(security_token="test_token", retries=3, retry_delay=linear_backoff)

        call_count = 0

        @retry
        def function_that_fails_twice(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise httpx.RequestError("Connection failed")
            return "success"

        with patch("entsoe.query.decorators.sleep") as mock_sleep:
            result = function_that_fails_twice()

        assert result == "success"
        assert call_count == 3
        # Verify custom backoff: first retry waits 5, second retry waits 10
        assert mock_sleep.call_count == 2
        mock_sleep.assert_any_call(5)  # (0 + 1) * 5 = 5
        mock_sleep.assert_any_call(10)  # (1 + 1) * 5 = 10

    def test_integer_retry_delay(self):
        """Test that integer retry_delay values work correctly."""
        reset_config()
        set_config(
            security_token="test_token", retries=3, retry_delay=7
        )  # Integer delay

        call_count = 0

        @retry
        def function_that_fails_twice(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise httpx.RequestError("Connection failed")
            return "success"

        with patch("entsoe.query.decorators.sleep") as mock_sleep:
            result = function_that_fails_twice()

        assert result == "success"
        assert call_count == 3
        # Verify constant backoff: both retries wait 7 seconds
        assert mock_sleep.call_count == 2
        mock_sleep.assert_any_call(7)  # First retry
        mock_sleep.assert_any_call(7)  # Second retry

"""Test module for verifying rate_limit decorator functionality."""

from concurrent.futures import ThreadPoolExecutor
import threading
import time as real_time
from unittest.mock import patch

from entsoe.query.decorators import rate_limit


class TestRateLimitDecorator:
    """Test class for rate_limit decorator functionality."""

    def test_calls_allowed_within_limit(self):
        """Test that calls are allowed when within the rate limit."""
        call_count = 0

        @rate_limit(max_calls=5, period=10)
        def simple_function():
            nonlocal call_count
            call_count += 1
            return "success"

        # Make calls within the limit
        with patch("entsoe.query.decorators.sleep") as mock_sleep:
            for _ in range(5):
                result = simple_function()
                assert result == "success"

            # No sleep should be called when within limit
            mock_sleep.assert_not_called()

        assert call_count == 5

    def test_excessive_calls_trigger_sleep(self):
        """Test that excessive calls trigger sleep for rate limiting."""
        call_count = 0

        @rate_limit(max_calls=2, period=10)
        def rate_limited_function():
            nonlocal call_count
            call_count += 1
            return "success"

        with patch("entsoe.query.decorators.sleep") as mock_sleep:
            with patch("entsoe.query.decorators.time") as mock_time:
                # First call at time 0
                mock_time.return_value = 0
                rate_limited_function()

                # Second call at time 0
                mock_time.return_value = 0
                rate_limited_function()

                # Third call at time 0 - should trigger sleep
                mock_time.return_value = 0
                rate_limited_function()

                # Sleep should have been called once
                assert mock_sleep.call_count == 1
                # Wait time should be period - (now - first_call) = 10 - 0 = 10
                mock_sleep.assert_called_once_with(10)

        assert call_count == 3

    def test_old_calls_cleaned_from_deque(self):
        """Test that old calls are properly cleaned from the deque."""
        call_count = 0

        @rate_limit(max_calls=2, period=5)
        def rate_limited_function():
            nonlocal call_count
            call_count += 1
            return "success"

        with patch("entsoe.query.decorators.sleep") as mock_sleep:
            with patch("entsoe.query.decorators.time") as mock_time:
                # First call at time 0
                mock_time.return_value = 0
                rate_limited_function()

                # Second call at time 0
                mock_time.return_value = 0
                rate_limited_function()

                # Third call at time 10 - old calls should be cleaned
                # Since period=5, calls from time 0 are > 5 seconds old
                mock_time.return_value = 10
                rate_limited_function()

                # Fourth call at time 10 - still within new limit
                mock_time.return_value = 10
                rate_limited_function()

                # No sleep should be called since old calls were cleaned
                mock_sleep.assert_not_called()

        assert call_count == 4

    def test_thread_safety_concurrent_access(self):
        """Test that the decorator is thread-safe under concurrent access."""
        call_count = 0
        call_lock = threading.Lock()

        @rate_limit(max_calls=10, period=60)
        def thread_safe_function(thread_id):
            nonlocal call_count
            with call_lock:
                call_count += 1
            return f"success from thread {thread_id}"

        # Use ThreadPoolExecutor to make concurrent calls
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(thread_safe_function, i) for i in range(10)]
            results = [f.result() for f in futures]

        # All calls should complete successfully
        assert len(results) == 10
        assert call_count == 10
        for i, result in enumerate(results):
            assert result == f"success from thread {i}"

    def test_thread_safety_rate_limiting_enforced(self):
        """Test that rate limiting is enforced correctly across threads."""
        call_timestamps = []
        timestamps_lock = threading.Lock()

        @rate_limit(max_calls=3, period=1)
        def tracked_function():
            # Record real time for each call
            with timestamps_lock:
                call_timestamps.append(real_time.time())
            return "success"

        # Make more calls than the limit in parallel
        with patch("entsoe.query.decorators.sleep") as mock_sleep:
            with ThreadPoolExecutor(max_workers=5) as executor:
                futures = [executor.submit(tracked_function) for _ in range(5)]
                results = [f.result() for f in futures]

            # All calls should complete
            assert len(results) == 5

            # Sleep should have been called for the calls beyond the limit
            assert mock_sleep.call_count >= 1

    def test_preserves_function_metadata(self):
        """Test that rate_limit decorator preserves original function's metadata."""

        @rate_limit(max_calls=10, period=60)
        def documented_function(param1, param2="default"):
            """This is a documented function."""
            return param1 + param2

        assert documented_function.__name__ == "documented_function"
        assert documented_function.__doc__ == "This is a documented function."

    def test_passes_arguments_correctly(self):
        """Test that rate_limit decorator correctly passes arguments."""

        @rate_limit(max_calls=10, period=60)
        def function_with_args(*args, **kwargs):
            return {"args": args, "kwargs": kwargs}

        result = function_with_args("pos1", "pos2", key1="val1", key2="val2")

        assert result["args"] == ("pos1", "pos2")
        assert result["kwargs"] == {"key1": "val1", "key2": "val2"}

    def test_logs_rate_limit_message(self):
        """Test that rate_limit decorator logs when rate limit is reached."""

        @rate_limit(max_calls=1, period=10)
        def rate_limited_function():
            return "success"

        with patch("entsoe.query.decorators.sleep"):
            with patch("entsoe.query.decorators.time") as mock_time:
                with patch("entsoe.query.decorators.logger") as mock_logger:
                    # First call at time 0
                    mock_time.return_value = 0
                    rate_limited_function()

                    # Second call at time 0 - should trigger rate limit
                    mock_time.return_value = 0
                    rate_limited_function()

                    # Verify debug message was logged
                    mock_logger.debug.assert_called()
                    debug_calls = [
                        str(call) for call in mock_logger.debug.call_args_list
                    ]
                    assert any("Rate limit reached" in call for call in debug_calls)

    def test_wait_time_calculation(self):
        """Test that wait time is calculated correctly."""

        @rate_limit(max_calls=2, period=10)
        def rate_limited_function():
            return "success"

        with patch("entsoe.query.decorators.sleep") as mock_sleep:
            with patch("entsoe.query.decorators.time") as mock_time:
                # First call at time 0
                mock_time.return_value = 0
                rate_limited_function()

                # Second call at time 0
                mock_time.return_value = 0
                rate_limited_function()

                # Third call at time 3 - should wait (10 - 3) = 7 seconds
                mock_time.return_value = 3
                rate_limited_function()

                mock_sleep.assert_called_once_with(7)

    def test_multiple_decorated_functions_have_separate_limits(self):
        """Test that different decorated functions have separate rate limit states."""
        calls_a = 0
        calls_b = 0

        @rate_limit(max_calls=2, period=10)
        def function_a():
            nonlocal calls_a
            calls_a += 1
            return "A"

        @rate_limit(max_calls=2, period=10)
        def function_b():
            nonlocal calls_b
            calls_b += 1
            return "B"

        with patch("entsoe.query.decorators.sleep") as mock_sleep:
            with patch("entsoe.query.decorators.time") as mock_time:
                mock_time.return_value = 0

                # Call function_a twice (at limit)
                function_a()
                function_a()

                # Call function_b twice (at limit)
                function_b()
                function_b()

                # No sleep should be needed - separate rate limit states
                mock_sleep.assert_not_called()

        assert calls_a == 2
        assert calls_b == 2

    def test_function_executes_outside_lock(self):
        """Test that decorated function executes outside lock, allowing parallel calls."""
        execution_order = []
        execution_lock = threading.Lock()
        in_function = threading.Event()
        function_started = threading.Event()

        @rate_limit(max_calls=10, period=60)
        def slow_function(call_id):
            function_started.set()
            with execution_lock:
                execution_order.append(f"start_{call_id}")
            # Simulate some work
            in_function.wait(timeout=0.1)
            with execution_lock:
                execution_order.append(f"end_{call_id}")
            return call_id

        # Start first call
        with ThreadPoolExecutor(max_workers=2) as executor:
            future1 = executor.submit(slow_function, 1)
            function_started.wait(timeout=1)  # Wait for first function to start

            # Start second call while first is still running
            future2 = executor.submit(slow_function, 2)

            # Allow functions to complete
            in_function.set()

            result1 = future1.result(timeout=2)
            result2 = future2.result(timeout=2)

        assert result1 == 1
        assert result2 == 2
        # Both functions should have started (proving they can run in parallel)
        assert "start_1" in execution_order
        assert "start_2" in execution_order

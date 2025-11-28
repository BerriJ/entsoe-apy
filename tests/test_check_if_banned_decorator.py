"""Test module for verifying check_if_banned decorator functionality."""

from unittest.mock import MagicMock, patch

import pytest

from entsoe.query.decorators import GotBannedError, check_if_banned


class TestCheckIfBannedDecorator:
    """Test class for check_if_banned decorator functionality."""

    def test_raises_got_banned_error_on_429_status(self):
        """Test that GotBannedError is raised when status_code is 429."""
        mock_response = MagicMock()
        mock_response.status_code = 429
        mock_response.text = "<html><body><p>You have been banned</p></body></html>"

        @check_if_banned
        def function_returning_banned_response():
            return mock_response

        with pytest.raises(GotBannedError, match="You have been banned"):
            function_returning_banned_response()

    def test_extracts_message_from_html_paragraph(self):
        """Test that message is correctly extracted from HTML response paragraph."""
        mock_response = MagicMock()
        mock_response.status_code = 429
        mock_response.text = (
            "<html><head></head><body>"
            "<h1>Error</h1>"
            "<p>Rate limit exceeded. Please try again later.</p>"
            "</body></html>"
        )

        @check_if_banned
        def function_returning_banned_response():
            return mock_response

        with pytest.raises(
            GotBannedError, match="Rate limit exceeded. Please try again later."
        ):
            function_returning_banned_response()

    def test_fallback_to_full_response_when_regex_no_match(self):
        """Test fallback to full response.text when regex doesn't match."""
        mock_response = MagicMock()
        mock_response.status_code = 429
        mock_response.text = "Plain text error message without HTML paragraph tags"

        @check_if_banned
        def function_returning_banned_response():
            return mock_response

        with pytest.raises(
            GotBannedError, match="Plain text error message without HTML paragraph tags"
        ):
            function_returning_banned_response()

    def test_normal_response_passes_through_unchanged(self):
        """Test that normal responses pass through unchanged."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<html><body>Success</body></html>"

        @check_if_banned
        def function_returning_success_response():
            return mock_response

        result = function_returning_success_response()

        assert result is mock_response
        assert result.status_code == 200

    def test_other_error_status_codes_pass_through(self):
        """Test that other error status codes (non-429) pass through."""
        for status_code in [400, 401, 403, 404, 500, 502, 503]:
            mock_response = MagicMock()
            mock_response.status_code = status_code
            mock_response.text = f"Error {status_code}"

            @check_if_banned
            def function_returning_error_response():
                return mock_response

            result = function_returning_error_response()

            assert result is mock_response
            assert result.status_code == status_code

    def test_preserves_function_metadata(self):
        """Test that check_if_banned decorator preserves original function metadata."""
        mock_response = MagicMock()
        mock_response.status_code = 200

        @check_if_banned
        def documented_function(param1, param2="default"):
            """This is a documented function."""
            return mock_response

        assert documented_function.__name__ == "documented_function"
        assert documented_function.__doc__ == "This is a documented function."

    def test_passes_arguments_correctly(self):
        """Test that check_if_banned decorator correctly passes arguments."""
        received_args = None
        received_kwargs = None

        mock_response = MagicMock()
        mock_response.status_code = 200

        @check_if_banned
        def function_with_args(*args, **kwargs):
            nonlocal received_args, received_kwargs
            received_args = args
            received_kwargs = kwargs
            return mock_response

        function_with_args("pos1", "pos2", key1="val1", key2="val2")

        assert received_args == ("pos1", "pos2")
        assert received_kwargs == {"key1": "val1", "key2": "val2"}

    def test_logs_info_message_on_429(self):
        """Test that check_if_banned decorator logs info message when 429 detected."""
        mock_response = MagicMock()
        mock_response.status_code = 429
        mock_response.text = "<p>You are temporarily banned</p>"

        @check_if_banned
        def function_returning_banned_response():
            return mock_response

        with patch("entsoe.query.decorators.logger") as mock_logger:
            with pytest.raises(GotBannedError):
                function_returning_banned_response()

            mock_logger.info.assert_called_once()
            info_call = mock_logger.info.call_args[0][0]
            assert "429" in info_call
            assert "You are temporarily banned" in info_call

    def test_extracts_first_paragraph_from_multiple(self):
        """Test that first paragraph is extracted when HTML has multiple paragraphs."""
        mock_response = MagicMock()
        mock_response.status_code = 429
        mock_response.text = (
            "<html><body>"
            "<p>First paragraph - the ban message</p>"
            "<p>Second paragraph - additional info</p>"
            "</body></html>"
        )

        @check_if_banned
        def function_returning_banned_response():
            return mock_response

        with pytest.raises(GotBannedError, match="First paragraph - the ban message"):
            function_returning_banned_response()

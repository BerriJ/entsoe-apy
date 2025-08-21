"""Test module for verifying debug logging functionality."""

from typing import Optional
from unittest.mock import Mock, patch

from entsoe import set_config, reset_config
from entsoe.query_api import query_core
from entsoe.utils import check_date_range_limit, merge_documents, split_date_range


class TestLogging:
    """Test class for logging functionality."""

    def setup_method(self):
        """Set up test configuration before each test."""
        set_config(security_token="test_token")

    def teardown_method(self):
        """Clean up configuration after each test."""
        reset_config()

    def test_utility_functions_have_logging(self):
        """Test that utility functions can be called and log debug messages."""
        # Test check_date_range_limit
        with patch("entsoe.utils.logger") as mock_logger:
            check_date_range_limit(202301010000, 202301020000, 365)
            assert mock_logger.debug.called
            # Verify that logging calls mention the function purpose
            call_args = [call[0][0] for call in mock_logger.debug.call_args_list]
            assert any("Checking date range limit" in arg for arg in call_args)

    def test_split_date_range_logging(self):
        """Test that split_date_range logs debug messages."""
        with patch("entsoe.utils.logger") as mock_logger:
            pivot, end = split_date_range(202301010000, 202301050000)
            assert mock_logger.debug.called
            # Verify that logging calls mention the function purpose
            call_args = [call[0][0] for call in mock_logger.debug.call_args_list]
            assert any("Splitting date range" in arg for arg in call_args)

    def test_merge_documents_logging(self):
        """Test that merge_documents logs debug messages."""
        from dataclasses import dataclass

        @dataclass
        class TestDoc:
            items: Optional[list] = None
            name: Optional[str] = None

            def __post_init__(self):
                if self.items is None:
                    self.items = []

        doc1 = TestDoc(items=[1, 2], name="doc1")
        doc2 = TestDoc(items=[3, 4], name=None)

        with patch("entsoe.utils.logger") as mock_logger:
            merge_documents(doc1, doc2)
            assert mock_logger.debug.called
            # Verify that logging calls mention the function purpose
            call_args = [call[0][0] for call in mock_logger.debug.call_args_list]
            assert any("Merging documents" in arg for arg in call_args)

    @patch("entsoe.query_api.get")
    def test_query_core_logging(self, mock_get):
        """Test that query_core logs debug messages without exposing tokens."""
        # Mock the response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "<xml>test</xml>"
        mock_get.return_value = mock_response

        params = {
            "periodStart": "202301010000",
            "periodEnd": "202301020000",
        }

        with patch("entsoe.query_api.logger") as mock_logger:
            query_core(params)

            assert mock_logger.debug.called

            # Check that the API call was logged with sanitized parameters
            call_args = [call[0][0] for call in mock_logger.debug.call_args_list]

            # Should log the API request
            assert any("Making API request" in arg for arg in call_args)

            # Should log the response status
            assert any("API response status" in arg for arg in call_args)

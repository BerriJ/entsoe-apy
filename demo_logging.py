#!/usr/bin/env python3
"""
Demonstration script for the new debug logging functionality.
This script shows how the logging works and that security tokens are properly masked.
"""

import sys
from loguru import logger
from unittest.mock import Mock, patch

# Configure loguru to output to stdout for demonstration
logger.remove()  # Remove default handler
logger.add(sys.stdout, level="DEBUG", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}")

# Import the modules we added logging to
from entsoe.query_api import _sanitize_params_for_logging, query_core
from entsoe.utils import check_date_range_limit, split_date_range, merge_documents
from entsoe.decorators import range_limited, acknowledgement, pagination

def demonstrate_logging():
    """Demonstrate the logging functionality."""
    
    print("=" * 60)
    print("ENTSOE-APY Debug Logging Demonstration")
    print("=" * 60)
    
    print("\n1. Demonstrating parameter sanitization for logging:")
    print("-" * 50)
    
    # Example with security token
    params_with_token = {
        "securityToken": "very-secret-token-12345",
        "periodStart": "202301010000",
        "periodEnd": "202301020000",
        "documentType": "A44"
    }
    
    print("Original params:", params_with_token)
    sanitized = _sanitize_params_for_logging(params_with_token)
    print("Sanitized params:", sanitized)
    
    print("\n2. Demonstrating utility function logging:")
    print("-" * 50)
    
    # Test date range checking
    print("\nTesting date range limit check:")
    result = check_date_range_limit(202301010000, 202301050000, 365)
    print(f"Result: {result}")
    
    # Test date range splitting
    print("\nTesting date range splitting:")
    pivot, end = split_date_range(202301010000, 202301100000)
    print(f"Pivot: {pivot}, End: {end}")
    
    print("\n3. Demonstrating query_core logging (mocked):")
    print("-" * 50)
    
    # Mock the HTTP response to avoid making real API calls
    with patch('entsoe.query_api.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "<xml>test response</xml>"
        mock_get.return_value = mock_response
        
        print("\nMaking mocked API call with security token:")
        response = query_core(params_with_token, timeout=10)
        print(f"Response status: {response.status_code}")
    
    print("\n4. Demonstrating decorator logging:")
    print("-" * 50)
    
    # Create a simple function to demonstrate decorator logging
    @range_limited
    def dummy_api_function(params, *args, **kwargs):
        """Dummy function to test decorator logging."""
        return f"Called with params: {params}"
    
    print("\nTesting range_limited decorator:")
    test_params = {
        "periodStart": 202301010000,
        "periodEnd": 202301020000,  # Short range - won't trigger splitting
        "other_param": "value"
    }
    result = dummy_api_function(test_params)
    print(f"Function result: {result}")
    
    print("\n" + "=" * 60)
    print("Logging demonstration complete!")
    print("Notice how security tokens are masked as '***MASKED***' in all log output.")
    print("=" * 60)

if __name__ == "__main__":
    demonstrate_logging()
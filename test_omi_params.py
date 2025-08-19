#!/usr/bin/env python3
"""Test script for OMI parameter class."""

import os
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from entsoe_api_py.Base.OMI import OMIParams


def test_omi_params():
    """Test OMI parameter class functionality."""

    # Test data
    security_token = "test_token_12345"
    period_start = 202401010000
    period_end = 202401020000
    control_area_domain = "10YFR-RTE------C"  # France RTE

    print("Testing OMI Parameter Class")
    print("=" * 50)

    # Test 1: Basic functionality with valid A05 status
    print("\n1. Testing basic functionality with A05 status...")
    try:
        omi = OMIParams(
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            control_area_domain=control_area_domain,
            doc_status="A05",
        )
        assert omi.params["documentType"] == "B47", "Document type should be B47"
        assert omi.params["docStatus"] == "A05", "Doc status should be A05"
        print("✓ A05 status validation: PASSED")
    except Exception as e:
        print(f"✗ A05 status validation: FAILED - {e}")
        return False

    # Test 2: Valid A09 status
    print("\n2. Testing A09 status...")
    try:
        omi = OMIParams(
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            control_area_domain=control_area_domain,
            doc_status="A09",
        )
        assert omi.params["docStatus"] == "A09", "Doc status should be A09"
        print("✓ A09 status validation: PASSED")
    except Exception as e:
        print(f"✗ A09 status validation: FAILED - {e}")
        return False

    # Test 3: Valid A13 status
    print("\n3. Testing A13 status...")
    try:
        omi = OMIParams(
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            control_area_domain=control_area_domain,
            doc_status="A13",
        )
        assert omi.params["docStatus"] == "A13", "Doc status should be A13"
        print("✓ A13 status validation: PASSED")
    except Exception as e:
        print(f"✗ A13 status validation: FAILED - {e}")
        return False

    # Test 4: Invalid status should raise ValueError
    print("\n4. Testing invalid status validation...")
    try:
        omi = OMIParams(
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            control_area_domain=control_area_domain,
            doc_status="INVALID",
        )
        print("✗ Invalid status validation: FAILED - Should have raised ValueError")
        return False
    except ValueError as e:
        if "doc_status must be one of ['A05', 'A09', 'A13']" in str(e):
            print("✓ Invalid status validation: PASSED")
        else:
            print(f"✗ Invalid status validation: FAILED - Wrong error message: {e}")
            return False
    except Exception as e:
        print(f"✗ Invalid status validation: FAILED - Unexpected error: {e}")
        return False

    # Test 5: No doc_status (should be optional)
    print("\n5. Testing optional doc_status...")
    try:
        omi = OMIParams(
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            control_area_domain=control_area_domain,
        )
        assert "docStatus" not in omi.params, (
            "Doc status should not be in params when not provided"
        )
        print("✓ Optional doc_status: PASSED")
    except Exception as e:
        print(f"✗ Optional doc_status: FAILED - {e}")
        return False

    # Test 6: Document type is always B47
    print("\n6. Testing fixed document type...")
    try:
        omi = OMIParams(
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            control_area_domain=control_area_domain,
        )
        assert omi.params["documentType"] == "B47", "Document type must always be B47"
        print("✓ Fixed document type: PASSED")
    except Exception as e:
        print(f"✗ Fixed document type: FAILED - {e}")
        return False

    # Test 7: Update period parameters
    print("\n7. Testing update period parameters...")
    try:
        omi = OMIParams(
            security_token=security_token,
            period_start_update=period_start,
            period_end_update=period_end,
            control_area_domain=control_area_domain,
        )
        assert omi.params["periodStartUpdate"] == period_start, (
            "Period start update should be set"
        )
        assert omi.params["periodEndUpdate"] == period_end, (
            "Period end update should be set"
        )
        print("✓ Update period parameters: PASSED")
    except Exception as e:
        print(f"✗ Update period parameters: FAILED - {e}")
        return False

    # Test 8: Complete parameter test
    print("\n8. Testing complete parameter set...")
    try:
        omi = OMIParams(
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            control_area_domain=control_area_domain,
            doc_status="A05",
            m_rid="test_mrid_123",
            timeout=120,
            offset=100,
        )
        expected_params = {
            "documentType": "B47",
            "securityToken": security_token,
            "periodStart": period_start,
            "periodEnd": period_end,
            "controlArea_Domain": control_area_domain,
            "docStatus": "A05",
            "mRID": "test_mrid_123",
            "offset": 100,
        }

        for key, expected_value in expected_params.items():
            assert omi.params.get(key) == expected_value, f"Parameter {key} mismatch"

        assert omi.timeout == 120, "Timeout should be set correctly"
        print("✓ Complete parameter test: PASSED")
    except Exception as e:
        print(f"✗ Complete parameter test: FAILED - {e}")
        return False

    print("\n" + "=" * 50)
    print("🎉 All OMI parameter tests PASSED!")
    return True


def main():
    """Run the OMI parameter tests."""
    success = test_omi_params()
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()

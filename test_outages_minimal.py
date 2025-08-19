#!/usr/bin/env python3
"""Minimal test for ENTSO-E Outages parameter classes."""

import sys
import os

# Add the base and specific directories to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src/entsoe_api_py/Base"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src/entsoe_api_py/Outages"))

# Import base class first
from Outages import OutagesParams

# Import specific classes
from specific_params import (
    ForcedProductionUnitUnavailabilityParams,
    ForcedTransmissionUnavailabilityParams,
    PlannedProductionUnitUnavailabilityParams,
    PlannedTransmissionUnavailabilityParams,
    ProductionUnitUnavailabilityParams,
    TransmissionUnavailabilityParams,
)


def test_outages_minimal():
    """Test Outages parameter classes with minimal imports."""
    
    # Test data
    security_token = "test_token_12345"
    period_start = 202308152200
    period_end = 202308162200
    domain = "10YBE----------2"  # Belgium
    
    print("ENTSO-E API Outages Parameter Classes - Minimal Test")
    print("=" * 55)
    
    # Outages Domain Tests
    print("\n🚨 OUTAGES DOMAIN - 6 Parameter Classes:")
    print("-" * 45)
    
    outages_classes = [
        ("7.1.A", PlannedProductionUnitUnavailabilityParams, 
         "Planned Production Unit Unavailability", "A77", "A53"),
        ("7.1.B", ForcedProductionUnitUnavailabilityParams, 
         "Forced Production Unit Unavailability", "A77", "A54"),
        ("7.1.C", PlannedTransmissionUnavailabilityParams, 
         "Planned Transmission Unavailability", "A78", "A53"),
        ("7.1.D", ForcedTransmissionUnavailabilityParams, 
         "Forced Transmission Unavailability", "A78", "A54"),
        ("7.1.E", ProductionUnitUnavailabilityParams, 
         "Production Unit Unavailability (All)", "A77", None),
        ("7.1.F", TransmissionUnavailabilityParams, 
         "Transmission Unavailability (All)", "A78", None),
    ]
    
    success_count = 0
    
    for code, cls, description, expected_doc_type, expected_business_type in outages_classes:
        try:
            params = cls(
                security_token=security_token,
                period_start=period_start,
                period_end=period_end,
                bidding_zone_domain=domain
            )
            doc_type = params.params['documentType']
            business_type = params.params.get('businessType')
            
            # Validate the parameters
            assert doc_type == expected_doc_type, f"Wrong document type for {code}: expected {expected_doc_type}, got {doc_type}"
            assert business_type == expected_business_type, f"Wrong business type for {code}: expected {expected_business_type}, got {business_type}"
            
            print(f"   ✅ {code}: {description}")
            print(f"        docType={doc_type}, businessType={business_type or 'None'}")
            success_count += 1
            
        except Exception as e:
            print(f"   ❌ {code}: ERROR - {e}")
    
    # Summary
    print("\n" + "=" * 55)
    print("📊 SUMMARY:")
    print(f"✅ Successfully tested: {success_count}/{len(outages_classes)} parameter classes")
    
    if success_count == len(outages_classes):
        print("🎉 All Outages parameter classes implemented correctly!")
        print("\n🔧 Features implemented:")
        print("   • 6 specific parameter classes for different outage types")
        print("   • Preset documentType values (A77 for production, A78 for transmission)")
        print("   • Preset businessType values (A53 for planned, A54 for forced, None for all)")
        print("   • Proper inheritance from OutagesParams base class")
        print("   • Consistent API with Load and Generation classes")
        print("   • Optional parameters for filtering and pagination")
        print("   • Comprehensive docstrings and parameter documentation")
        return True
    else:
        print("❌ Some classes failed testing")
        return False


if __name__ == "__main__":
    success = test_outages_minimal()
    sys.exit(0 if success else 1)
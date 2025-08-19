#!/usr/bin/env python3
"""Test script for ENTSO-E Outages parameter classes."""

import os
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from entsoe_api_py.Outages import (
    ForcedProductionUnitUnavailabilityParams,
    ForcedTransmissionUnavailabilityParams,
    PlannedProductionUnitUnavailabilityParams,
    PlannedTransmissionUnavailabilityParams,
    ProductionUnitUnavailabilityParams,
    TransmissionUnavailabilityParams,
)


def test_outages_params():
    """Test all Outages parameter classes."""
    
    # Test data
    security_token = "test_token_12345"
    period_start = 202308152200
    period_end = 202308162200
    domain = "10YBE----------2"  # Belgium
    
    print("ENTSO-E API Outages Parameter Classes - Test")
    print("=" * 50)
    
    # Outages Domain Tests
    print("\n🚨 OUTAGES DOMAIN - 6 Parameter Classes:")
    print("-" * 40)
    
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
    
    for code, cls, description, expected_doc_type, expected_business_type in outages_classes:
        params = cls(
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=domain
        )
        doc_type = params.params['documentType']
        business_type = params.params.get('businessType')
        
        # Validate the parameters
        assert doc_type == expected_doc_type, f"Wrong document type for {code}"
        assert business_type == expected_business_type, f"Wrong business type for {code}"
        
        print(f"   {code}: {description}")
        print(f"        docType={doc_type}, businessType={business_type or 'None'}")
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 SUMMARY:")
    print(f"✅ Outages Domain: {len(outages_classes)} parameter classes implemented")
    print("\n🎯 All classes inherit from OutagesParams:")
    print("   • Outages classes inherit from OutagesParams")
    print("   • OutagesParams inherits from BaseParams")
    print("\n🔧 Each class provides:")
    print("   • Preset documentType values (A77 for production, A78 for transmission)")
    print("   • Preset businessType values (A53 for planned, A54 for forced, None for all)")
    print("   • Proper parameter validation and structure")
    print("   • Easy-to-use constructor with required parameters")
    print("   • Optional parameters for filtering (registered_resource, etc.)")


if __name__ == "__main__":
    test_outages_params()
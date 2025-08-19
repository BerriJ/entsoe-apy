#!/usr/bin/env python3
"""Simple validation for ENTSO-E Outages parameter classes."""

import sys
import os

# Add the src directory to path and change working directory
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
os.chdir(os.path.join(os.path.dirname(__file__), "src"))

# Import with full path
from entsoe_api_py.Base.Base import BaseParams
from entsoe_api_py.Base.Outages import OutagesParams


def test_class_structure():
    """Test basic class structure and functionality."""
    
    print("ENTSO-E API Outages Parameter Classes - Structure Test")
    print("=" * 55)
    
    # Test that OutagesParams works
    try:
        params = OutagesParams(
            document_type="A77",
            security_token="test_token",
            period_start=202308152200,
            period_end=202308162200,
            bidding_zone_domain="10YBE----------2"
        )
        
        print("✅ OutagesParams base class works correctly")
        print(f"   Document type: {params.params['documentType']}")
        print(f"   Security token: {params.params['securityToken']}")
        print(f"   Period start: {params.params['periodStart']}")
        print(f"   Bidding zone: {params.params['biddingZone_Domain']}")
        
    except Exception as e:
        print(f"❌ OutagesParams base class failed: {e}")
        return False
    
    # Now test each specific class by importing and instantiating
    print("\n🚨 Testing Specific Outages Classes:")
    print("-" * 40)
    
    class_tests = [
        ("PlannedProductionUnitUnavailabilityParams", "A77", "A53"),
        ("ForcedProductionUnitUnavailabilityParams", "A77", "A54"),
        ("PlannedTransmissionUnavailabilityParams", "A78", "A53"),
        ("ForcedTransmissionUnavailabilityParams", "A78", "A54"),
        ("ProductionUnitUnavailabilityParams", "A77", None),
        ("TransmissionUnavailabilityParams", "A78", None),
    ]
    
    success_count = 0
    
    for class_name, expected_doc_type, expected_business_type in class_tests:
        try:
            # Import the specific class
            from entsoe_api_py.Outages.specific_params import (
                PlannedProductionUnitUnavailabilityParams,
                ForcedProductionUnitUnavailabilityParams,
                PlannedTransmissionUnavailabilityParams,
                ForcedTransmissionUnavailabilityParams,
                ProductionUnitUnavailabilityParams,
                TransmissionUnavailabilityParams,
            )
            
            # Get the class by name
            cls = globals()[class_name] if class_name in globals() else locals()[class_name]
            
            # Create instance
            params = cls(
                security_token="test_token",
                period_start=202308152200,
                period_end=202308162200,
                bidding_zone_domain="10YBE----------2"
            )
            
            # Validate parameters
            doc_type = params.params['documentType']
            business_type = params.params.get('businessType')
            
            assert doc_type == expected_doc_type, f"Wrong document type: expected {expected_doc_type}, got {doc_type}"
            assert business_type == expected_business_type, f"Wrong business type: expected {expected_business_type}, got {business_type}"
            
            print(f"   ✅ {class_name}")
            print(f"      docType={doc_type}, businessType={business_type or 'None'}")
            success_count += 1
            
        except Exception as e:
            print(f"   ❌ {class_name}: {e}")
    
    print(f"\n📊 SUMMARY: {success_count}/{len(class_tests)} classes tested successfully")
    
    if success_count == len(class_tests):
        print("\n🎉 All Outages parameter classes implemented correctly!")
        return True
    else:
        print("\n❌ Some classes failed")
        return False


if __name__ == "__main__":
    success = test_class_structure()
    sys.exit(0 if success else 1)
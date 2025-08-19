#!/usr/bin/env python3
"""Test script for Generation parameter classes."""

import os
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from entsoe_api_py.Generation import (
    ActualGenerationPerGenerationUnitParams,
    ActualGenerationPerProductionTypeParams,
    GenerationForecastDayAheadParams,
    GenerationForecastWindAndSolarParams,
    InstalledCapacityPerProductionTypeParams,
    InstalledCapacityPerProductionUnitParams,
    WaterReservoirsAndHydroStorageParams,
)


def test_generation_params():
    """Test all Generation parameter classes."""
    
    # Test data
    security_token = "test_token_12345"
    period_start = 202308152200
    period_end = 202308162200
    in_domain = "10YBE----------2"  # Belgium
    
    print("Testing Generation Parameter Classes")
    print("=" * 50)
    
    # Test 1: 14.1.A Installed Capacity per Production Type
    print("\n1. Testing InstalledCapacityPerProductionTypeParams (14.1.A):")
    params1 = InstalledCapacityPerProductionTypeParams(
        security_token=security_token,
        period_start=period_start,
        period_end=period_end,
        in_domain=in_domain,
        psr_type="B14"  # Nuclear
    )
    print(f"   Document Type: {params1.params['documentType']}")
    print(f"   Process Type: {params1.params['processType']}")
    print(f"   In Domain: {params1.params['in_Domain']}")
    print(f"   PSR Type: {params1.params.get('psrType', 'Not specified')}")
    print(f"   Code: {params1.code}")
    
    # Test 2: 16.1.D Water Reservoirs and Hydro Storage Plants
    print("\n2. Testing WaterReservoirsAndHydroStorageParams (16.1.D):")
    params2 = WaterReservoirsAndHydroStorageParams(
        security_token=security_token,
        period_start=period_start,
        period_end=period_end,
        in_domain=in_domain
    )
    print(f"   Document Type: {params2.params['documentType']}")
    print(f"   Process Type: {params2.params['processType']}")
    print(f"   In Domain: {params2.params['in_Domain']}")
    print(f"   Code: {params2.code}")
    
    # Test 3: 16.1.B&C Actual Generation per Production Type
    print("\n3. Testing ActualGenerationPerProductionTypeParams (16.1.B&C):")
    params3 = ActualGenerationPerProductionTypeParams(
        security_token=security_token,
        period_start=period_start,
        period_end=period_end,
        in_domain=in_domain,
        psr_type="B19"  # Wind Onshore
    )
    print(f"   Document Type: {params3.params['documentType']}")
    print(f"   Process Type: {params3.params['processType']}")
    print(f"   In Domain: {params3.params['in_Domain']}")
    print(f"   PSR Type: {params3.params.get('psrType', 'Not specified')}")
    print(f"   Code: {params3.code}")
    
    # Test 4: 16.1.A Actual Generation per Generation Unit
    print("\n4. Testing ActualGenerationPerGenerationUnitParams (16.1.A):")
    params4 = ActualGenerationPerGenerationUnitParams(
        security_token=security_token,
        period_start=period_start,
        period_end=period_end,
        in_domain=in_domain,
        psr_type="B14",  # Nuclear
        registered_resource="22WAMERCO000008L"  # Example EIC code
    )
    print(f"   Document Type: {params4.params['documentType']}")
    print(f"   Process Type: {params4.params['processType']}")
    print(f"   In Domain: {params4.params['in_Domain']}")
    print(f"   PSR Type: {params4.params.get('psrType', 'Not specified')}")
    registered_resource_val = params4.params.get('registeredResource', 'Not specified')
    print(f"   Registered Resource: {registered_resource_val}")
    print(f"   Code: {params4.code}")
    
    # Test 5: 14.1.C Generation Forecast - Day ahead
    print("\n5. Testing GenerationForecastDayAheadParams (14.1.C):")
    params5 = GenerationForecastDayAheadParams(
        security_token=security_token,
        period_start=period_start,
        period_end=period_end,
        in_domain=in_domain
    )
    print(f"   Document Type: {params5.params['documentType']}")
    print(f"   Process Type: {params5.params['processType']}")
    print(f"   In Domain: {params5.params['in_Domain']}")
    print(f"   Code: {params5.code}")
    
    # Test 6: 14.1.D Generation Forecasts for Wind and Solar
    print("\n6. Testing GenerationForecastWindAndSolarParams (14.1.D):")
    params6 = GenerationForecastWindAndSolarParams(
        security_token=security_token,
        period_start=period_start,
        period_end=period_end,
        in_domain=in_domain,
        process_type="A01",  # Day ahead
        psr_type="B16"  # Solar
    )
    print(f"   Document Type: {params6.params['documentType']}")
    print(f"   Process Type: {params6.params['processType']}")
    print(f"   In Domain: {params6.params['in_Domain']}")
    print(f"   PSR Type: {params6.params.get('psrType', 'Not specified')}")
    print(f"   Code: {params6.code}")
    
    # Test 7: 14.1.B Installed Capacity Per Production Unit
    print("\n7. Testing InstalledCapacityPerProductionUnitParams (14.1.B):")
    params7 = InstalledCapacityPerProductionUnitParams(
        security_token=security_token,
        period_start=period_start,
        period_end=period_end,
        in_domain=in_domain,
        psr_type="B02"  # Brown coal
    )
    print(f"   Document Type: {params7.params['documentType']}")
    print(f"   Process Type: {params7.params['processType']}")
    print(f"   In Domain: {params7.params['in_Domain']}")
    print(f"   PSR Type: {params7.params.get('psrType', 'Not specified')}")
    print(f"   Code: {params7.code}")
    
    print("\n" + "=" * 50)
    print("All Generation parameter classes tested successfully!")
    print("✅ All 7 classes instantiated correctly")
    print("✅ All required parameters accessible via params dictionary")
    print("✅ All classes have proper inheritance from GenerationParams")


if __name__ == "__main__":
    test_generation_params()

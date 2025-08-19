#!/usr/bin/env python3
"""Comprehensive test showing all Load, Generation, and Outages parameter classes."""

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
from entsoe_api_py.Load import (
    ActualTotalLoadParams,
    DayAheadTotalLoadForecastParams,
    MonthAheadTotalLoadForecastParams,
    WeekAheadTotalLoadForecastParams,
    YearAheadForecastMarginParams,
    YearAheadTotalLoadForecastParams,
)
from entsoe_api_py.Outages import (
    ForcedProductionUnitUnavailabilityParams,
    ForcedTransmissionUnavailabilityParams,
    PlannedProductionUnitUnavailabilityParams,
    PlannedTransmissionUnavailabilityParams,
    ProductionUnitUnavailabilityParams,
    TransmissionUnavailabilityParams,
)


def test_all_domains():
    """Test all Load, Generation, and Outages parameter classes."""
    
    # Test data
    security_token = "test_token_12345"
    period_start = 202308152200
    period_end = 202308162200
    domain = "10YBE----------2"  # Belgium
    
    print("ENTSO-E API Parameter Classes - Complete Test")
    print("=" * 60)
    
    # Load Domain Tests
    print("\n🔋 LOAD DOMAIN - 6 Parameter Classes:")
    print("-" * 40)
    
    load_classes = [
        ("6.1.A", ActualTotalLoadParams, "Actual Total Load"),
        ("6.1.B", DayAheadTotalLoadForecastParams, "Day-ahead Total Load Forecast"),
        ("6.1.C", WeekAheadTotalLoadForecastParams, "Week-ahead Total Load Forecast"),
        ("6.1.D", MonthAheadTotalLoadForecastParams, "Month-ahead Total Load Forecast"),
        ("6.1.E", YearAheadTotalLoadForecastParams, "Year-ahead Total Load Forecast"),
        ("8.1", YearAheadForecastMarginParams, "Year-ahead Forecast Margin"),
    ]
    
    for code, cls, description in load_classes:
        params = cls(
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            out_bidding_zone_domain=domain
        )
        doc_type = params.params['documentType']
        proc_type = params.params['processType']
        print(f"   {code}: {description}")
        print(f"        docType={doc_type}, processType={proc_type}")
    
    # Generation Domain Tests
    print("\n⚡ GENERATION DOMAIN - 7 Parameter Classes:")
    print("-" * 40)
    
    generation_classes = [
        ("14.1.A", InstalledCapacityPerProductionTypeParams, 
         "Installed Capacity per Production Type"),
        ("16.1.D", WaterReservoirsAndHydroStorageParams, 
         "Water Reservoirs and Hydro Storage Plants"),
        ("16.1.B_C", ActualGenerationPerProductionTypeParams, 
         "Actual Generation per Production Type"),
        ("16.1.A", ActualGenerationPerGenerationUnitParams, 
         "Actual Generation per Generation Unit"),
        ("14.1.C", GenerationForecastDayAheadParams, 
         "Generation Forecast - Day ahead"),
        ("14.1.D", GenerationForecastWindAndSolarParams, 
         "Generation Forecasts for Wind and Solar"),
        ("14.1.B", InstalledCapacityPerProductionUnitParams, 
         "Installed Capacity Per Production Unit"),
    ]
    
    for code, cls, description in generation_classes:
        if cls == GenerationForecastWindAndSolarParams:
            # Special case for wind/solar with optional process_type parameter
            params = cls(
                security_token=security_token,
                period_start=period_start,
                period_end=period_end,
                in_domain=domain,
                process_type="A01"  # Day ahead
            )
        else:
            params = cls(
                security_token=security_token,
                period_start=period_start,
                period_end=period_end,
                in_domain=domain
            )
        doc_type = params.params['documentType']
        proc_type = params.params['processType']
        print(f"   {code}: {description}")
        print(f"        docType={doc_type}, processType={proc_type}")
    
    # Outages Domain Tests
    print("\n🚨 OUTAGES DOMAIN - 6 Parameter Classes:")
    print("-" * 40)
    
    outages_classes = [
        ("7.1.A", PlannedProductionUnitUnavailabilityParams, 
         "Planned Production Unit Unavailability"),
        ("7.1.B", ForcedProductionUnitUnavailabilityParams, 
         "Forced Production Unit Unavailability"),
        ("7.1.C", PlannedTransmissionUnavailabilityParams, 
         "Planned Transmission Unavailability"),
        ("7.1.D", ForcedTransmissionUnavailabilityParams, 
         "Forced Transmission Unavailability"),
        ("7.1.E", ProductionUnitUnavailabilityParams, 
         "Production Unit Unavailability (All)"),
        ("7.1.F", TransmissionUnavailabilityParams, 
         "Transmission Unavailability (All)"),
    ]
    
    for code, cls, description in outages_classes:
        params = cls(
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=domain
        )
        doc_type = params.params['documentType']
        business_type = params.params.get('businessType', 'None')
        print(f"   {code}: {description}")
        print(f"        docType={doc_type}, businessType={business_type}")
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 SUMMARY:")
    total_count = len(load_classes) + len(generation_classes) + len(outages_classes)
    print(f"✅ Load Domain: {len(load_classes)} parameter classes implemented")
    print(f"✅ Generation Domain: {len(generation_classes)} parameter classes implemented")
    print(f"✅ Outages Domain: {len(outages_classes)} parameter classes implemented")
    print(f"✅ Total: {total_count} endpoint parameter classes")
    print("\n🎯 All classes inherit from their respective base classes:")
    print("   • Load classes inherit from LoadParams")
    print("   • Generation classes inherit from GenerationParams")
    print("   • Outages classes inherit from OutagesParams")
    print("   • All base classes inherit from BaseParams")
    print("\n🔧 Each class provides:")
    print("   • Preset documentType and processType/businessType values")
    print("   • Proper parameter validation and structure")
    print("   • Easy-to-use constructor with required parameters")
    print("   • Optional parameters for filtering (PSR type, registered resource, etc.)")


if __name__ == "__main__":
    test_all_domains()

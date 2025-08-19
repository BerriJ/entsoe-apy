"""Tests for Transmission parameter classes."""

import pytest

from entsoe_api_py.Transmission import (
    CommercialSchedulesParams,
    CrossBorderPhysicalFlowsParams,
    ExplicitAllocationsOfferedCapacityParams,
    FlowBasedAllocationsParams,
    ForecastedTransferCapacitiesParams,
    ImplicitAllocationsOfferedCapacityParams,
    TotalCapacityAlreadyAllocatedParams,
    TotalNominatedCapacityParams,
    TransmissionParams,
    UnavailabilityOffshoreGridInfrastructureParams,
    UnavailabilityTransmissionInfrastructureParams,
)


class TestTransmissionParams:
    """Test the base TransmissionParams class."""

    def test_transmission_params_instantiation(self):
        """Test basic instantiation of TransmissionParams."""
        params = TransmissionParams(
            document_type="A11",
            security_token="test_token",
            period_start=202312312300,
            period_end=202401012300,
            out_domain="10YGB----------A",
            in_domain="10YBE----------2",
        )
        
        assert params.params["documentType"] == "A11"
        assert params.params["securityToken"] == "test_token"
        assert params.params["periodStart"] == 202312312300
        assert params.params["periodEnd"] == 202401012300
        assert params.params["out_Domain"] == "10YGB----------A"
        assert params.params["in_Domain"] == "10YBE----------2"


class TestTotalNominatedCapacityParams:
    """Test TotalNominatedCapacityParams class."""

    def test_instantiation(self):
        """Test instantiation with required parameters."""
        params = TotalNominatedCapacityParams(
            security_token="test_token",
            period_start=202312312300,
            period_end=202401012300,
            out_domain="10YGB----------A",
            in_domain="10YBE----------2",
        )
        
        assert params.params["documentType"] == "A26"
        assert params.params["businessType"] == "B08"
        assert params.code == "12.1.B"

    def test_with_optional_parameters(self):
        """Test instantiation with optional parameters."""
        params = TotalNominatedCapacityParams(
            security_token="test_token",
            period_start=202312312300,
            period_end=202401012300,
            out_domain="10YGB----------A",
            in_domain="10YBE----------2",
            timeout=120,
            offset=10,
        )
        
        assert params.timeout == 120
        assert params.params["offset"] == 10


class TestImplicitAllocationsOfferedCapacityParams:
    """Test ImplicitAllocationsOfferedCapacityParams class."""

    def test_instantiation(self):
        """Test instantiation with required parameters."""
        params = ImplicitAllocationsOfferedCapacityParams(
            security_token="test_token",
            period_start=202312312300,
            period_end=202401012300,
            out_domain="10YGB----------A",
            in_domain="10YBE----------2",
        )
        
        assert params.params["documentType"] == "A31"
        assert params.params["auction.Type"] == "A01"
        assert params.params["contract_MarketAgreement.Type"] == "A01"
        assert params.code == "11.1"


class TestExplicitAllocationsOfferedCapacityParams:
    """Test ExplicitAllocationsOfferedCapacityParams class."""

    def test_instantiation(self):
        """Test instantiation with required parameters."""
        params = ExplicitAllocationsOfferedCapacityParams(
            security_token="test_token",
            period_start=202312312300,
            period_end=202401012300,
            out_domain="10YGB----------A",
            in_domain="10YBE----------2",
        )
        
        assert params.params["documentType"] == "A31"
        assert params.params["auction.Type"] == "A02"
        assert params.params["contract_MarketAgreement.Type"] == "A01"
        assert params.code == "11.1.A"


class TestTotalCapacityAlreadyAllocatedParams:
    """Test TotalCapacityAlreadyAllocatedParams class."""

    def test_instantiation(self):
        """Test instantiation with required parameters."""
        params = TotalCapacityAlreadyAllocatedParams(
            security_token="test_token",
            period_start=202312312300,
            period_end=202401012300,
            out_domain="10YGB----------A",
            in_domain="10YBE----------2",
        )
        
        assert params.params["documentType"] == "A26"
        assert params.params["businessType"] == "A29"
        assert params.params["contract_MarketAgreement.Type"] == "A01"
        assert params.code == "12.1.C"


class TestCrossBorderPhysicalFlowsParams:
    """Test CrossBorderPhysicalFlowsParams class."""

    def test_instantiation(self):
        """Test instantiation with required parameters."""
        params = CrossBorderPhysicalFlowsParams(
            security_token="test_token",
            period_start=202312312300,
            period_end=202401012300,
            out_domain="10YGB----------A",
            in_domain="10YBE----------2",
        )
        
        assert params.params["documentType"] == "A11"
        assert params.code == "12.1.G"


class TestCommercialSchedulesParams:
    """Test CommercialSchedulesParams class."""

    def test_instantiation(self):
        """Test instantiation with required parameters."""
        params = CommercialSchedulesParams(
            security_token="test_token",
            period_start=202312312300,
            period_end=202401012300,
            out_domain="10YGB----------A",
            in_domain="10YBE----------2",
        )
        
        assert params.params["documentType"] == "A09"
        assert params.params["contract_MarketAgreement.Type"] == "A01"
        assert params.code == "12.1.F"


class TestForecastedTransferCapacitiesParams:
    """Test ForecastedTransferCapacitiesParams class."""

    def test_instantiation(self):
        """Test instantiation with required parameters."""
        params = ForecastedTransferCapacitiesParams(
            security_token="test_token",
            period_start=202312312300,
            period_end=202401012300,
            out_domain="10YGB----------A",
            in_domain="10YBE----------2",
        )
        
        assert params.params["documentType"] == "A61"
        assert params.params["contract_MarketAgreement.Type"] == "A01"
        assert params.code == "11.1.A"


class TestFlowBasedAllocationsParams:
    """Test FlowBasedAllocationsParams class."""

    def test_instantiation(self):
        """Test instantiation with required parameters."""
        params = FlowBasedAllocationsParams(
            security_token="test_token",
            period_start=202312312300,
            period_end=202401012300,
            bidding_zone_domain="10YDOM-REGION-1V",
        )
        
        assert params.params["documentType"] == "B09"
        assert params.params["processType"] == "A44"
        assert params.params["biddingZone_Domain"] == "10YDOM-REGION-1V"
        assert params.code == "11.1.B"


class TestUnavailabilityTransmissionInfrastructureParams:
    """Test UnavailabilityTransmissionInfrastructureParams class."""

    def test_instantiation(self):
        """Test instantiation with required parameters."""
        params = UnavailabilityTransmissionInfrastructureParams(
            security_token="test_token",
            period_start=202312312300,
            period_end=202401012300,
            bidding_zone_domain="10YDOM-REGION-1V",
        )
        
        assert params.params["documentType"] == "A78"
        assert params.params["biddingZone_Domain"] == "10YDOM-REGION-1V"
        assert params.code == "10.1.A&B"


class TestUnavailabilityOffshoreGridInfrastructureParams:
    """Test UnavailabilityOffshoreGridInfrastructureParams class."""

    def test_instantiation(self):
        """Test instantiation with required parameters."""
        params = UnavailabilityOffshoreGridInfrastructureParams(
            security_token="test_token",
            period_start=202312312300,
            period_end=202401012300,
            bidding_zone_domain="10YDOM-REGION-1V",
        )
        
        assert params.params["documentType"] == "A79"
        assert params.params["biddingZone_Domain"] == "10YDOM-REGION-1V"
        assert params.code == "10.1.C"


class TestAllTransmissionClasses:
    """Test all transmission classes together."""

    def test_all_classes_have_required_attributes(self):
        """Test that all classes have required attributes."""
        transmission_classes = [
            TotalNominatedCapacityParams,
            ImplicitAllocationsOfferedCapacityParams,
            ExplicitAllocationsOfferedCapacityParams,
            TotalCapacityAlreadyAllocatedParams,
            CrossBorderPhysicalFlowsParams,
            CommercialSchedulesParams,
            ForecastedTransferCapacitiesParams,
            FlowBasedAllocationsParams,
            UnavailabilityTransmissionInfrastructureParams,
            UnavailabilityOffshoreGridInfrastructureParams,
        ]
        
        for cls in transmission_classes:
            # Check that class has code attribute
            assert hasattr(cls, "code")
            assert isinstance(cls.code, str)
            assert len(cls.code) > 0
            
            # Check that class has proper docstring
            assert cls.__doc__ is not None
            assert len(cls.__doc__.strip()) > 0

    def test_all_classes_inherit_from_transmission_params(self):
        """Test that all classes inherit from TransmissionParams."""
        transmission_classes = [
            TotalNominatedCapacityParams,
            ImplicitAllocationsOfferedCapacityParams,
            ExplicitAllocationsOfferedCapacityParams,
            TotalCapacityAlreadyAllocatedParams,
            CrossBorderPhysicalFlowsParams,
            CommercialSchedulesParams,
            ForecastedTransferCapacitiesParams,
            FlowBasedAllocationsParams,
            UnavailabilityTransmissionInfrastructureParams,
            UnavailabilityOffshoreGridInfrastructureParams,
        ]
        
        for cls in transmission_classes:
            assert issubclass(cls, TransmissionParams)
"""Specific parameter classes for ENTSO-E Market endpoints.

This module contains specialized parameter classes for different Market data endpoints,
each inheriting from MarketParams and providing preset values for fixed parameters.
"""

from typing import Literal, Optional

from .base import MarketParams


class ImplicitFlowBasedAllocationsCongestionIncomeParams(MarketParams):
    """Parameters for 12.1.E Implicit and Flow-based Allocations - Congestion Income.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/intradayImplicitAllocationsCongestionIncome/show
    https://transparency.entsoe.eu/transmission/r2/dailyFlowBasedImplicitAllocationsCongestionIncome/show

    Fixed parameters:
    - documentType: A25 (Allocation results)
    - businessType: B10 (Congestion income)
    """

    code = "12.1.E"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        in_domain: str,
        out_domain: str,
        contract_market_agreement_type: Literal["A01", "A07"] = "A01",
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize congestion income parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of a Border or Bidding Zone
            out_domain: EIC code of a Border or Bidding Zone
            contract_market_agreement_type: A01=Daily; A07=Intraday
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A25",  # Fixed: Allocation results
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=out_domain,
            business_type="B10",  # Fixed: Congestion income
            contract_market_agreement_type=contract_market_agreement_type,
            timeout=timeout,
            offset=offset,
        )


class TotalNominatedCapacityParams(MarketParams):
    """Parameters for 12.1.B Total Nominated Capacity.

    Data view:
    https://transparency.entsoe.eu/transmission-domain/r2/totalCapacityNominated/show

    Fixed parameters:
    - documentType: A26 (Capacity document)
    - businessType: B08 (Total nominated capacity)
    """

    code = "12.1.B"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        in_domain: str,
        out_domain: str,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize total nominated capacity parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of a Control Area or Bidding Zone
            out_domain: EIC code of a Control Area or Bidding Zone
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A26",  # Fixed: Capacity document
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=out_domain,
            business_type="B08",  # Fixed: Total nominated capacity
            timeout=timeout,
            offset=offset,
        )


class ImplicitAllocationsOfferedCapacityParams(MarketParams):
    """Parameters for 11.1 Implicit Allocations - Offered Transfer Capacity.

    Data view:
    https://transparency.entsoe.eu/transmission-domain/r2/implicitAllocationsIntraday/show
    https://transparency.entsoe.eu/transmission-domain/r2/implicitAllocationsDayAhead/show

    Fixed parameters:
    - documentType: A31 (Agreed capacity)
    - auction_Type: A01 (Implicit)
    """

    code = "11.1"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        in_domain: str,
        out_domain: str,
        contract_market_agreement_type: Literal["A01", "A07"] = "A01",
        update_date_and_or_time: Optional[str] = None,
        classification_sequence_position: Optional[int] = None,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize implicit allocations offered transfer capacity parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of Control Area, Bidding Zone or Aggregation
            out_domain: EIC code of Control Area, Bidding Zone or Aggregation
            contract_market_agreement_type: A01=Day ahead; A07=Intraday
            update_date_and_or_time: For Offered Capacity Evolution
            classification_sequence_position: Integer for classification
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A31",  # Fixed: Agreed capacity
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=out_domain,
            contract_market_agreement_type=contract_market_agreement_type,
            auction_type="A01",  # Fixed: Implicit
            timeout=timeout,
            offset=offset,
        )

        # Add optional parameters
        self.add_optional_param("Update_DateAndOrTime", update_date_and_or_time)
        param_name = "ClassificationSequence_AttributeInstanceComponent.Position"
        self.add_optional_param(param_name, classification_sequence_position)


class EnergyPricesParams(MarketParams):
    """Parameters for 12.1.D Energy Prices.

    Data view: https://transparency.entsoe.eu/market/prices/show

    Fixed parameters:
    - documentType: A44 (Price Document)

    Request Limits:
    - One year range limit applies

    Response Limits:
    - 100 documents (TimeSeries) - Offset parameter can be used
    - Minimum time interval ranges from part of day to 29 hours
    """

    code = "12.1.D"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        in_domain: str,
        out_domain: str,
        contract_market_agreement_type: Optional[Literal["A01", "A07"]] = None,
        classification_sequence_position: Optional[int] = None,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize energy prices parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of a Bidding Zone
            out_domain: EIC code of a Bidding Zone (must be same as in_domain)
            contract_market_agreement_type: A01=Day-ahead; A07=Intraday
            classification_sequence_position: Integer for classification
            timeout: Request timeout in seconds
            offset: Offset for pagination (max 4800, allows max 4900 documents)
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A44",  # Fixed: Price Document
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=out_domain,
            contract_market_agreement_type=contract_market_agreement_type,
            timeout=timeout,
            offset=offset,
        )

        # Add optional classification parameter
        param_name = "classificationSequence_AttributeInstanceComponent.position"
        self.add_optional_param(param_name, classification_sequence_position)


class TotalCapacityAllocatedParams(MarketParams):
    """Parameters for 12.1.C Total Capacity Already Allocated.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/totalCapacityAllocated/show

    Fixed parameters:
    - documentType: A26 (Capacity document)
    - businessType: B07 (Total allocated capacity)
    """

    code = "12.1.C"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        in_domain: str,
        out_domain: str,
        contract_market_agreement_type: Optional[Literal["A01", "A07"]] = None,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize total capacity already allocated parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of a Control Area or Bidding Zone
            out_domain: EIC code of a Control Area or Bidding Zone
            contract_market_agreement_type: A01=Daily; A07=Intraday
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A26",  # Fixed: Capacity document
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=out_domain,
            business_type="B07",  # Fixed: Total allocated capacity
            contract_market_agreement_type=contract_market_agreement_type,
            timeout=timeout,
            offset=offset,
        )


class ExplicitAllocationsOfferedCapacityParams(MarketParams):
    """Parameters for 11.1.A Explicit Allocations - Offered Transfer Capacity.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/explicitAllocationsIntraday/show

    Fixed parameters:
    - documentType: A31 (Agreed capacity)
    - auction_Type: A02 (Explicit)
    """

    code = "11.1.A"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        in_domain: str,
        out_domain: str,
        contract_market_agreement_type: Literal["A01", "A07"] = "A01",
        auction_category: Optional[str] = None,
        classification_sequence_position: Optional[int] = None,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize explicit allocations offered transfer capacity parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of Control Area, Bidding Zone or Aggregation
            out_domain: EIC code of Control Area, Bidding Zone or Aggregation
            contract_market_agreement_type: A01=Day ahead; A07=Intraday
            auction_category: Auction category (e.g., A04)
            classification_sequence_position: Integer for classification
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A31",  # Fixed: Agreed capacity
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=out_domain,
            contract_market_agreement_type=contract_market_agreement_type,
            auction_type="A02",  # Fixed: Explicit
            auction_category=auction_category,
            timeout=timeout,
            offset=offset,
        )

        # Add optional classification parameter
        param_name = "ClassificationSequence_AttributeInstanceComponent.Position"
        self.add_optional_param(param_name, classification_sequence_position)


class FlowBasedAllocationsParams(MarketParams):
    """Parameters for 11.1.B Flow Based Allocations.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/flowBasedAllocationsDayAhead/show

    Fixed parameters:
    - documentType: A94 (Flow-based allocations)
    - auction_Type: A01 (Implicit)
    """

    code = "11.1.B"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        in_domain: str,
        out_domain: str,
        # Only Day ahead for Flow Based
        contract_market_agreement_type: Literal["A01"] = "A01",
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize flow based allocations parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of Control Area, Bidding Zone or Aggregation
            out_domain: EIC code of Control Area, Bidding Zone or Aggregation
            contract_market_agreement_type: A01=Day ahead (Flow Based only)
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A94",  # Fixed: Flow-based allocations
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=out_domain,
            contract_market_agreement_type=contract_market_agreement_type,
            auction_type="A01",  # Fixed: Implicit
            timeout=timeout,
            offset=offset,
        )


class ContinuousAllocationsOfferedCapacityParams(MarketParams):
    """Parameters for 11.1 Continuous Allocations - Offered Transfer Capacity.

    Data view:
    https://transparency.entsoe.eu/transmission-domain/r2/implicitAllocationsIntraday/show
    https://transparency.entsoe.eu/transmission-domain/r2/implicitAllocationsDayAhead/show

    Fixed parameters:
    - documentType: B33 (Continuous capacity document)
    - auction_Type: A08 (Continuous)
    """

    code = "11.1"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        in_domain: str,
        out_domain: str,
        # Continuous is typically intraday
        contract_market_agreement_type: Literal["A07"] = "A07",
        business_type: Optional[str] = None,
        update_date_and_or_time: Optional[str] = None,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize continuous allocations offered transfer capacity parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of Control Area, Bidding Zone or Aggregation
            out_domain: EIC code of Control Area, Bidding Zone or Aggregation
            contract_market_agreement_type: A07=Intraday (Continuous)
            business_type: Business type (e.g., A31)
            update_date_and_or_time: Update date and time filter
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="B33",  # Fixed: Continuous capacity document
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=out_domain,
            business_type=business_type,
            contract_market_agreement_type=contract_market_agreement_type,
            auction_type="A08",  # Fixed: Continuous
            timeout=timeout,
            offset=offset,
        )

        # Add optional update parameter
        self.add_optional_param(
            "update_DateAndOrTime.dateTime", update_date_and_or_time
        )


class ExplicitAllocationsUseTransferCapacityParams(MarketParams):
    """Parameters for 12.1.A Explicit Allocations - Use of the Transfer Capacity.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/explicitAllocationsIntraday/show

    Fixed parameters:
    - documentType: A25 (Allocation result document)
    - businessType: B05 (Capacity allocated including price)
    """

    code = "12.1.A"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        in_domain: str,
        out_domain: str,
        contract_market_agreement_type: Literal[
            "A01", "A02", "A03", "A04", "A06", "A07", "A08"
        ] = "A07",
        auction_category: Optional[str] = None,
        classification_sequence_position: Optional[int] = None,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize explicit allocations use of transfer capacity parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of a Control Area, Bidding Zone or
                Bidding Zone Aggregation
            out_domain: EIC code of a Control Area, Bidding Zone or
                Bidding Zone Aggregation
            contract_market_agreement_type: A01=Day ahead; A02=Weekly;
                A03=Monthly; A04=Yearly; A06=Long Term; A07=Intraday;
                A08=Quarterly
            auction_category: Auction category (e.g., A04=Hourly)
            classification_sequence_position: Integer for classification
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A25",  # Fixed: Allocation result document
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=out_domain,
            business_type="B05",  # Fixed: Capacity allocated (including price)
            contract_market_agreement_type=contract_market_agreement_type,
            auction_category=auction_category,
            timeout=timeout,
            offset=offset,
        )

        # Add optional classification parameter
        param_name = "ClassificationSequence_AttributeInstanceComponent.Position"
        self.add_optional_param(param_name, classification_sequence_position)


class ExplicitAllocationsAuctionRevenueParams(MarketParams):
    """Parameters for 12.1.A Explicit Allocations - Auction Revenue.

    Data view:
    https://transparency.entsoe.eu/transmission-domain/r2/explicitAllocationsRevenue/show

    Fixed parameters:
    - documentType: A25 (Allocation result document)
    - businessType: B07 (Auction Revenue)
    """

    code = "12.1.A"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        in_domain: str,
        out_domain: str,
        contract_market_agreement_type: Literal[
            "A01", "A02", "A03", "A04", "A06", "A07", "A08"
        ] = "A01",
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize explicit allocations auction revenue parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of a Control Area, Bidding Zone or
                Bidding Zone Aggregation
            out_domain: EIC code of a Control Area, Bidding Zone or
                Bidding Zone Aggregation
            contract_market_agreement_type: A01=Daily; A02=Weekly;
                A03=Monthly; A04=Yearly; A06=Long Term; A07=Intraday;
                A08=Quarterly
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A25",  # Fixed: Allocation result document
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=out_domain,
            business_type="B07",  # Fixed: Auction Revenue
            contract_market_agreement_type=contract_market_agreement_type,
            timeout=timeout,
            offset=offset,
        )


class TransferCapacitiesThirdCountriesExplicitParams(MarketParams):
    """Parameters for 12.1.H Transfer Capacities Allocated with Third Countries.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/transCapAllocThirdCountries/show

    Fixed parameters:
    - documentType: A94 (Non EU allocations)
    - auction_Type: A02 (Explicit)
    """

    code = "12.1.H"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        in_domain: str,
        out_domain: str,
        contract_market_agreement_type: Literal[
            "A01", "A02", "A03", "A04", "A06", "A07", "A08"
        ] = "A07",
        auction_category: Optional[str] = None,
        classification_sequence_position: Optional[int] = None,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize transfer capacities allocated with third countries parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of a Control Area, Bidding Zone,
                Bidding Zone Aggregation
            out_domain: EIC code of a Control Area, Bidding Zone,
                Bidding Zone Aggregation
            contract_market_agreement_type: A01=Daily; A02=Weekly;
                A03=Monthly; A04=Yearly; A06=Long Term; A07=Intraday;
                A08=Quarterly
            auction_category: Auction category (e.g., A04=Hourly)
            classification_sequence_position: Integer for classification
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A94",  # Fixed: Non EU allocations
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=out_domain,
            contract_market_agreement_type=contract_market_agreement_type,
            auction_type="A02",  # Fixed: Explicit
            auction_category=auction_category,
            timeout=timeout,
            offset=offset,
        )

        # Add optional classification parameter
        param_name = "classificationSequence_AttributeInstanceComponent.Position"
        self.add_optional_param(param_name, classification_sequence_position)


class TransferCapacitiesThirdCountriesImplicitParams(MarketParams):
    """Parameters for 12.1.H Transfer Capacities Allocated with Third Countries.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/transCapAllocThirdCountries/show

    Fixed parameters:
    - documentType: A94 (Non EU allocations)
    - auction_Type: A01 (Implicit)
    """

    code = "12.1.H"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        in_domain: str,
        out_domain: str,
        contract_market_agreement_type: Literal["A01", "A07"] = "A01",
        classification_sequence_position: Optional[int] = None,
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize transfer capacities allocated with third countries parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of a Control Area, Bidding Zone or
                Bidding Zone Aggregation
            out_domain: EIC code of a Control Area, Bidding Zone or
                Bidding Zone Aggregation
            contract_market_agreement_type: A01=Daily; A07=Intraday
            classification_sequence_position: Integer for classification
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A94",  # Fixed: Non EU allocations
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=out_domain,
            contract_market_agreement_type=contract_market_agreement_type,
            auction_type="A01",  # Fixed: Implicit
            timeout=timeout,
            offset=offset,
        )

        # Add optional classification parameter
        param_name = "classificationSequence_AttributeInstanceComponent.Position"
        self.add_optional_param(param_name, classification_sequence_position)


class ImplicitAuctionNetPositionsParams(MarketParams):
    """Parameters for 12.1.E Implicit Auction — Net Positions.

    Fixed parameters:
    - documentType: A25 (Allocation results)
    - businessType: B09 (Net position)
    """

    code = "12.1.E"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        in_domain: str,
        out_domain: str,
        contract_market_agreement_type: Literal["A01", "A05", "A07"] = "A07",
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize implicit auction net positions parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of a Bidding Zone or Control Area
            out_domain: EIC code of a Bidding Zone or Control Area
                (must be same as in_domain)
            contract_market_agreement_type: A01=Daily; A05=Total; A07=Intraday
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A25",  # Fixed: Allocation results
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=out_domain,
            business_type="B09",  # Fixed: Net position
            contract_market_agreement_type=contract_market_agreement_type,
            timeout=timeout,
            offset=offset,
        )


class FlowBasedAllocationsLegacyParams(MarketParams):
    """Parameters for 11.1.B Flow Based Allocations (legacy).

    Data view:
    https://transparency.entsoe.eu/transmission/r2/flowBasedAllocationsDayAhead/show

    Fixed parameters:
    - documentType: A94 (Flow-based allocations)
    - auction_Type: A01 (Implicit)

    Note: This is the legacy version of Flow Based Allocations.
    """

    code = "11.1.B"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        in_domain: str,
        out_domain: str,
        # Only Day ahead for Flow Based
        contract_market_agreement_type: Literal["A01"] = "A01",
        # Additional common parameters
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """
        Initialize flow based allocations (legacy) parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of Control Area, Bidding Zone or Aggregation
            out_domain: EIC code of Control Area, Bidding Zone or Aggregation
            contract_market_agreement_type: A01=Day ahead (Flow Based only)
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A94",  # Fixed: Flow-based allocations
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=out_domain,
            contract_market_agreement_type=contract_market_agreement_type,
            auction_type="A01",  # Fixed: Implicit
            timeout=timeout,
            offset=offset,
        )

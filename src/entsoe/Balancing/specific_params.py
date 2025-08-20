"""Specific parameter classes for ENTSO-E Balancing endpoints.

This module contains specialized parameter classes for different Balancing data
endpoints, each inheriting from BalancingParams and providing preset values for
fixed parameters.
"""

from typing import Optional

from ..Base.Balancing import Balancing


class CrossBorderBalancing(Balancing):
    """Parameters for 17.1.J Cross Border Balancing.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/crossBorderBalancing/show

    Fixed parameters:
    - documentType: A88 (Cross border balancing)

    Notes:
    - Cross-border balancing activities between different market areas
    - Requires acquiring_domain and connecting_domain for cross-border queries
    """

    code = "17.1.J"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        acquiring_domain: str,
        connecting_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize cross border balancing parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            acquiring_domain: EIC code of Market Balancing Area (acquiring area)
            connecting_domain: EIC code of Market Balancing Area (connecting area)
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A88",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            acquiring_domain=acquiring_domain,
            connecting_domain=connecting_domain,
            timeout=timeout,
            offset=offset,
        )


class AcceptedAggregatedOffers(Balancing):
    """Parameters for 17.1.D Accepted Aggregated Offers.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/acceptedAggregatedOffers/show

    Fixed parameters:
    - documentType: A82 (Accepted offers)

    Optional parameters:
    - businessType: A95=Frequency containment reserve, A96=Automatic frequency
                   restoration reserve, A97=Manual frequency restoration reserve,
                   A98=Replacement reserve
    """

    code = "17.1.D"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Optional balancing-specific parameters
        business_type: Optional[str] = None,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize accepted aggregated offers parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            business_type: A95=FCR, A96=aFRR, A97=mFRR, A98=RR
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A82",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            business_type=business_type,
            timeout=timeout,
            offset=offset,
        )


class ActivatedBalancingEnergy(Balancing):
    """Parameters for 17.1.E Activated Balancing Energy.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/activationAndActivatedBalancingReserves/show

    Fixed parameters:
    - documentType: A83 (Activated balancing quantities)

    Optional parameters:
    - businessType: A95=Frequency containment reserve, A96=Automatic frequency
                   restoration reserve, A97=Manual frequency restoration reserve,
                   A98=Replacement reserve
    """

    code = "17.1.E"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Optional balancing-specific parameters
        business_type: Optional[str] = None,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize activated balancing energy parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            business_type: A95=FCR, A96=aFRR, A97=mFRR, A98=RR
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A83",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            business_type=business_type,
            timeout=timeout,
            offset=offset,
        )


class PricesOfActivatedBalancingEnergy(Balancing):
    """Parameters for 17.1.F Prices of Activated Balancing Energy.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/activationAndActivatedBalancingReserves/show

    Fixed parameters:
    - documentType: A84 (Activated balancing prices)

    Required parameters:
    - processType: A16=Realised, A60=Scheduled activation mFRR,
                  A61=Direct activation mFRR, A68=Local Selection aFRR

    Optional parameters:
    - businessType: A95=FCR, A96=aFRR, A97=mFRR, A98=RR
    """

    code = "17.1.F"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        process_type: str,
        # Optional balancing-specific parameters
        business_type: Optional[str] = None,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize prices of activated balancing energy parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            process_type: A16=Realised, A60=Scheduled activation mFRR,
                         A61=Direct activation mFRR, A68=Local Selection aFRR
            business_type: A95=FCR, A96=aFRR, A97=mFRR, A98=RR
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A84",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            process_type=process_type,
            business_type=business_type,
            timeout=timeout,
            offset=offset,
        )


class VolumesAndPricesOfContractedReserves(Balancing):
    """Parameters for 17.1.B&C Volumes and Prices of Contracted Reserves.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/contractedReserves/show

    Fixed parameters:
    - documentType: A81 (Contracted reserves)
    - businessType: B95 (Procured capacity)

    Required parameters:
    - processType: A51=Automatic frequency restoration reserve,
                  A52=Frequency containment reserve, A47=Manual frequency
                  restoration reserve, A46=Replacement reserve
    """

    code = "17.1.B_C"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        process_type: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize volumes and prices of contracted reserves parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            process_type: A51=aFRR, A52=FCR, A47=mFRR, A46=RR
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A81",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            business_type="B95",
            process_type=process_type,
            timeout=timeout,
            offset=offset,
        )


class ImbalancePrices(Balancing):
    """Parameters for 17.1.G Imbalance Prices.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/imbalancePricing/show

    Fixed parameters:
    - documentType: A85 (Imbalance prices)

    Notes:
    - Returns imbalance prices for the specified bidding zone
    - Used for settlement and pricing of imbalances
    """

    code = "17.1.G"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize imbalance prices parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A85",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            timeout=timeout,
            offset=offset,
        )


class TotalImbalanceVolumes(Balancing):
    """Parameters for 17.1.H Total Imbalance Volumes.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/imbalanceVolume/show

    Fixed parameters:
    - documentType: A86 (Imbalance volume)

    Optional parameters:
    - businessType: A19=Balance Energy Deviation (default when not specified)
    """

    code = "17.1.H"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Optional balancing-specific parameters
        business_type: Optional[str] = None,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize total imbalance volumes parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            business_type: A19=Balance Energy Deviation (default)
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A86",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            business_type=business_type,
            timeout=timeout,
            offset=offset,
        )


class FinancialExpensesAndIncomeForBalancing(Balancing):
    """Parameters for 17.1.I Financial Expenses and Income for Balancing.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/financialExpensesAndIncomeForBalancing/show

    Fixed parameters:
    - documentType: A87 (Financial situation)

    Notes:
    - Returns financial data related to balancing activities
    - Shows expenses and income from balancing operations
    """

    code = "17.1.I"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize financial expenses and income for balancing parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A87",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            timeout=timeout,
            offset=offset,
        )


class BalancingEnergyBids(Balancing):
    """Parameters for 12.3.B&C Balancing Energy Bids.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/balancingEnergyBids/show

    Fixed parameters:
    - documentType: A37 (Reserve bid document)
    - businessType: B74 (Offer)

    Required parameters:
    - processType: A46=Replacement reserve, A47=Manual frequency restoration reserve,
                  A51=Automatic frequency restoration reserve
    """

    code = "12.3.B_C"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        process_type: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize balancing energy bids parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            process_type: A46=RR, A47=mFRR, A51=aFRR
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A37",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            business_type="B74",
            process_type=process_type,
            timeout=timeout,
            offset=offset,
        )


class AggregatedBalancingEnergyBids(Balancing):
    """Parameters for 12.3.E Aggregated Balancing Energy Bids (GL EB).

    Data view:
    https://transparency.entsoe.eu/balancing/r2/aggregatedBalancingEnergyBids/show

    Fixed parameters:
    - documentType: A24 (Bid document)

    Required parameters:
    - processType: A51=aFRR, A46=RR, A47=mFRR, A60=Scheduled activation mFRR,
                  A61=Direct activation mFRR, A67=Central Selection aFRR,
                  A68=Local Selection aFRR
    """

    code = "12.3.E"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        process_type: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize aggregated balancing energy bids parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            process_type: A51=aFRR, A46=RR, A47=mFRR, A60=Scheduled mFRR,
                         A61=Direct mFRR, A67=Central aFRR, A68=Local aFRR
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A24",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            process_type=process_type,
            timeout=timeout,
            offset=offset,
        )


class ProcuredBalancingCapacity(Balancing):
    """Parameters for 12.3.F Procured Balancing Capacity (GL EB).

    Data view:
    https://transparency.entsoe.eu/balancing/r2/procuredBalancingCapacity/show

    Fixed parameters:
    - documentType: A15 (Acquiring system operator reserve schedule)

    Required parameters:
    - processType: A46=Replacement reserve, A47=Manual frequency restoration reserve,
                  A51=Automatic frequency restoration reserve,
                  A52=Frequency containment reserve
    """

    code = "12.3.F"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        process_type: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize procured balancing capacity parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            process_type: A46=RR, A47=mFRR, A51=aFRR, A52=FCR
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A15",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            process_type=process_type,
            timeout=timeout,
            offset=offset,
        )


class AllocationAndUseOfCrossZonalBalancingCapacity(Balancing):
    """Parameters for 12.3.H&I Allocation and Use of Cross-zonal Balancing Capacity.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/allocationAndUseOfCrossZonalBalancingCapacity/show

    Fixed parameters:
    - documentType: A38 (Reserve allocation result document)

    Required parameters:
    - processType: A46=Replacement reserve, A47=Manual frequency restoration reserve,
                  A51=Automatic frequency restoration reserve,
                  A52=Frequency containment reserve
    """

    code = "12.3.H_I"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        process_type: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize allocation and use of cross-zonal balancing capacity parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            process_type: A46=RR, A47=mFRR, A51=aFRR, A52=FCR
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A38",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            process_type=process_type,
            timeout=timeout,
            offset=offset,
        )


class CurrentBalancingState(Balancing):
    """Parameters for 12.3.A Current Balancing State (GL EB).

    Data view:
    https://transparency.entsoe.eu/balancing/r2/currentBalancingState/show

    Fixed parameters:
    - documentType: A86 (Imbalance volume)
    - businessType: B33 (Area Control Error)

    Notes:
    - Returns current balancing state information
    - Shows real-time area control error data
    """

    code = "12.3.A"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize current balancing state parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A86",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            business_type="B33",
            timeout=timeout,
            offset=offset,
        )


class FCRTotalCapacity(Balancing):
    """Parameters for 187.2 FCR Total Capacity (SO GL).

    Data view:
    https://transparency.entsoe.eu/balancing/r2/fcrTotalCapacity/show

    Fixed parameters:
    - documentType: A26 (Capacity document)
    - businessType: A25 (General Capacity Information)

    Notes:
    - Returns total FCR (Frequency Containment Reserve) capacity data
    - Used for capacity planning and reserve management
    """

    code = "187.2"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize FCR total capacity parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A26",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            business_type="A25",
            timeout=timeout,
            offset=offset,
        )


class SharesOfFCRCapacity(Balancing):
    """Parameters for 187.2 Shares of FCR Capacity (SO GL).

    Data view:
    https://transparency.entsoe.eu/balancing/r2/sharesOfFCRCapacity/show

    Fixed parameters:
    - documentType: A26 (Capacity document)
    - businessType: C23 (Share of reserve capacity)

    Notes:
    - Returns shares of FCR capacity between different areas
    - Shows distribution of frequency containment reserves
    """

    code = "187.2_Shares"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize shares of FCR capacity parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A26",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            business_type="C23",
            timeout=timeout,
            offset=offset,
        )


class SharingOfFCRBetweenSAs(Balancing):
    """Parameters for 190.2 Sharing of FCR between SAs (SO GL).

    Data view:
    https://transparency.entsoe.eu/balancing/r2/sharingOfFCRBetweenSAs/show

    Fixed parameters:
    - documentType: A26 (Capacity document)
    - processType: A52 (Frequency containment reserve)
    - businessType: C22 (Shared Balancing Reserve Capacity)

    Notes:
    - Shows sharing arrangements of FCR between Scheduling Areas
    - Used for cross-border reserve sharing coordination
    """

    code = "190.2"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize sharing of FCR between SAs parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A26",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            process_type="A52",
            business_type="C22",
            timeout=timeout,
            offset=offset,
        )


class FRRAndRRCapacityOutlook(Balancing):
    """Parameters for 188.3 & 189.2 FRR & RR Capacity Outlook (SO GL).

    Data view:
    https://transparency.entsoe.eu/balancing/r2/frrAndRRCapacityOutlook/show

    Fixed parameters:
    - documentType: A26 (Capacity document)
    - businessType: C76 (Forecasted capacity)

    Required parameters:
    - processType: A46=Replacement Reserve, A56=Frequency Restoration Reserve
    """

    code = "188.3_189.2"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        process_type: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize FRR and RR capacity outlook parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            process_type: A46=Replacement Reserve, A56=Frequency Restoration Reserve
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A26",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            process_type=process_type,
            business_type="C76",
            timeout=timeout,
            offset=offset,
        )


class FRRAndRRActualCapacity(Balancing):
    """Parameters for 188.4 & 189.3 FRR and RR Actual Capacity (SO GL).

    Data view:
    https://transparency.entsoe.eu/balancing/r2/frrAndRRActualCapacity/show

    Fixed parameters:
    - documentType: A26 (Capacity document)

    Required parameters:
    - processType: A46=Replacement reserve, A56=Frequency restoration reserve
    - businessType: C77=Min, C78=Avg, C79=Max
    """

    code = "188.4_189.3"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        process_type: str,
        business_type: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize FRR and RR actual capacity parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            process_type: A46=Replacement reserve, A56=Frequency restoration reserve
            business_type: C77=Min, C78=Avg, C79=Max
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A26",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            process_type=process_type,
            business_type=business_type,
            timeout=timeout,
            offset=offset,
        )


class OutlookOfReserveCapacitiesOnRR(Balancing):
    """Parameters for 189.2 Outlook of Reserve Capacities on RR (SO GL).

    Data view:
    https://transparency.entsoe.eu/balancing/r2/outlookOfReserveCapacitiesOnRR/show

    Fixed parameters:
    - documentType: A26 (Capacity document)
    - processType: A46 (Replacement reserve)
    - businessType: C76 (Forecasted capacity)

    Notes:
    - Provides outlook/forecast of replacement reserve capacities
    - Used for medium-term capacity planning
    """

    code = "189.2"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize outlook of reserve capacities on RR parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A26",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            process_type="A46",
            business_type="C76",
            timeout=timeout,
            offset=offset,
        )


class RRActualCapacity(Balancing):
    """Parameters for 189.3 RR Actual Capacity (SO GL).

    Data view:
    https://transparency.entsoe.eu/balancing/r2/rrActualCapacity/show

    Fixed parameters:
    - documentType: A26 (Capacity document)
    - processType: A46 (Replacement reserve)
    - businessType: C77 (Min)

    Notes:
    - Returns actual replacement reserve capacity data
    - Shows minimum actual capacity available
    """

    code = "189.3"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize RR actual capacity parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A26",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            process_type="A46",
            business_type="C77",
            timeout=timeout,
            offset=offset,
        )


class SharingOfRRAndFRR(Balancing):
    """Parameters for 190.1 Sharing of RR and FRR (SO GL).

    Data view:
    https://transparency.entsoe.eu/balancing/r2/sharingOfRRAndFRR/show

    Fixed parameters:
    - documentType: A26 (Capacity document)
    - processType: A56 (Frequency restoration reserve)

    Notes:
    - Shows sharing arrangements for RR and FRR between areas
    - Used for cross-border reserve sharing coordination
    """

    code = "190.1"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize sharing of RR and FRR parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A26",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            process_type="A56",
            timeout=timeout,
            offset=offset,
        )


class ExchangedReserveCapacity(Balancing):
    """Parameters for 190.3 Exchanged Reserve Capacity (SO GL).

    Data view:
    https://transparency.entsoe.eu/balancing/r2/exchangedReserveCapacity/show

    Fixed parameters:
    - documentType: A26 (Capacity document)
    - processType: A46 (Replacement reserve)

    Notes:
    - Shows exchanged reserve capacity between areas
    - Used for cross-border capacity exchange tracking
    """

    code = "190.3"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize exchanged reserve capacity parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A26",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            process_type="A46",
            timeout=timeout,
            offset=offset,
        )


class CrossBorderMarginalPricesForAFRR(Balancing):
    """Parameters for IF aFRR 3.16 Cross Border Marginal Prices (CBMPs) for
    aFRR Central Selection (CS).

    Data view:
    https://transparency.entsoe.eu/balancing/r2/crossBorderMarginalPricesForAFRR/show

    Fixed parameters:
    - documentType: A84 (Activated balancing prices)
    - processType: A67 (Central Selection aFRR)
    - businessType: A96 (Automatic frequency restoration reserve)

    Notes:
    - Specific to aFRR Central Selection marginal prices
    - Cross-border pricing information for automatic frequency restoration
    """

    code = "IF_aFRR_3.16"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize cross border marginal prices for aFRR parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A84",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            process_type="A67",
            business_type="A96",
            timeout=timeout,
            offset=offset,
        )


class NettedAndExchangedVolumes(Balancing):
    """Parameters for IFs 3.10, 3.16 & 3.17 Netted and Exchanged Volumes.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/nettedAndExchangedVolumes/show

    Fixed parameters:
    - documentType: B17 (Aggregated netted external TSO schedule document)

    Required parameters:
    - processType: A60=mFRR with Scheduled Activation, A61=mFRR with Direct Activation,
                  A51=Automatic Frequency Restoration Reserve, A63=Imbalance Netting
    """

    code = "IF_3.10_3.16_3.17"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        process_type: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize netted and exchanged volumes parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            process_type: A60=mFRR Scheduled, A61=mFRR Direct, A51=aFRR,
                         A63=Imbalance Netting
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="B17",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            process_type=process_type,
            timeout=timeout,
            offset=offset,
        )


class NettedAndExchangedVolumesPerBorder(Balancing):
    """Parameters for IFs 3.10, 3.16 & 3.17 Netted and Exchanged Volumes per Border.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/nettedAndExchangedVolumesPerBorder/show

    Fixed parameters:
    - documentType: A30 (Cross border schedule)

    Required parameters:
    - processType: A60=mFRR with Scheduled Activation, A61=mFRR with Direct Activation,
                  A51=Automatic Frequency Restoration Reserve, A63=Imbalance Netting
    """

    code = "IF_3.10_3.16_3.17_Border"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        acquiring_domain: str,
        connecting_domain: str,
        process_type: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize netted and exchanged volumes per border parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            acquiring_domain: EIC code of Market Balancing Area (acquiring area)
            connecting_domain: EIC code of Market Balancing Area (connecting area)
            process_type: A60=mFRR Scheduled, A61=mFRR Direct, A51=aFRR,
                         A63=Imbalance Netting
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A30",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            acquiring_domain=acquiring_domain,
            connecting_domain=connecting_domain,
            process_type=process_type,
            timeout=timeout,
            offset=offset,
        )


class ElasticDemands(Balancing):
    """Parameters for IFs aFRR 3.4 & mFRR 3.4 Elastic Demands.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/elasticDemands/show

    Fixed parameters:
    - documentType: A37 (Reserve bid document)
    - businessType: B75 (Need)

    Required parameters:
    - processType: A51=Automatic Frequency Restoration Reserve,
                  A47=Manual Frequency Restoration Reserve
    """

    code = "IF_aFRR_mFRR_3.4"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        process_type: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize elastic demands parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            process_type: A51=aFRR, A47=mFRR
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A37",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            business_type="B75",
            process_type=process_type,
            timeout=timeout,
            offset=offset,
        )


class ChangesToBidAvailability(Balancing):
    """Parameters for IFs mFRR 9.9, aFRR 9.6&9.8 Changes to Bid Availability.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/changesToBidAvailability/show

    Fixed parameters:
    - documentType: B45 (Bid Availability Document)
    - processType: A47 (Manual frequency restoration reserve)

    Optional parameters:
    - businessType: C40=Conditional bid, C41=Thermal limit, C42=Frequency limit,
                   C43=Voltage limit, C44=Current limit,
                   C45=Short-circuit current limits,
                   C46=Dynamic stability limit
    """

    code = "IF_mFRR_aFRR_9.6_9.8_9.9"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Optional balancing-specific parameters
        business_type: Optional[str] = None,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize changes to bid availability parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            business_type: C40=Conditional bid, C41=Thermal limit, C42=Frequency limit,
                          C43=Voltage limit, C44=Current limit, C45=Short-circuit limit,
                          C46=Dynamic stability limit
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="B45",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            process_type="A47",
            business_type=business_type,
            timeout=timeout,
            offset=offset,
        )


class BalancingBorderCapacityLimitations(Balancing):
    """Parameters for IFs 4.3 & 4.4 Balancing Border Capacity Limitations.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/balancingBorderCapacityLimitations/show

    Fixed parameters:
    - documentType: A31 (Agreed capacity)

    Required parameters:
    - processType: A51=Automatic Frequency Restoration Reserve,
                  A63=Imbalance Netting, A47=Manual frequency restoration reserve
    """

    code = "IF_4.3_4.4"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        acquiring_domain: str,
        connecting_domain: str,
        process_type: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize balancing border capacity limitations parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            acquiring_domain: EIC code of Market Balancing Area (acquiring area)
            connecting_domain: EIC code of Market Balancing Area (connecting area)
            process_type: A51=aFRR, A63=Imbalance Netting, A47=mFRR
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A31",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            acquiring_domain=acquiring_domain,
            connecting_domain=connecting_domain,
            process_type=process_type,
            timeout=timeout,
            offset=offset,
        )


class PermanentAllocationLimitationsToHVDCLines(Balancing):
    """Parameters for IFs 4.5 Permanent Allocation Limitations to Cross-border
    Capacity on HVDC Lines.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/permanentAllocationLimitationsToHVDCLines/show

    Fixed parameters:
    - documentType: A99 (HVDC Link constraints)

    Required parameters:
    - processType: A51=Automatic Frequency Restoration Reserve,
                  A63=Imbalance Netting, A47=Manual frequency restoration reserve
    """

    code = "IF_4.5"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        acquiring_domain: str,
        connecting_domain: str,
        process_type: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize permanent allocation limitations to HVDC lines parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            acquiring_domain: EIC code of Market Balancing Area (acquiring area)
            connecting_domain: EIC code of Market Balancing Area (connecting area)
            process_type: A51=aFRR, A63=Imbalance Netting, A47=mFRR
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A99",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            acquiring_domain=acquiring_domain,
            connecting_domain=connecting_domain,
            process_type=process_type,
            timeout=timeout,
            offset=offset,
        )


class ResultsOfCriteriaApplicationProcess(Balancing):
    """Parameters for 185.4 Results of the Criteria Application Process -
    Measurements (SO GL).

    Data view:
    https://transparency.entsoe.eu/balancing/r2/resultsOfCriteriaApplicationProcess/show

    Fixed parameters:
    - documentType: A45 (Measurement Value Document)

    Required parameters:
    - processType: A64=Criteria application for instantaneous frequency (For SNA),
                  A65=Criteria application for frequency restoration (for LFC Block)
    """

    code = "185.4"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        process_type: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize results of criteria application process parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            process_type: A64=Instantaneous frequency criteria,
                         A65=Frequency restoration criteria
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A45",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            process_type=process_type,
            timeout=timeout,
            offset=offset,
        )


class BalancingEnergyBidsArchives(Balancing):
    """Parameters for 12.3.B&C Balancing Energy Bids Archives.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/balancingEnergyBidsArchives/show

    Fixed parameters:
    - documentType: A37 (Reserve bid document)
    - businessType: B74 (Offer)

    Required parameters:
    - processType: A46=Replacement reserve, A47=Manual frequency restoration reserve,
                  A51=Automatic frequency restoration reserve

    Notes:
    - This is the archived version of balancing energy bids
    - Contains historical bid data for analysis and reporting
    """

    code = "12.3.B_C_Archives"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        process_type: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize balancing energy bids archives parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            process_type: A46=RR, A47=mFRR, A51=aFRR
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A37",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            business_type="B74",
            process_type=process_type,
            timeout=timeout,
            offset=offset,
        )


class FRRActualCapacityLegacy(Balancing):
    """Parameters for 188.4 FRR Actual Capacity (SO GL) - Legacy.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/frrActualCapacityLegacy/show

    Fixed parameters:
    - documentType: A26 (Capacity document)
    - processType: A46=Replacement reserve, A56=Frequency restoration reserve
    - businessType: C77=Min, C78=Avg, C79=Max

    Notes:
    - This is the legacy version of FRR actual capacity endpoint
    - Maintained for backward compatibility
    """

    code = "188.4_Legacy"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        process_type: str,
        business_type: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize FRR actual capacity legacy parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            process_type: A46=Replacement reserve, A56=Frequency restoration reserve
            business_type: C77=Min, C78=Avg, C79=Max
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A26",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            process_type=process_type,
            business_type=business_type,
            timeout=timeout,
            offset=offset,
        )


class RRActualCapacityLegacy(Balancing):
    """Parameters for 189.3 RR Actual Capacity (SO GL) Legacy.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/rrActualCapacityLegacy/show

    Fixed parameters:
    - documentType: A26 (Capacity document)
    - processType: A46 (Replacement reserve)
    - businessType: C24 (Actual reserve capacity)

    Notes:
    - This is the legacy version using C24 instead of C77 business type
    - Maintained for backward compatibility with older implementations
    """

    code = "189.3_Legacy"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize RR actual capacity legacy parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A26",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            process_type="A46",
            business_type="C24",
            timeout=timeout,
            offset=offset,
        )


class SharingOfRRAndFRRLegacy(Balancing):
    """Parameters for 190.1 Sharing of RR and FRR (SO GL) Legacy.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/sharingOfRRAndFRRLegacy/show

    Fixed parameters:
    - documentType: A26 (Capacity document)
    - processType: A47 (Manual frequency restoration reserve)

    Notes:
    - This is the legacy version using A47 instead of A56 process type
    - Maintained for backward compatibility with older implementations
    """

    code = "190.1_Legacy"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize sharing of RR and FRR legacy parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A26",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            process_type="A47",
            timeout=timeout,
            offset=offset,
        )


class SharesOfFCRCapacityLegacy(Balancing):
    """Parameters for 187.2 Shares of FCR Capacity - Share of Capacity (SO GL) Legacy.

    Data view:
    https://transparency.entsoe.eu/balancing/r2/sharesOfFCRCapacityLegacy/show

    Fixed parameters:
    - documentType: A26 (Capacity document)
    - businessType: C23 (Share of reserve capacity)
    - processType: A52 (Frequency containment reserve)

    Notes:
    - This is the legacy version with explicit A52 process type
    - Maintained for backward compatibility with older implementations
    """

    code = "187.2_Legacy"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize shares of FCR capacity legacy parameters.

        Args:
            security_token: API security token
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            bidding_zone_domain: EIC code of Bidding Zone or Market Balancing Area
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A26",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            process_type="A52",
            business_type="C23",
            timeout=timeout,
            offset=offset,
        )

"""Specific parameter classes for ENTSO-E Transmission endpoints.

This module contains specialized parameter classes for different Transmission data
endpoints, each inheriting from TransmissionParams and providing preset values for
fixed parameters.
"""

from typing import Optional

from ..Base.Transmission import Transmission


class CrossBorderPhysicalFlows(Transmission):
    """Parameters for 12.1.G Cross-Border Physical Flows.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/physicalFlows/show

    Fixed parameters:

    - documentType: A11 (Flow document)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one MTU period
    """

    code = "12.1.G"

    def __init__(
        self,
        period_start: int,
        period_end: int,
        out_domain: str,
        in_domain: str,
    ):
        """
        Initialize cross-border physical flows parameters.

        Args:
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            out_domain: EIC code of output domain/bidding zone
            in_domain: EIC code of input domain/bidding zone"""
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A11",
            period_start=period_start,
            period_end=period_end,
            out_domain=out_domain,
            in_domain=in_domain,
        )

        self.validate_eic_equality(in_domain, out_domain, must_be_equal=False)


class CommercialSchedules(Transmission):
    """Parameters for 12.1.F Commercial Schedules.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/dayAheadCommercialSchedules/show

    Fixed parameters:

    - documentType: A09 (Finalised schedule)
    - contract_MarketAgreement.Type: A01 (Daily)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one MTU period
    """

    code = "12.1.F"

    def __init__(
        self,
        period_start: int,
        period_end: int,
        out_domain: str,
        in_domain: str,
    ):
        """
        Initialize commercial schedules parameters.

        Args:
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            out_domain: EIC code of output domain/bidding zone
            in_domain: EIC code of input domain/bidding zone"""
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A09",
            period_start=period_start,
            period_end=period_end,
            out_domain=out_domain,
            in_domain=in_domain,
        )

        self.validate_eic_equality(in_domain, out_domain, must_be_equal=False)

        # Add specific parameters
        self.add_optional_param("contract_MarketAgreement.Type", "A01")


class ForecastedTransferCapacities(Transmission):
    """Parameters for 11.1.A Forecasted Transfer Capacities.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/forecastedCapacity/show

    Fixed parameters:

    - documentType: A61 (Estimated Net Transfer Capacity)
    - contract_MarketAgreement.Type: A01 (Daily)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one MTU period
    """

    code = "11.1.A"

    def __init__(
        self,
        period_start: int,
        period_end: int,
        out_domain: str,
        in_domain: str,
    ):
        """
        Initialize forecasted transfer capacities parameters.

        Args:
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            out_domain: EIC code of output domain/bidding zone
            in_domain: EIC code of input domain/bidding zone"""
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A61",
            period_start=period_start,
            period_end=period_end,
            out_domain=out_domain,
            in_domain=in_domain,
        )

        self.validate_eic_equality(in_domain, out_domain, must_be_equal=False)

        # Add specific parameters
        self.add_optional_param("contract_MarketAgreement.Type", "A01")


class CommercialSchedulesNetPositions(Transmission):
    """Parameters for 12.1.F Commercial Schedules - Net Positions.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/dayAheadCommercialSchedules/show

    Fixed parameters:

    - documentType: A09 (Finalised schedule)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one MTU period
    """

    code = "12.1.F"

    def __init__(
        self,
        period_start: int,
        period_end: int,
        in_domain: str,
        contract_market_agreement_type: Optional[str] = None,
    ):
        """
        Initialize commercial schedules net positions parameters.

        Args:
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of Control Area, Bidding Zone or Country
                (in_domain and out_domain must be the same)
            contract_market_agreement_type: A01=Day Ahead; A05=Total (optional)
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A09",
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=in_domain,  # Same as in_domain for net positions
        )

        # Add optional contract type
        if contract_market_agreement_type:
            self.add_optional_param(
                "contract_MarketAgreement.Type", contract_market_agreement_type
            )


class CrossBorderCapacityDCLinks(Transmission):
    """Parameters for 11.3 Cross Border Capacity of DC Links - Intraday Transfer Limits.

    Data view:
    https://transparency.entsoe.eu/transmission/r2/dcLinkCapacity/show

    Fixed parameters:

    - documentType: A93 (DC link capacity)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one MTU period
    """

    code = "11.3"

    def __init__(
        self,
        period_start: int,
        period_end: int,
        in_domain: str,
        out_domain: str,
    ):
        """
        Initialize DC link capacity parameters.

        Args:
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of Bidding Zone, Control Area or Country
            out_domain: EIC code of Bidding Zone, Control Area or Country
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A93",
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=out_domain,
        )

        self.validate_eic_equality(in_domain, out_domain, must_be_equal=False)


class RedispatchingCrossBorder(Transmission):
    """Parameters for 13.1.A Redispatching Cross Border.

    Data view:
    https://transparency.entsoe.eu/transmission-domain/r2/redispatching/show

    Fixed parameters:

    - documentType: A63 (Redispatch notice)
    - businessType: A46 (System Operator re-dispatching)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one day
    """

    code = "13.1.A"

    def __init__(
        self,
        period_start: int,
        period_end: int,
        in_domain: str,
        out_domain: str,
    ):
        """
        Initialize cross border redispatching parameters.

        Args:
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of Control Area
            out_domain: EIC code of Control Area
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A63",
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=out_domain,
            business_type="A46",  # Fixed: System Operator re-dispatching
        )

        self.validate_eic_equality(in_domain, out_domain, must_be_equal=False)


class RedispatchingInternal(Transmission):
    """Parameters for 13.1.A Redispatching Internal.

    Data view:
    https://transparency.entsoe.eu/transmission-domain/r2/redispatching/show

    Fixed parameters:

    - documentType: A63 (Redispatch notice)
    - businessType: A85 (Internal requirements)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one day
    """

    code = "13.1.A"

    def __init__(
        self,
        period_start: int,
        period_end: int,
        in_domain: str,
    ):
        """
        Initialize internal redispatching parameters.

        Args:
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of Control Area (in_domain and out_domain
                must be the same for internal)
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A63",
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=in_domain,  # Same as in_domain for internal
            business_type="A85",  # Fixed: Internal requirements
        )


class Countertrading(Transmission):
    """Parameters for 13.1.B Countertrading.

    Data view:
    https://transparency.entsoe.eu/transmission-domain/r2/countertrading/show

    Fixed parameters:

    - documentType: A91 (Counter trade notice)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one day
    """

    code = "13.1.B"

    def __init__(
        self,
        period_start: int,
        period_end: int,
        in_domain: str,
        out_domain: str,
    ):
        """
        Initialize countertrading parameters.

        Args:
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of Control Area or Bidding Zone
            out_domain: EIC code of Control Area or Bidding Zone
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A91",
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=out_domain,
        )

        self.validate_eic_equality(in_domain, out_domain, must_be_equal=False)


class CostsOfCongestionManagement(Transmission):
    """Parameters for 13.1.C Costs of Congestion Management.

    Data view:
    https://transparency.entsoe.eu/transmission-domain/r2/congestionManagementCosts/show

    Fixed parameters:

    - documentType: A92 (Congestion costs)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one year
    """

    code = "13.1.C"

    def __init__(
        self,
        period_start: int,
        period_end: int,
        in_domain: str,
    ):
        """
        Initialize congestion management costs parameters.

        Args:
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of Control Area (in_domain and out_domain
                must be the same)
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A92",
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=in_domain,  # Same as in_domain
        )


class ExpansionAndDismantlingProject(Transmission):
    """Parameters for 9.1 Expansion and Dismantling Project.

    Data view:
    https://transparency.entsoe.eu/transmission-domain/r2/networkExpansion/show

    Fixed parameters:

    - documentType: A90 (Interconnector network expansion)

    Request Limits:
    - One year range limit applies
    - Minimum time interval in query response is one year
    """

    code = "9.1"

    def __init__(
        self,
        period_start: int,
        period_end: int,
        in_domain: str,
        out_domain: str,
        business_type: Optional[str] = None,
        doc_status: Optional[str] = None,
    ):
        """
        Initialize expansion and dismantling project parameters.

        Args:
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: EIC code of Bidding Zone or Control Area
            out_domain: EIC code of Bidding Zone or Control Area
            business_type: B01=interconnector network evolution;
                B02=interconnector network dismantling (optional)
            doc_status: A01=Intermediate; A02=Final; A05=Active; A09=Cancelled;
                A13=Withdrawn; X01=Estimated (optional)
        """
        # Initialize with preset and user parameters
        super().__init__(
            document_type="A90",
            period_start=period_start,
            period_end=period_end,
            in_domain=in_domain,
            out_domain=out_domain,
            business_type=business_type,
        )

        self.validate_eic_equality(in_domain, out_domain, must_be_equal=False)

        # Add optional doc status
        if doc_status:
            self.add_optional_param("DocStatus", doc_status)

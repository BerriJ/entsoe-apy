"""Specific parameter classes for ENTSO-E Outages endpoints.

This module contains specialized parameter classes for different Outages data
endpoints, each inheriting from Outages and providing preset values for
fixed parameters based on the ENTSO-E Transparency Platform API specification.
"""

from typing import Optional

from ..Base.Outages import Outages


class UnavailabilityOfProductionUnits(Outages):
    """Parameters for 15.1.C-D Unavailability of Production Units.

    Data view:
    https://transparency.entsoe.eu/outage-domain/r2/unavailabilityInTransmissionGrid/show

    Fixed parameters:
    - documentType: A77 (Production unit unavailability)

    Notes:
    - Returns production unit unavailability data
    - Can be filtered by business type (A53=Planned maintenance,
      A54=Forced unavailability)
    - Supports update-based queries with PeriodStartUpdate/PeriodEndUpdate
    """

    code = "15.1.C-D"

    def __init__(
        self,
        security_token: str,
        bidding_zone_domain: str,
        # Time period parameters (at least one set required)
        period_start: Optional[int] = None,
        period_end: Optional[int] = None,
        period_start_update: Optional[int] = None,
        period_end_update: Optional[int] = None,
        # Optional filtering parameters
        business_type: Optional[str] = None,
        doc_status: Optional[str] = None,
        registered_resource: Optional[str] = None,
        m_rid: Optional[str] = None,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize unavailability of production units parameters.

        Args:
            security_token: API security token
            bidding_zone_domain: EIC code of Control Area, Bidding Zone
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            period_start_update: Start of update period (YYYYMMDDHHMM format)
            period_end_update: End of update period (YYYYMMDDHHMM format)
            business_type: Business type (A53=Planned maintenance,
                         A54=Forced unavailability)
            doc_status: Document status (A05=Active, A09=Cancelled,
                       A13=Withdrawn)
            registered_resource: EIC Code of Production Unit
            m_rid: Message ID for specific outage versions
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        super().__init__(
            document_type="A77",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            period_start_update=period_start_update,
            period_end_update=period_end_update,
            business_type=business_type,
            doc_status=doc_status,
            registered_resource=registered_resource,
            m_rid=m_rid,
            timeout=timeout,
            offset=offset,
        )


class UnavailabilityOfGenerationUnits(Outages):
    """Parameters for 15.1.A&B Unavailability of Generation Units.

    Data view:
    https://transparency.entsoe.eu/outage-domain/r2/unavailabilityInTransmissionGrid/show

    Fixed parameters:
    - documentType: A80 (Generation unavailability)

    Notes:
    - Returns generation unit unavailability data
    - Can be filtered by business type (A53=Planned maintenance,
      A54=Forced unavailability)
    - Supports update-based queries with PeriodStartUpdate/PeriodEndUpdate
    """

    code = "15.1.A&B"

    def __init__(
        self,
        security_token: str,
        bidding_zone_domain: str,
        # Time period parameters (at least one set required)
        period_start: Optional[int] = None,
        period_end: Optional[int] = None,
        period_start_update: Optional[int] = None,
        period_end_update: Optional[int] = None,
        # Optional filtering parameters
        business_type: Optional[str] = None,
        doc_status: Optional[str] = None,
        registered_resource: Optional[str] = None,
        m_rid: Optional[str] = None,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize unavailability of generation units parameters.

        Args:
            security_token: API security token
            bidding_zone_domain: EIC code of Control Area, Bidding Zone
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            period_start_update: Start of update period (YYYYMMDDHHMM format)
            period_end_update: End of update period (YYYYMMDDHHMM format)
            business_type: Business type (A53=Planned maintenance,
                         A54=Forced unavailability)
            doc_status: Document status (A05=Active, A09=Cancelled,
                       A13=Withdrawn)
            registered_resource: EIC Code of Generation Unit
            m_rid: Message ID for specific outage versions
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        super().__init__(
            document_type="A80",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            period_start_update=period_start_update,
            period_end_update=period_end_update,
            business_type=business_type,
            doc_status=doc_status,
            registered_resource=registered_resource,
            m_rid=m_rid,
            timeout=timeout,
            offset=offset,
        )


class AggregatedUnavailabilityOfConsumptionUnits(Outages):
    """Parameters for 7.1.A-B Aggregated Unavailability of Consumption Units.

    Data view:
    https://transparency.entsoe.eu/outage-domain/r2/unavailabilityInTransmissionGrid/show

    Fixed parameters:
    - documentType: A76 (Load unavailability)

    Notes:
    - Returns aggregated unavailability data for consumption units
    - Can be filtered by business type (A53=Planned maintenance,
      A54=Forced unavailability)
    - Period parameters are optional if PeriodStartUpdate/PeriodEndUpdate
      are defined
    """

    code = "7.1.A-B"

    def __init__(
        self,
        security_token: str,
        bidding_zone_domain: str,
        # Time period parameters (at least one set required)
        period_start: Optional[int] = None,
        period_end: Optional[int] = None,
        period_start_update: Optional[int] = None,
        period_end_update: Optional[int] = None,
        # Optional filtering parameters
        business_type: Optional[str] = None,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize aggregated unavailability of consumption units parameters.

        Args:
            security_token: API security token
            bidding_zone_domain: EIC code of Control Area or Bidding Zone
            period_start: Start period (YYYYMMDDHHMM format, optional if
                         period_start_update defined)
            period_end: End period (YYYYMMDDHHMM format, optional if
                       period_end_update defined)
            period_start_update: Start of update period (YYYYMMDDHHMM format)
            period_end_update: End of update period (YYYYMMDDHHMM format)
            business_type: Business type (A53=Planned maintenance,
                         A54=Forced unavailability)
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        super().__init__(
            document_type="A76",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            period_start_update=period_start_update,
            period_end_update=period_end_update,
            business_type=business_type,
            timeout=timeout,
            offset=offset,
        )


class UnavailabilityOfTransmissionInfrastructure(Outages):
    """Parameters for 10.1.A&B Unavailability of Transmission Infrastructure.

    Data view:
    https://transparency.entsoe.eu/outage-domain/r2/unavailabilityInTransmissionGrid/show

    Fixed parameters:
    - documentType: A78 (Transmission unavailability)

    Notes:
    - Returns transmission infrastructure unavailability data
    - Uses Out_Domain and In_Domain instead of BiddingZone_Domain
    - Supports TimeIntervalUpdate as alternative to
      PeriodStartUpdate/PeriodEndUpdate
    - Can be filtered by business type (A53=Planned maintenance,
      A54=Forced unavailability)
    """

    code = "10.1.A&B"

    def __init__(
        self,
        security_token: str,
        out_domain: str,
        in_domain: str,
        # Time period parameters (at least one set required)
        period_start: Optional[int] = None,
        period_end: Optional[int] = None,
        period_start_update: Optional[int] = None,
        period_end_update: Optional[int] = None,
        time_interval_update: Optional[str] = None,
        # Optional filtering parameters
        business_type: Optional[str] = None,
        doc_status: Optional[str] = None,
        m_rid: Optional[str] = None,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize unavailability of transmission infrastructure parameters.

        Args:
            security_token: API security token
            out_domain: EIC code of Control Area or Bidding Zone (output domain)
            in_domain: EIC code of Control Area or Bidding Zone (input domain)
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            period_start_update: Start of update period (YYYYMMDDHHMM format)
            period_end_update: End of update period (YYYYMMDDHHMM format)
            time_interval_update: Can be used instead of PeriodStartUpdate
                                & PeriodEndUpdate
            business_type: Business type (A53=Planned maintenance,
                         A54=Forced unavailability)
            doc_status: Document status (A05=Active, A09=Cancelled,
                       A13=Withdrawn)
            m_rid: Message ID for specific outage versions
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        super().__init__(
            document_type="A78",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            period_start_update=period_start_update,
            period_end_update=period_end_update,
            time_interval_update=time_interval_update,
            business_type=business_type,
            doc_status=doc_status,
            m_rid=m_rid,
            timeout=timeout,
            offset=offset,
        )

        # Add domain parameters specific to this endpoint
        self.add_domain_params(out_domain=out_domain, in_domain=in_domain)


class UnavailabilityOfOffshoreGridInfrastructure(Outages):
    """Parameters for 10.1.C Unavailability of Offshore Grid Infrastructure.

    Data view:
    https://transparency.entsoe.eu/outage-domain/r2/unavailabilityInTransmissionGrid/show

    Fixed parameters:
    - documentType: A79 (Offshore grid infrastructure unavailability)

    Notes:
    - Returns offshore grid infrastructure unavailability data
    - Period parameters are optional if PeriodStartUpdate/PeriodEndUpdate
      are defined
    - No BusinessType parameter available for this endpoint
    """

    code = "10.1.C"

    def __init__(
        self,
        security_token: str,
        bidding_zone_domain: str,
        # Time period parameters (at least one set required)
        period_start: Optional[int] = None,
        period_end: Optional[int] = None,
        period_start_update: Optional[int] = None,
        period_end_update: Optional[int] = None,
        # Optional filtering parameters
        doc_status: Optional[str] = None,
        m_rid: Optional[str] = None,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize unavailability of offshore grid infrastructure parameters.

        Args:
            security_token: API security token
            bidding_zone_domain: EIC code of Control Area, Bidding Zone
            period_start: Start period (YYYYMMDDHHMM format, optional if
                         period_start_update defined)
            period_end: End period (YYYYMMDDHHMM format, optional if
                       period_end_update defined)
            period_start_update: Start of update period (YYYYMMDDHHMM format,
                               mandatory if period_start/end not defined)
            period_end_update: End of update period (YYYYMMDDHHMM format,
                             mandatory if period_start/end not defined)
            doc_status: Document status (A05=Active, A09=Cancelled,
                       A13=Withdrawn)
            m_rid: Message ID for specific outage versions
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        super().__init__(
            document_type="A79",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            period_start_update=period_start_update,
            period_end_update=period_end_update,
            doc_status=doc_status,
            m_rid=m_rid,
            timeout=timeout,
            offset=offset,
        )


class Fallbacks(Outages):
    """Parameters for Fall-backs [IFs IN 7.2, mFRR 3.11, aFRR 3.10].

    Data view:
    https://transparency.entsoe.eu/outage-domain/r2/unavailabilityInTransmissionGrid/show

    Fixed parameters:
    - documentType: A53 (Outage publication document)

    Required parameters:
    - processType: A47 (Manual frequency restoration reserve),
      A51 (Automatic frequency restoration reserve), A63 (Imbalance Netting)
    - businessType: C47 (Disconnection), A53 (Planned maintenance),
      A54 (Unplanned outage), A83 (Auction cancellation)

    Notes:
    - Returns fall-back data for frequency restoration reserves and
      imbalance netting
    - Both processType and businessType are mandatory for this endpoint
    - Period parameters are optional if PeriodStartUpdate/PeriodEndUpdate
      are defined
    """

    code = "Fall-backs"

    def __init__(
        self,
        security_token: str,
        process_type: str,
        business_type: str,
        bidding_zone_domain: str,
        # Time period parameters (at least one set required)
        period_start: Optional[int] = None,
        period_end: Optional[int] = None,
        period_start_update: Optional[int] = None,
        period_end_update: Optional[int] = None,
        # Optional filtering parameters
        doc_status: Optional[str] = None,
        m_rid: Optional[str] = None,
        # Additional common parameters
        timeout: int = 5,
        offset: int = 0,
    ):
        """
        Initialize fall-backs parameters.

        Args:
            security_token: API security token
            process_type: Process type (A47=Manual frequency restoration
                        reserve, A51=Automatic frequency restoration reserve,
                        A63=Imbalance Netting)
            business_type: Business type (C47=Disconnection,
                         A53=Planned maintenance, A54=Unplanned outage,
                         A83=Auction cancellation)
            bidding_zone_domain: EIC code of a CTA/LFA/REG
            period_start: Start period (YYYYMMDDHHMM format, optional if
                         period_start_update defined)
            period_end: End period (YYYYMMDDHHMM format, optional if
                       period_end_update defined)
            period_start_update: Start of update period (YYYYMMDDHHMM format)
            period_end_update: End of update period (YYYYMMDDHHMM format)
            doc_status: Document status (A13=Withdrawn, by default withdrawn
                       publications not returned)
            m_rid: Message ID for specific publication versions
            timeout: Request timeout in seconds
            offset: Offset for pagination
        """
        super().__init__(
            document_type="A53",
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            period_start_update=period_start_update,
            period_end_update=period_end_update,
            business_type=business_type,
            doc_status=doc_status,
            m_rid=m_rid,
            timeout=timeout,
            offset=offset,
        )

        # Add process type parameter specific to this endpoint
        self.add_business_params(process_type=process_type)

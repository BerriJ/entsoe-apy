from typing import Optional

from .Base import Base


class Market(Base):
    """Market data parameters for ENTSO-E Transparency Platform queries."""

    def __init__(
        self,
        document_type: str,
        period_start: int,
        period_end: int,
        # Domain parameters - at least one required
        in_domain: Optional[str] = None,
        out_domain: Optional[str] = None,
        domain_mrid: Optional[str] = None,
        # Optional parameters based on Postman collection
        business_type: Optional[str] = None,
        process_type: Optional[str] = None,
        contract_market_agreement_type: Optional[str] = None,
        auction_type: Optional[str] = None,
        auction_category: Optional[str] = None,
        classification_sequence_attribute_instance_component_position: Optional[
            int
        ] = None,
        # Additional common parameters
        offset: int | None = None,
    ):
        """
        Initialize market data parameters for ENTSO-E Transparency Platform.

        Args:
            document_type: Document type (e.g., A25, A26, A31, A44, A94, A09, B09, B33)
            period_start: Start period (YYYYMMDDHHMM format)
            period_end: End period (YYYYMMDDHHMM format)
            in_domain: Input domain/bidding zone (e.g., 10YBE----------2)
            out_domain: Output domain/bidding zone (e.g., 10YGB----------A)
            domain_mrid: Domain mRID for specific queries (e.g., 10YDOM-REGION-1V)
            business_type: Business type (e.g., A29, A31, A34, A37, A43, B05, B07,
                          B08, B10, B11)
            process_type: Process type (e.g., A44 for flow-based allocations)
            contract_market_agreement_type: Contract market agreement type (A01,
                                           A05, A06, A07)
            auction_type: Auction type (A01, A02)
            auction_category: Auction category (A04)
            classification_sequence_attribute_instance_component_position: Position
                for classification
            offset: Offset for pagination

        Raises:
            ValidationError: If any input parameter is invalid


        """
        # Initialize base parameters
        super().__init__(
            document_type=document_type,
            period_start=period_start,
            period_end=period_end,
            offset=offset,
        )

        # Add domain parameters
        self.add_domain_params(
            in_domain=in_domain,
            out_domain=out_domain,
            domain_mrid=domain_mrid,
        )

        # Add business parameters
        self.add_business_params(
            business_type=business_type,
            process_type=process_type,
        )

        # Add market parameters
        self.add_market_params(
            contract_market_agreement_type=contract_market_agreement_type,
            auction_type=auction_type,
            auction_category=auction_category,
        )

        # Add classification parameter if provided
        self.add_optional_param(
            "classificationSequence_AttributeInstanceComponent.position",
            classification_sequence_attribute_instance_component_position,
        )

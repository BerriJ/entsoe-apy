from typing import Optional


def Market_params(
    document_type: str,
    security_token: str,
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
    classification_sequence_attribute_instance_component_position: Optional[int] = None,
    # Additional common parameters
    timeout: int = 60,
    offset: Optional[int] = None,
) -> object:
    """
    Request market data from ENTSO-E Transparency Platform.

    Args:
        document_type: Document type (e.g., A25, A26, A31, A44, A94, A09, B09, B33)
        security_token: API security token
        period_start: Start period (YYYYMMDDHHMM format)
        period_end: End period (YYYYMMDDHHMM format)
        in_domain: Input domain/bidding zone (e.g., 10YBE----------2)
        out_domain: Output domain/bidding zone (e.g., 10YGB----------A)
        domain_mrid: Domain mRID for specific queries (e.g., 10YDOM-REGION-1V)
        business_type: Business type (e.g., A29, A31, A34, A37, A43, B05, B07, B08, B10, B11)
        process_type: Process type (e.g., A44 for flow-based allocations)
        contract_market_agreement_type: Contract market agreement type (A01, A05, A06, A07)
        auction_type: Auction type (A01, A02)
        auction_category: Auction category (A04)
        classification_sequence_attribute_instance_component_position: Position for classification
        timeout: Request timeout in seconds
        offset: Offset for pagination

    Raises:
        ValidationError: If any input parameter is invalid
    """
    # Build query parameters
    params = {
        "documentType": document_type,
        "securityToken": security_token,
        "periodStart": period_start,
        "periodEnd": period_end,
    }

    # Add domain parameters - at least one typically required
    if in_domain:
        params["in_Domain"] = in_domain
    if out_domain:
        params["out_Domain"] = out_domain
    if domain_mrid:
        params["domain.mRID"] = domain_mrid

    # Add optional parameters if provided
    if business_type:
        params["businessType"] = business_type
    if process_type:
        params["processType"] = process_type
    if contract_market_agreement_type:
        params["contract_MarketAgreement.Type"] = contract_market_agreement_type
    if auction_type:
        params["auction.Type"] = auction_type
    if auction_category:
        params["auction.category"] = auction_category
    if classification_sequence_attribute_instance_component_position:
        params["classificationSequence_AttributeInstanceComponent.position"] = (
            classification_sequence_attribute_instance_component_position
        )
    if offset:
        params["offset"] = offset

    return params

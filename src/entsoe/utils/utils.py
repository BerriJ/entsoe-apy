from datetime import datetime, timedelta
import inspect
from xml.etree import ElementTree as ET

from loguru import logger
from pydantic import BaseModel

import entsoe.xml_models as xml_models


class RangeLimitError(Exception):
    """Raised when the requested date range exceeds API limits."""

    pass


def parse_entsoe_datetime(date_int: int) -> datetime:
    """
    Parse ENTSOE datetime format (YYYYMMDDHHMM) to datetime object.

    Args:
        date_int: Date in YYYYMMDDHHMM format

    Returns:
        datetime object
    """
    date_str = str(date_int)
    return datetime.strptime(date_str, "%Y%m%d%H%M")


def format_entsoe_datetime(dt: datetime) -> int:
    """
    Format datetime object to ENTSOE datetime format (YYYYMMDDHHMM).

    Args:
        dt: datetime object

    Returns:
        Date in YYYYMMDDHHMM format as integer
    """
    return int(dt.strftime("%Y%m%d%H%M"))


def check_date_range_limit(
    period_start: int, period_end: int, max_days: int = 365
) -> bool:
    """
    Check if date range exceeds the specified limit.

    Args:
        period_start: Start date in YYYYMMDDHHMM format
        period_end: End date in YYYYMMDDHHMM format
        max_days: Maximum allowed days (default: 365 for 1 year)

    Returns:
        True if range exceeds limit, False otherwise
    """
    logger.debug(
        f"Checking date range limit: {period_start} to {period_end}, "
        f"max_days: {max_days}"
    )

    start_dt = parse_entsoe_datetime(period_start)
    end_dt = parse_entsoe_datetime(period_end)
    diff = end_dt - start_dt

    exceeds_limit = diff.days > max_days
    logger.debug(f"Date range spans {diff.days} days, exceeds limit: {exceeds_limit}")

    return exceeds_limit


def split_date_range(period_start: int, period_end: int) -> int:
    """
    Split a date range into the first 365 days and the remaining days.

    Args:
        period_start: Start date in YYYYMMDDHHMM format
        period_end: End date in YYYYMMDDHHMM format

    Returns:
        The pivot date (end of first segment) in YYYYMMDDHHMM format
    """
    logger.debug(f"Splitting date range: {period_start} to {period_end}")

    start_dt = parse_entsoe_datetime(period_start)

    # Add 365 days to the start date
    pivot_dt = start_dt + timedelta(days=365)

    period_pivot = format_entsoe_datetime(pivot_dt)

    logger.debug(f"Split at {period_pivot}")

    return period_pivot


def extract_namespace_and_find_classes(response) -> tuple[str, type]:
    logger.debug("Extracting namespace from XML response")

    root = ET.fromstring(response.text)
    if root.tag[0] == "{":
        namespace = root.tag[1:].split("}")[0]
    else:
        raise ValueError("No default namespace found in root element")

    if not namespace:
        raise ValueError("Empty namespace found in root element")

    logger.debug(f"Extracted namespace: {namespace}")

    matching_classes = []

    # Get all classes from the xml_models module
    for name, obj in inspect.getmembers(xml_models, inspect.isclass):
        if hasattr(obj, "Meta") and hasattr(obj.Meta, "namespace"):
            if obj.Meta.namespace == namespace:
                matching_classes.append((name, obj))

    logger.debug(f"Found {len(matching_classes)} matching classes for namespace")

    if len(matching_classes) == 0:
        raise ValueError(f"No classes found matching namespace '{namespace}'")
    elif len(matching_classes) > 1:
        class_names = [name for name, _ in matching_classes]
        raise ValueError(
            f"Multiple classes found matching namespace '{namespace}': {class_names}"
        )

    selected_class = matching_classes[0][1]
    logger.debug(f"Selected class: {selected_class.__name__}")

    return namespace, selected_class


def merge_documents(base, other):
    """
    Merge `other` document into `base` document.

    Args:
        base: Base document to merge into (modified in-place)
        other: Other document to merge from

    Rules:
    - If base is None, returns other
    - If other is None, returns base
    - Lists: extend base list with other's items
    - Nested Pydantic models: merge recursively
    - Scalars: keep base value, use other only if base is None

    Returns:
        The modified base document, or other/base if one is None
    """
    if not base:
        logger.debug("Base is None/empty, returning other")
        return other
    if not other:
        logger.debug("Other is None/empty, returning base")
        return base

    base_type = type(base).__name__ if base else None
    other_type = type(other).__name__ if other else None
    logger.debug(f"Merging documents: base={base_type}, other={other_type}")

    merge_count = 0

    # Handle Pydantic models only
    if not isinstance(base, BaseModel):
        logger.debug(f"Base is not a Pydantic model: {type(base)}")
        raise TypeError("Base document must be a Pydantic model")

    # Use Pydantic model fields
    field_items = type(base).model_fields.items()

    for field_name, field_info in field_items:
        base_value = getattr(base, field_name)
        other_value = getattr(other, field_name)

        if isinstance(base_value, list) and isinstance(other_value, list):
            if other_value:  # Only log if there are items to merge
                logger.debug(
                    f"Merging list field '{field_name}': {len(base_value)} + "
                    f"{len(other_value)} items"
                )
                base_value.extend(other_value)
                merge_count += len(other_value)
        elif isinstance(base_value, BaseModel) and isinstance(other_value, BaseModel):
            logger.debug(f"Recursively merging nested model field '{field_name}'")
            merge_documents(base_value, other_value)
        elif base_value is None and other_value is not None:
            logger.debug(f"Setting field '{field_name}' from other (base was None)")
            setattr(base, field_name, other_value)
            merge_count += 1

    logger.debug(f"Document merge completed, {merge_count} fields/items merged")
    return base

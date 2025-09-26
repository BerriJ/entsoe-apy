from datetime import datetime, timedelta
import inspect
from xml.etree import ElementTree as ET

from loguru import logger

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


def split_date_range(period_start: int, period_end: int, max_days: int = 365) -> int:
    """
    Split a date range at the specified maximum number of days.

    Args:
        period_start: Start date in YYYYMMDDHHMM format
        period_end: End date in YYYYMMDDHHMM format
        max_days: Maximum days for the first segment (default: 365)

    Returns:
        The pivot date (end of first segment) in YYYYMMDDHHMM format
    """
    logger.debug(
        f"Splitting date range: {period_start} to {period_end} at {max_days} days"
    )

    start_dt = parse_entsoe_datetime(period_start)

    # Add max_days to the start date
    pivot_dt = start_dt + timedelta(days=max_days)

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

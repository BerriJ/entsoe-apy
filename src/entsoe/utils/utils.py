from datetime import datetime, timedelta, timezone
import inspect
from xml.etree import ElementTree as ET

import entsoe.xml_models as xml_models

from ..config.config import logger


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

    Convert a (tz-aware) datetime to UTC and format it as an integer in the
    ENTSOE format. If the datetime is naive, it is assumed to be in UTC.This
    function can be used to convert pd.Timestamp and pl.Datetime objects to the
    required format for ENTSOE API calls. Please have a look at the
    documentation for more details and examples.

    Args:
        dt: datetime object

    Returns:
        Date in YYYYMMDDHHMM format as integer
    """
    if dt.tzinfo is not None:
        utc_timestamp = dt.astimezone(timezone.utc)
        return int(utc_timestamp.strftime("%Y%m%d%H%M"))
    else:
        # Assume naive timestamps are in UTC
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
    logger.trace(
        f"check_date_range_limit: Enter with {period_start} to {period_end}, max_days={max_days}"
    )

    start_dt = parse_entsoe_datetime(period_start)
    end_dt = parse_entsoe_datetime(period_end)
    diff = end_dt - start_dt

    exceeds_limit = diff.days > max_days
    logger.debug(f"Date range spans {diff.days} days, exceeds limit: {exceeds_limit}")
    logger.trace(f"check_date_range_limit: Exit with {exceeds_limit}")

    return exceeds_limit


def split_date_range(
    period_start: int, period_end: int, max_days: int = 365
) -> list[tuple[int, int]]:
    """
    Split a date range into chunks of maximum specified days.

    Args:
        period_start: Start date in YYYYMMDDHHMM format
        period_end: End date in YYYYMMDDHHMM format
        max_days: Maximum days for each chunk (default: 365)

    Returns:
        List of tuples containing (start, end) dates in YYYYMMDDHHMM format for each chunk
    """
    logger.trace(
        f"split_date_range: Enter with {period_start} to {period_end}, max_days={max_days}"
    )

    date_ranges = []
    current_start = period_start
    end_dt = parse_entsoe_datetime(period_end)

    while True:
        # Check if remaining range is within limit
        current_start_dt = parse_entsoe_datetime(current_start)
        remaining_days = (end_dt - current_start_dt).days

        if remaining_days <= max_days:
            # Last chunk - add remaining range
            date_ranges.append((current_start, period_end))
            break

        # Calculate pivot date for this chunk
        pivot_dt = current_start_dt + timedelta(days=max_days)
        period_pivot = format_entsoe_datetime(pivot_dt)

        # Add this chunk
        date_ranges.append((current_start, period_pivot))

        # Move to next chunk
        current_start = period_pivot

    logger.debug(f"Split into {len(date_ranges)} chunks: {date_ranges}")
    logger.trace(f"split_date_range: Exit with {len(date_ranges)} chunks")

    return date_ranges


def extract_namespace_and_find_classes(response) -> tuple[str, type]:
    logger.trace("extract_namespace_and_find_classes: Enter")
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

    logger.trace(f"Found {len(matching_classes)} matching classes for namespace")

    if len(matching_classes) == 0:
        raise ValueError(f"No classes found matching namespace '{namespace}'")
    elif len(matching_classes) > 1:
        class_names = [name for name, _ in matching_classes]
        raise ValueError(
            f"Multiple classes found matching namespace '{namespace}': {class_names}"
        )

    selected_class = matching_classes[0][1]
    logger.debug(f"Selected class: {selected_class.__name__}")
    logger.trace(
        f"extract_namespace_and_find_classes: Exit with {selected_class.__name__}"
    )

    return namespace, selected_class

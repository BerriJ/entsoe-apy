from dataclasses import fields, is_dataclass
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


def split_date_range(period_start: int, period_end: int) -> tuple[int, int]:
    """
    Split a date range into two equal parts.

    Args:
        period_start: Start date in YYYYMMDDHHMM format
        period_end: End date in YYYYMMDDHHMM format

    Returns:
        Tuple of (pivot_date, end_date) where pivot_date is the midpoint
    """
    logger.debug(f"Splitting date range: {period_start} to {period_end}")

    start_dt = parse_entsoe_datetime(period_start)
    end_dt = parse_entsoe_datetime(period_end)

    # Calculate the midpoint
    diff = end_dt - start_dt
    pivot_dt = start_dt + (diff / 2)

    pivot_date = format_entsoe_datetime(pivot_dt)
    logger.debug(f"Split result: pivot={pivot_date}, end={period_end}")

    return pivot_date, period_end


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
        if (
            hasattr(obj, "__dataclass_fields__")
            and hasattr(obj, "Meta")
            and hasattr(obj.Meta, "namespace")
        ):
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
    - Nested dataclasses: merge recursively
    - Scalars: keep base value, use other only if base is None

    Returns:
        The modified base document, or other/base if one is None
    """
    base_type = type(base).__name__ if base else None
    other_type = type(other).__name__ if other else None
    logger.debug(f"Merging documents: base={base_type}, other={other_type}")

    if not base:
        logger.debug("Base is None/empty, returning other")
        return other
    if not other:
        logger.debug("Other is None/empty, returning base")
        return base

    merge_count = 0
    for field in fields(base):
        base_value = getattr(base, field.name)
        other_value = getattr(other, field.name)

        if isinstance(base_value, list) and isinstance(other_value, list):
            if other_value:  # Only log if there are items to merge
                logger.debug(
                    f"Merging list field '{field.name}': {len(base_value)} + "
                    f"{len(other_value)} items"
                )
                base_value.extend(other_value)
                merge_count += len(other_value)
        elif is_dataclass(base_value) and is_dataclass(other_value):
            logger.debug(f"Recursively merging dataclass field '{field.name}'")
            merge_documents(base_value, other_value)
        elif base_value is None and other_value is not None:
            logger.debug(f"Setting field '{field.name}' from other (base was None)")
            setattr(base, field.name, other_value)
            merge_count += 1

    logger.debug(f"Document merge completed, {merge_count} fields/items merged")
    return base


def parse_duration_to_minutes(duration_str):
    """Parse ISO 8601 duration string to minutes."""
    # Examples: "PT15M" -> 15, "PT60M" -> 60, "PT1H" -> 60
    if "PT" in duration_str:
        duration_str = duration_str.replace("PT", "")

    if "H" in duration_str:
        hours = int(duration_str.replace("H", ""))
        return hours * 60
    elif "M" in duration_str:
        return int(duration_str.replace("M", ""))
    else:
        return 60  # Default to 60 minutes if unclear


def calculate_timestamp(period_start_str, position, resolution_str):
    """Calculate the actual timestamp for a data point."""
    # Parse the period start timestamp
    # Format: '2025-08-21T22:00Z'
    period_start_str = period_start_str.replace("Z", "+00:00")
    period_start = datetime.fromisoformat(period_start_str)

    # Get resolution in minutes
    resolution_minutes = parse_duration_to_minutes(resolution_str)

    # Calculate timestamp for this position (position starts at 1)
    minutes_offset = (position - 1) * resolution_minutes
    timestamp = period_start + timedelta(minutes=minutes_offset)

    return timestamp


def ts_to_dict(time_series):
    data_rows = []
    for i, ts in enumerate(time_series):
        periods = ts.period

        for period in periods:
            points = period.point

            period_start_str = str(period.time_interval.start)
            resolution_str = str(period.resolution)

            # Extract each data point
            for point in points:
                # Calculate the actual timestamp for this data point
                timestamp = calculate_timestamp(
                    period_start_str, point.position, resolution_str
                )

                row = {
                    "timestamp": timestamp,
                    "position": point.position,
                    "price_amount": float(point.price_amount),
                    "currency": str(ts.currency_unit_name.name),
                    "price_measure_unit": str(ts.price_measure_unit_name.name),
                    "in_domain": str(ts.in_domain_m_rid.value),
                    "resolution": resolution_str,
                    "resolution_minutes": parse_duration_to_minutes(resolution_str),
                    "business_type": ts.business_type.name,
                    "contract_market_agreement_type": (
                        ts.contract_market_agreement_type.name
                    ),
                }
                data_rows.append(row)

    # Print progress for every 100 time series
    if (i + 1) % 100 == 0:
        print(f"Processed {i + 1}/{len(time_series)} time series...")

    return data_rows

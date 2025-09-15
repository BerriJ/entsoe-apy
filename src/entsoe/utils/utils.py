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


def ts_to_dict(time_series: list) -> list[dict]:
    """
    Convert arbitrary TimeSeries objects to a list of dictionaries.

    This function works with any TimeSeries class from the xml_models package,
    dynamically extracting available fields using dataclass introspection.
    This makes it compatible with all the various TimeSeries classes defined
    in the entsoe/xml_models folder, regardless of their specific field structures.

    The function extracts:
    - All fields from Point objects (e.g., position, price_amount, quantity, etc.)
    - All fields from TimeSeries objects with 'ts_' prefix to avoid conflicts
    - Calculated timestamps when period and position data is available
    - Period-level information (resolution, resolution_minutes)

    Args:
        time_series: List of TimeSeries objects from any xml_models schema.
                    Can contain mixed types of TimeSeries objects.

    Returns:
        List of dictionaries where each dictionary represents one data point.
        Each dictionary contains:
        - position: Position index from the Point object
        - timestamp: Calculated timestamp (when available)
        - resolution: Period resolution string
        - resolution_minutes: Period resolution in minutes
        - All Point fields (varies by schema)
        - All TimeSeries fields with 'ts_' prefix (varies by schema)

    Examples:
        >>> from entsoe.xml_models.iec62325_451_3_publication_v7_3 import TimeSeries
        >>> result = ts_to_dict([publication_time_series])
        >>> # Returns dicts with fields like:
        >>> # position, timestamp, price_amount, ts_currency_unit_name, etc.

        >>> from entsoe.xml_models.iec62325_451_6_generationload_v3_0 import TimeSeries
        >>> result = ts_to_dict([generation_time_series])
        >>> # Returns dicts with fields like:
        >>> # position, timestamp, quantity, secondary_quantity, ts_curve_type, etc.
    """
    data_rows = []
    for i, ts in enumerate(time_series):
        # Handle case where ts might not have period attribute
        if not hasattr(ts, "period"):
            logger.debug(
                f"TimeSeries object at index {i} has no 'period' attribute, skipping"
            )
            continue

        periods = ts.period

        for period in periods:
            # Handle case where period might not have point attribute
            if not hasattr(period, "point"):
                logger.debug("Period object has no 'point' attribute, skipping")
                continue

            points = period.point

            # Extract period-level information
            period_start_str = (
                str(period.time_interval.start)
                if hasattr(period, "time_interval") and period.time_interval
                else None
            )
            resolution_str = (
                str(period.resolution)
                if hasattr(period, "resolution") and period.resolution
                else None
            )

            # Extract each data point
            for point in points:
                row = {
                    "position": point.position if hasattr(point, "position") else None,
                    "timestamp": None,  # Always include timestamp field
                }

                # Add timestamp calculation if we have the necessary data
                if (
                    period_start_str
                    and resolution_str
                    and hasattr(point, "position")
                    and point.position
                ):
                    try:
                        timestamp = calculate_timestamp(
                            period_start_str, point.position, resolution_str
                        )
                        row["timestamp"] = timestamp
                    except Exception as e:
                        logger.debug(f"Could not calculate timestamp: {e}")
                        # row["timestamp"] remains None

                # Add period-level data
                if resolution_str:
                    row["resolution"] = resolution_str
                    row["resolution_minutes"] = parse_duration_to_minutes(
                        resolution_str
                    )

                # Dynamically extract all fields from the point object
                if is_dataclass(point):
                    for field_info in fields(point):
                        field_name = field_info.name
                        if field_name == "position":  # Already handled above
                            continue

                        field_value = getattr(point, field_name, None)
                        if field_value is not None:
                            # Handle different types of field values
                            if hasattr(field_value, "value"):
                                # e.g., AreaIdString.value
                                row[field_name] = str(field_value.value)
                            elif hasattr(field_value, "name"):  # e.g., enum.name
                                row[field_name] = str(field_value.name)
                            elif isinstance(field_value, (int, float, str)):
                                row[field_name] = field_value
                            elif hasattr(field_value, "__float__"):  # Decimal, etc.
                                row[field_name] = float(field_value)
                            else:
                                row[field_name] = str(field_value)

                # Dynamically extract all fields from the TimeSeries object
                if is_dataclass(ts):
                    for field_info in fields(ts):
                        field_name = field_info.name
                        if field_name == "period":  # Already handled above
                            continue

                        field_value = getattr(ts, field_name, None)
                        if field_value is not None:
                            # Create a prefixed field name to avoid conflicts
                            ts_field_name = f"ts_{field_name}"

                            # Handle different types of field values
                            if hasattr(field_value, "value"):
                                # e.g., AreaIdString.value
                                row[ts_field_name] = str(field_value.value)
                            elif hasattr(field_value, "name"):  # e.g., enum.name
                                row[ts_field_name] = str(field_value.name)
                            elif isinstance(field_value, (int, float, str)):
                                row[ts_field_name] = field_value
                            elif hasattr(field_value, "__float__"):  # Decimal, etc.
                                row[ts_field_name] = float(field_value)
                            elif isinstance(field_value, list):
                                # Skip list fields to avoid complexity
                                continue
                            else:
                                row[ts_field_name] = str(field_value)

                data_rows.append(row)

        # Print progress for every 100 time series
        if (i + 1) % 100 == 0:
            print(f"Processed {i + 1}/{len(time_series)} time series...")

    return data_rows

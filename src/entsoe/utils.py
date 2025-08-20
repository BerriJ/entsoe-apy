from dataclasses import fields, is_dataclass
from datetime import datetime
import inspect
from xml.etree import ElementTree as ET

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
    start_dt = parse_entsoe_datetime(period_start)
    end_dt = parse_entsoe_datetime(period_end)
    diff = end_dt - start_dt
    return diff.days > max_days


def split_date_range(period_start: int, period_end: int) -> tuple[int, int]:
    """
    Split a date range into two equal parts.

    Args:
        period_start: Start date in YYYYMMDDHHMM format
        period_end: End date in YYYYMMDDHHMM format

    Returns:
        Tuple of (pivot_date, end_date) where pivot_date is the midpoint
    """
    start_dt = parse_entsoe_datetime(period_start)
    end_dt = parse_entsoe_datetime(period_end)

    # Calculate the midpoint
    diff = end_dt - start_dt
    pivot_dt = start_dt + (diff / 2)

    return format_entsoe_datetime(pivot_dt), period_end


def extract_namespace_and_find_classes(response) -> tuple[str, type]:
    root = ET.fromstring(response.text)
    if root.tag[0] == "{":
        namespace = root.tag[1:].split("}")[0]
    else:
        raise ValueError("No default namespace found in root element")

    if not namespace:
        raise ValueError("Empty namespace found in root element")

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

    if len(matching_classes) == 0:
        raise ValueError(f"No classes found matching namespace '{namespace}'")
    elif len(matching_classes) > 1:
        class_names = [name for name, _ in matching_classes]
        raise ValueError(
            f"Multiple classes found matching namespace '{namespace}': {class_names}"
        )
    return namespace, matching_classes[0][1]


def merge_documents(base, other):
    """
    Merge `other` document into `base` document.

    Rules:
    - Lists: extend base list with other's items
    - Nested dataclasses: merge recursively
    - Scalars: keep base value, use other only if base is None

    Returns the modified base document.
    """
    if base is None and other is None:
        return None
    if base is None:
        return other
    if other is None:
        return base

    for field in fields(base):
        field_name = field.name
        base_value = getattr(base, field_name)
        other_value = getattr(other, field_name)

        # Handle lists: extend base with other's items
        if isinstance(base_value, list) and isinstance(other_value, list):
            base_value.extend(other_value)
            continue

        # Handle nested dataclasses: merge recursively
        if is_dataclass(base_value) and is_dataclass(other_value):
            merge_documents(base_value, other_value)
            continue

        # Handle scalars: use other value only if base is None
        if base_value is None and other_value is not None:
            setattr(base, field_name, other_value)

    return base

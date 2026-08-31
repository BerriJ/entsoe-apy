from datetime import datetime
from typing import Any, Literal

import isodate

from ..config.config import logger


def calculate_timestamp(
    start: str,
    resolution: str,
    position: int,
    interval_type: Literal["start", "end"] = "start",
) -> str:
    """
    Calculate actual timestamp from period information in ENTSO-E data.

    This function calculates the actual timestamp for a data point based on:
    - start: Start of the time interval (ISO 8601 format)
    - resolution: Time increment (ISO 8601 duration format)
    - position: 1-indexed position within the interval

    Args:
        start: Start timestamp in ISO format (e.g., '2015-01-01T00:00Z')
        resolution: Time resolution as ISO 8601 duration
                   (e.g., 'PT60M' for 60 minutes, 'P1Y' for 1 year,
                    'P1M' for 1 month, 'P1D' for 1 day)
        position: 1-indexed position in the interval (1 = first position)

    Returns:
        str: Calculated timestamp in ISO format

    Examples:
        >>> # Hourly resolution
        >>> ts = calculate_timestamp('2024-08-19T22:00Z', 'PT60M', 1)
        >>> print(ts)
        2024-08-19T22:00:00+00:00

        >>> ts = calculate_timestamp('2024-08-19T22:00Z', 'PT60M', 2)
        >>> print(ts)
        2024-08-19T23:00:00+00:00

        >>> # Yearly resolution
        >>> ts = calculate_timestamp('2015-01-01T00:00Z', 'P1Y', 1)
        >>> print(ts)
        2015-01-01T00:00:00+00:00

        >>> ts = calculate_timestamp('2015-01-01T00:00Z', 'P1Y', 2)
        >>> print(ts)
        2016-01-01T00:00:00+00:00
    """
    start_dt = datetime.fromisoformat(start)
    duration = isodate.parse_duration(resolution)
    if interval_type == "end":
        timestamp = start_dt + (duration * position)
    elif interval_type == "start":
        timestamp = start_dt + (duration * (position - 1))
    else:
        raise ValueError(
            f"Invalid interval_type: {interval_type}. Must be 'start' or 'end'."
        )
    timestamp_str = timestamp.isoformat()
    return timestamp_str


def find_field_key(record: dict[str, Any], search_field: str) -> str | None:
    """
    Find a field key in the record by exact match or suffix match.

    Args:
        record: The record dictionary to search in
        search_field: The field pattern to search for

    Returns:
        The actual key from the record, or None if not found
    """
    # First try exact match
    if search_field in record:
        return search_field

    # Then try suffix match
    for key in record:
        if key.endswith(search_field):
            return key

    return None


def add_timestamps(
    records: list[dict[str, Any]],
    start_field: str = "period.time_interval.start",
    resolution_field: str = "period.resolution",
    position_field: str = "period.point.position",
    timestamp_field: str = "timestamp",
    interval_type: Literal["start", "end"] = "start",
) -> list[dict[str, Any]]:
    """
    Add calculated timestamps to records from extract_records().

    This function takes the output from extract_records() and adds a timestamp
    field to each record by calculating it from the period information fields.

    Field matching supports both exact matches and suffix matches. For example,
    if you specify "period.resolution" as the resolution_field, it will match
    both "period.resolution" (exact) and "time_series.period.resolution" (suffix).

    Args:
        records: List of dictionaries from extract_records()
        start_field: Dotted path to the start time field in the records.
                    Can be a full path or suffix that matches the end of a key.
                    Defaults to "period.time_interval.start"
        resolution_field: Dotted path to the resolution field in the records.
                         Can be a full path or suffix that matches the end of a key.
                         Defaults to "period.resolution"
        position_field: Dotted path to the position field in the records.
                       Can be a full path or suffix that matches the end of a key.
                       Defaults to "period.point.position"
        timestamp_field: Name of the new field to add for the calculated timestamp.
                        Defaults to "timestamp"
        interval_type: Whether to use the start or end of the time interval.
                      - "start": Use the beginning of the interval (default)
                      - "end": Use the end of the interval (adds one resolution unit)

    Returns:
        List of dictionaries with added timestamp field. Original records are not modified.

    Raises:
        KeyError: If required fields are not found in a record
        ValueError: If field values are invalid for timestamp calculation

    Examples:
        >>> records = [
        ...     {
        ...         'time_series.period.time_interval.start': '2024-08-19T22:00Z',
        ...         'time_series.period.resolution': 'PT60M',
        ...         'time_series.period.point.position': 1,
        ...         'value': 100
        ...     }
        ... ]
        >>> # Works with partial field names
        >>> result = add_timestamps(records,
        ...                         start_field="period.time_interval.start",
        ...                         resolution_field="period.resolution",
        ...                         position_field="period.point.position")
        >>> print(result[0]['timestamp'])
        2024-08-19T22:00:00+00:00
    """

    enriched_records = []
    missing_fields_logged = False

    for i, record in enumerate(records):
        # Create a copy to avoid modifying the original
        enriched_record = record.copy()

        # Find the actual keys in the record
        actual_start_field = find_field_key(record, start_field)
        actual_resolution_field = find_field_key(record, resolution_field)
        actual_position_field = find_field_key(record, position_field)

        # Check if all required fields are present
        missing_fields = []
        if actual_start_field is None:
            missing_fields.append(start_field)
        if actual_resolution_field is None:
            missing_fields.append(resolution_field)
        if actual_position_field is None:
            missing_fields.append(position_field)

        if missing_fields:
            if not missing_fields_logged:
                logger.debug(
                    f"Skipping timestamp calculation: "
                    f"missing required fields: {missing_fields}. "
                    f"Available keys: {list(record.keys())[:3]}..."
                )
                missing_fields_logged = True
            enriched_records.append(enriched_record)
            continue

        try:
            # Extract values from the record using the actual keys
            # Type checker: we already verified these are not None above
            assert actual_start_field is not None
            assert actual_resolution_field is not None
            assert actual_position_field is not None

            start = record[actual_start_field]
            resolution = record[actual_resolution_field]
            position = record[actual_position_field]

            # Calculate timestamp
            timestamp = calculate_timestamp(
                start, resolution, position, interval_type=interval_type
            )

            # Add timestamp to the record
            enriched_record[timestamp_field] = timestamp

        except (ValueError, TypeError) as e:
            logger.warning(
                f"Failed to calculate timestamp for record {i}: {e}. "
                f"Values: start={record.get(actual_start_field) if actual_start_field else 'N/A'}, "
                f"resolution={record.get(actual_resolution_field) if actual_resolution_field else 'N/A'}, "
                f"position={record.get(actual_position_field) if actual_position_field else 'N/A'}"
            )

        enriched_records.append(enriched_record)

    return enriched_records

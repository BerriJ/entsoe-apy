from typing import Any

from pydantic import BaseModel

from ..config.config import logger

_DEFAULT_IGNORE_FIELDS = ["m_rid", "time_series.m_rid"]
_UNSET = object()


def _deduplicate_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Remove duplicate records while preserving order."""
    seen = set()
    unique_records = []
    for record in records:
        record_key = frozenset(record.items())
        if record_key not in seen:
            seen.add(record_key)
            unique_records.append(record)
    return unique_records


def normalize_to_records(
    data: dict[str, Any] | list[Any] | Any,
    parent_key: str = "",
    sep: str = ".",
    ignore_fields: list[str] | None = None,
) -> list[dict[str, Any]]:
    """
    Recursively flattens nested JSON/dictionary structures into a list of records suitable for pandas DataFrames.

    This function handles complex nested data by:
    - Flattening nested dictionaries using dot notation (e.g., {"a": {"b": 1}} -> {"a.b": 1})
    - Expanding lists into multiple records (one per list element)
    - Creating cross-products when multiple lists exist at the same level
    - Preserving primitive values as-is
    - Filtering out specified fields from the final records

    Args:
        data: The input data to flatten. Can be a dictionary, list, or primitive value.
        parent_key: The parent key prefix for nested structures. Used internally for recursion.
        sep: The separator character used to join nested keys. Defaults to ".".
        ignore_fields: List of field names to exclude from the flattened records. Fields are
                      matched by their full dotted path (e.g., "m_rid", "time_series.m_rid").

    Returns:
        A list of flattened dictionaries where each dictionary represents a record
        suitable for creating a pandas DataFrame, with ignored fields removed.

    Examples:
        >>> data = {"user": "john", "orders": [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]}
        >>> normalize_to_records(data)
        [
            {"user": "john", "orders.id": 1, "orders.amount": 100},
            {"user": "john", "orders.id": 2, "orders.amount": 200}
        ]

        >>> data = {"nested": {"level1": {"level2": "value"}}}
        >>> normalize_to_records(data)
        [{"nested.level1.level2": "value"}]

        >>> data = {"m_rid": "123", "user": "john", "orders": [{"id": 1}]}
        >>> normalize_to_records(data, ignore_fields=["m_rid"])
        [{"user": "john", "orders.id": 1}]
    """

    if ignore_fields is None:
        ignore_fields = []

    def _filter_ignored_fields(record: dict[str, Any]) -> dict[str, Any]:
        """Filter out ignored fields from a record."""
        return {k: v for k, v in record.items() if k not in ignore_fields}

    if isinstance(data, dict):
        items: dict[str, Any] = {}
        expansions: list[list[dict[str, Any]]] = []
        for k, v in data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                sub_records = normalize_to_records(
                    v, new_key, sep=sep, ignore_fields=ignore_fields
                )
                if len(sub_records) == 1:
                    items.update(sub_records[0])
                elif len(sub_records) > 1:
                    expansions.append(sub_records)
            elif isinstance(v, list):
                # Expand list elements into multiple records
                list_records = []
                for elem in v:
                    if isinstance(elem, dict):
                        sub_records = normalize_to_records(
                            elem, new_key, sep=sep, ignore_fields=ignore_fields
                        )
                        list_records.extend(sub_records)
                    else:
                        list_records.append({new_key: elem})
                if list_records:
                    expansions.append(list_records)
            else:
                items[new_key] = v
        # Cross-join base items with all collected expansions
        result: list[dict[str, Any]] = [items]
        for expansion in expansions:
            result = [dict(r, **e) for r in result for e in expansion]
        return [_filter_ignored_fields(r) for r in result]
    elif isinstance(data, list):
        records = []
        for elem in data:
            records.extend(
                normalize_to_records(
                    elem, parent_key, sep=sep, ignore_fields=ignore_fields
                )
            )
        return records
    else:
        return [_filter_ignored_fields({parent_key: data})]


def extract_records(
    data: BaseModel | list[BaseModel],
    domain: str | None = None,
    ignore_fields: list[str] | None = _UNSET,  # type: ignore[assignment]
    deduplicate: bool = True,
) -> list[dict[str, int | float | str | None]]:
    """
    Convert a Pydantic model or list of Pydantic models to a list of flattened records suitable for pandas DataFrame.

    This function now handles both single BaseModel instances and lists of BaseModel instances,
    flattening all data into a unified list of records. When multiple BaseModel instances
    are provided, their records are combined while preserving the individual metadata
    and structure of each model.

    Args:
        data: Single Pydantic model instance or list of Pydantic model instances.
              When a list is provided, all models are processed and their records
              are combined into a single result list.
        domain: Optional key to extract a specific domain from each model.
               When specified, only the data under this key is extracted from
               each BaseModel instance.
        ignore_fields: Optional list of field names to exclude from the flattened records.
                      Fields are matched by their full dotted path (e.g., "m_rid", "time_series.m_rid").
                      Defaults to ["m_rid", "time_series.m_rid"].
                      Pass None to disable field filtering.
        deduplicate: Whether to remove duplicate records while preserving order. Defaults to True.

    Returns:
        List of flattened dictionaries (records) from all BaseModel instances.

    Raises:
        KeyError: If specified domain is not found in the data
        TypeError: If data is not a BaseModel or list of BaseModels

    Note:
        If mixed BaseModel types are detected in a list, a warning is logged
        as this may result in inconsistent record structures.
    """
    if ignore_fields is _UNSET:
        ignore_fields = _DEFAULT_IGNORE_FIELDS

    # Convert single BaseModel to list for uniform processing
    if isinstance(data, BaseModel):
        data_list = [data]
    elif isinstance(data, list):
        for item in data:
            if not isinstance(item, BaseModel):
                raise TypeError(
                    f"Expected all items in the list to be BaseModel instances, got {type(item)}"
                )
        data_list = data

        # Check if all BaseModel instances have the same type
        if len(data_list) > 1:
            first_type = type(data_list[0])
            different_types = [
                type(item) for item in data_list if type(item) is not first_type
            ]
            if different_types:
                unique_types = {type(item).__name__ for item in data_list}
                logger.warning(
                    f"Mixed BaseModel types detected in list: {sorted(unique_types)}. "
                    "This may result in inconsistent record structures."
                )
    else:
        raise TypeError(
            f"Expected data to be a BaseModel or list of BaseModel instances, got {type(data)}"
        )

    data_dict = [item.model_dump(mode="json") for item in data_list]
    all_records = []

    if domain:
        # Check if domain exists in all dictionaries
        available_keys = set().union(*(d.keys() for d in data_dict))
        if domain not in available_keys:
            raise KeyError(
                f"Domain '{domain}' not found in data. Available keys: {available_keys}"
            )

        # Extract the domain from each dictionary and flatten all results
        for item_dict in data_dict:
            if domain in item_dict:
                domain_records = normalize_to_records(
                    item_dict[domain], ignore_fields=ignore_fields
                )
                all_records.extend(domain_records)
    else:
        for item_dict in data_dict:
            all_records.extend(
                normalize_to_records(item_dict, ignore_fields=ignore_fields)
            )

    return _deduplicate_records(all_records) if deduplicate else all_records

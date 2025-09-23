from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel


def normalize_to_records(
    data: Union[Dict[str, Any], List[Any], Any], parent_key: str = "", sep: str = "."
) -> List[Dict[str, Any]]:
    """
    Recursively flattens nested JSON/dictionary structures into a list of records suitable for pandas DataFrames.

    This function handles complex nested data by:
    - Flattening nested dictionaries using dot notation (e.g., {"a": {"b": 1}} -> {"a.b": 1})
    - Expanding lists into multiple records (one per list element)
    - Creating cross-products when multiple lists exist at the same level
    - Preserving primitive values as-is

    Args:
        data: The input data to flatten. Can be a dictionary, list, or primitive value.
        parent_key: The parent key prefix for nested structures. Used internally for recursion.
        sep: The separator character used to join nested keys. Defaults to ".".

    Returns:
        A list of flattened dictionaries where each dictionary represents a record
        suitable for creating a pandas DataFrame.

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
    """

    if isinstance(data, dict):
        items = {}
        for k, v in data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(normalize_to_records(v, new_key, sep=sep)[0])  # merge dict
            elif isinstance(v, list):
                # Expand list elements into multiple records
                list_records = []
                for elem in v:
                    if isinstance(elem, dict):
                        sub_records = normalize_to_records(elem, new_key, sep=sep)
                        list_records.extend(sub_records)
                    else:
                        list_records.append({new_key: elem})
                # Cross join if multiple records, else just keep one
                if list_records:
                    return [dict(items, **lr) for lr in list_records]
            else:
                items[new_key] = v
        return [items]
    elif isinstance(data, list):
        records = []
        for elem in data:
            records.extend(normalize_to_records(elem, parent_key, sep=sep))
        return records
    else:
        return [{parent_key: data}]


def extract_records(
    data: BaseModel, domain: Optional[str] = None
) -> List[Dict[str, Union[int, float, str, None]]]:
    """
    Convert a Pydantic model to a list of flattened records suitable for pandas DataFrame.

    Args:
        data: Pydantic model instance
        domain: Optional key to extract a specific domain from the data

    Returns:
        List of flattened dictionaries (records)

    Raises:
        KeyError: If specified domain is not found in the data
    """

    if not isinstance(data, BaseModel):
        raise TypeError(f"Expected data to be a Pydantic BaseModel, got {type(data)}")

    data_dict = data.model_dump(mode="json")

    if domain:
        if domain not in data_dict:
            available_keys = list(data_dict.keys())
            raise KeyError(
                f"Domain '{domain}' not found in data. Available keys: {available_keys}"
            )
        return normalize_to_records(data_dict[domain])

    return normalize_to_records(data_dict)

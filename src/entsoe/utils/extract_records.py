from typing import Any, Dict, List, Optional

from loguru import logger
from pydantic import BaseModel


def normalize_to_records(
    data: Dict[str, Any] | List[Any] | Any, parent_key: str = "", sep: str = "."
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
    data: BaseModel | list[BaseModel], domain: Optional[str] = None
) -> List[Dict[str, int | float | str | None]]:
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

    Returns:
        List of flattened dictionaries (records) from all BaseModel instances.
        Records from multiple models are concatenated in the order they appear.

    Raises:
        KeyError: If specified domain is not found in the data
        TypeError: If data is not a BaseModel or list of BaseModels

    Note:
        If mixed BaseModel types are detected in a list, a warning is logged
        as this may result in inconsistent record structures.
    """

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
                unique_types = set([type(item).__name__ for item in data_list])
                logger.warning(
                    f"Mixed BaseModel types detected in list: {sorted(unique_types)}. "
                    "This may result in inconsistent record structures."
                )
    else:
        raise TypeError(
            f"Expected data to be a BaseModel or list of BaseModel instances, got {type(data)}"
        )

    data_dict = [item.model_dump(mode="json") for item in data_list]

    if domain:
        # Check if domain exists in all dictionaries
        available_keys = set().union(*(d.keys() for d in data_dict))
        if domain not in available_keys:
            raise KeyError(
                f"Domain '{domain}' not found in data. Available keys: {available_keys}"
            )

        # Extract the domain from each dictionary and flatten all results
        all_records = []
        for item_dict in data_dict:
            if domain in item_dict:
                domain_records = normalize_to_records(item_dict[domain])
                all_records.extend(domain_records)
        return all_records

    all_records = []
    for item_dict in data_dict:
        all_records.extend(normalize_to_records(item_dict))
    return all_records

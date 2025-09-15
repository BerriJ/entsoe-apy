from collections.abc import Iterable
from itertools import product


def is_iterable(obj) -> bool:
    return isinstance(obj, Iterable) and not isinstance(obj, (str, bytes))


def flatten_to_rows(obj) -> list[dict]:
    if hasattr(obj, "__dict__"):
        attr_items = list(vars(obj).items())
        values = []
        for key, value in attr_items:
            if is_iterable(value):
                nested = flatten_to_rows(value)
                values.append(nested)
            else:
                values.append([{key: value}])

        # Cartesian product of all attribute rows (dict merge)
        result = []
        for row in product(*values):
            merged = {}
            for d in row:
                merged.update(d)
            result.append(merged)
        return result
    elif is_iterable(obj):
        rows = []
        for item in obj:
            rows.extend(flatten_to_rows(item))
        return rows
    else:
        raise ValueError(
            "Object must be a dataclass instance or an iterable of such instances."
        )

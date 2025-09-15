from collections.abc import Iterable
from itertools import product


def is_iterable(obj) -> bool:
    return isinstance(obj, Iterable) and not isinstance(obj, (str, bytes))


def flatten_to_rows(obj) -> list[list]:
    if hasattr(obj, "__dict__"):
        values = []
        for value in vars(obj).values():
            if is_iterable(value):
                nested = []
                for item in value:
                    nested.extend(flatten_to_rows(item))
                values.append(nested)
            else:
                values.append([[value]])

        # Cartesian product of all attribute rows
        return [sum(row, []) for row in product(*values)]
    elif is_iterable(obj):
        rows = []
        for item in obj:
            rows.extend(flatten_to_rows(item))
        return rows
    else:
        return [[obj]]

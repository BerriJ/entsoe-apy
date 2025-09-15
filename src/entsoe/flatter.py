from dataclasses import dataclass, field
from itertools import product
from typing import Any, Callable


@dataclass
class Flatter:
    custom_encoders: dict[type, Callable[[str, Any], dict[str, Any]]] = field(
        default_factory=dict
    )

    def do(self, obj) -> list[dict]:
        if hasattr(obj, "__dict__"):
            attr_items = list(vars(obj).items())
            values = []
            for key, value in attr_items:
                if isinstance(value, tuple(self.custom_encoders.keys())):
                    first = next(
                        (
                            encoder
                            for type_, encoder in self.custom_encoders.items()
                            if isinstance(value, type_)
                        ),
                        None,
                    )

                    values.append([
                        {key_: value_} for key_, value_ in first(key, value).items()
                    ])
                elif isinstance(value, list):
                    nested = self.do(value)
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
        elif isinstance(obj, list):
            rows = []
            for item in obj:
                rows.extend(self.do(item))
            return rows
        else:
            raise ValueError(
                f"Object must be a dataclass instance or an iterable of such instances: {type(obj)}."
            )

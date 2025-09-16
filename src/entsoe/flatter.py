from dataclasses import dataclass, field
from itertools import product
from typing import Any, Callable


def _is_instance(obj, typ: type) -> bool:
    """Check if obj is an instance of typ, handling generics like list[int]."""
    origin = getattr(typ, "__origin__", None)
    if origin is not None:
        if not isinstance(obj, origin):
            return False

        args = getattr(typ, "__args__", ())
        if origin is list and len(args) == 1:
            return all(isinstance(item, args[0]) for item in obj)

        return False
    else:
        return isinstance(obj, typ)


@dataclass
class Flatter:
    custom_encoders: dict[type, Callable[[str, Any], dict[str, Any]]] = field(
        default_factory=dict
    )

    def first_custom_decoder(self, value: Any) -> Callable[[str, Any], dict[str, Any]]:
        return next(
            (
                encoder
                for typ, encoder in self.custom_encoders.items()
                if _is_instance(value, typ)
            ),
            None,
        )

    def do(self, obj) -> list[dict]:
        if hasattr(obj, "__dict__"):
            attr_items = list(vars(obj).items())
            values = []
            for key, value in attr_items:
                first = self.first_custom_decoder(value)
                if first is not None:
                    for key_, value_ in first(key, value).items():
                        values.append([{key_: value_}])
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

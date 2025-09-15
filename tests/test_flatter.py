from dataclasses import dataclass
from enum import Enum

from entsoe.flatter import Flatter


class _Enum(Enum):
    A = "A"
    B = "B"


@dataclass
class SubSubItem:
    x2: str
    y2: int
    z3: _Enum = _Enum.A


@dataclass
class SubItem:
    x: int
    y: list[SubSubItem]


@dataclass
class Item:
    a: int
    b: list[SubItem]


_MAIN = Item(
    1,
    [
        SubItem(10, [SubSubItem("1", 2), SubSubItem("5", 6)]),
        SubItem(30, [SubSubItem("3", 4)]),
    ],
)


def test_basic():
    result = Flatter().do(_MAIN)
    assert result[0] == {"a": 1, "x": 10, "x2": "1", "y2": 2, "z3": _Enum.A}
    assert result[1] == {"a": 1, "x": 10, "x2": "5", "y2": 6, "z3": _Enum.A}
    assert result[2] == {"a": 1, "x": 30, "x2": "3", "y2": 4, "z3": _Enum.A}


def test_list():
    result = Flatter().do([_MAIN, _MAIN])

    assert result[0] == {"a": 1, "x": 10, "x2": "1", "y2": 2, "z3": _Enum.A}
    assert result[1] == {"a": 1, "x": 10, "x2": "5", "y2": 6, "z3": _Enum.A}
    assert result[2] == {"a": 1, "x": 30, "x2": "3", "y2": 4, "z3": _Enum.A}
    assert result[3] == {"a": 1, "x": 10, "x2": "1", "y2": 2, "z3": _Enum.A}
    assert result[4] == {"a": 1, "x": 10, "x2": "5", "y2": 6, "z3": _Enum.A}
    assert result[5] == {"a": 1, "x": 30, "x2": "3", "y2": 4, "z3": _Enum.A}


def test_custom_encoder():
    result = Flatter(
        custom_encoders={
            int: lambda key, value: {key + " + 1": value + 1},
            _Enum: lambda key, value: {key: _Enum.B},
        }
    ).do(_MAIN)
    assert result[0] == {"a + 1": 2, "x + 1": 11, "x2": "1", "y2 + 1": 3, "z3": _Enum.B}
    assert result[1] == {"a + 1": 2, "x + 1": 11, "x2": "5", "y2 + 1": 7, "z3": _Enum.B}
    assert result[2] == {"a + 1": 2, "x + 1": 31, "x2": "3", "y2 + 1": 5, "z3": _Enum.B}

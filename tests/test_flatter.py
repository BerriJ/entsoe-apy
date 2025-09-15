from dataclasses import dataclass

from entsoe.flatter import Flatter


@dataclass
class SubSubItem:
    x2: str
    y2: int


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
    assert result[0] == {"a": 1, "x": 10, "x2": "1", "y2": 2}
    assert result[1] == {"a": 1, "x": 10, "x2": "5", "y2": 6}
    assert result[2] == {"a": 1, "x": 30, "x2": "3", "y2": 4}


def test_list():
    result = Flatter().do([_MAIN, _MAIN])

    assert result[0] == {"a": 1, "x": 10, "x2": "1", "y2": 2}
    assert result[1] == {"a": 1, "x": 10, "x2": "5", "y2": 6}
    assert result[2] == {"a": 1, "x": 30, "x2": "3", "y2": 4}
    assert result[3] == {"a": 1, "x": 10, "x2": "1", "y2": 2}
    assert result[4] == {"a": 1, "x": 10, "x2": "5", "y2": 6}
    assert result[5] == {"a": 1, "x": 30, "x2": "3", "y2": 4}


def test_custom_encoder():
    result = Flatter(custom_encoders={int: lambda v: v + 1}).do(_MAIN)
    assert result[0] == {"a": 2, "x": 11, "x2": "1", "y2": 3}
    assert result[1] == {"a": 2, "x": 11, "x2": "5", "y2": 7}
    assert result[2] == {"a": 2, "x": 31, "x2": "3", "y2": 5}

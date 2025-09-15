from dataclasses import dataclass

from entsoe.flatter import flatten_to_rows


@dataclass
class SubSubItem:
    x2: int
    y2: int


@dataclass
class SubItem:
    x: int
    y: list[SubSubItem]


@dataclass
class Item:
    a: int
    b: list[SubItem]


def test_():
    obj = Item(
        1,
        [
            SubItem(10, [SubSubItem(1, 2), SubSubItem(5, 6)]),
            SubItem(30, [SubSubItem(3, 4)]),
        ],
    )

    result = flatten_to_rows(obj)
    assert result[0] == {"a": 1, "x": 10, "x2": 1, "y2": 2}
    assert result[1] == {"a": 1, "x": 10, "x2": 5, "y2": 6}
    assert result[2] == {"a": 1, "x": 30, "x2": 3, "y2": 4}

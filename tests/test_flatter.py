from dataclasses import dataclass

from entsoe.flatter import flatten_to_rows


@dataclass
class SubSubItem:
    x: int
    y: int


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
    assert result[0] == [1, 10, 1, 2]
    assert result[1] == [1, 10, 5, 6]
    assert result[2] == [1, 30, 3, 4]

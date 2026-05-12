"""Unit tests for the normalize_to_records function."""

from entsoe.utils.records import normalize_to_records


def test_flat_dict():
    """Flat dict produces a single record."""
    data = {"a": 1, "b": "x"}
    result = normalize_to_records(data)
    assert result == [{"a": 1, "b": "x"}]


def test_nested_dict_flattened():
    """Nested dict is flattened with dot-notation keys."""
    data = {"a": {"b": 1, "c": 2}}
    result = normalize_to_records(data)
    assert result == [{"a.b": 1, "a.c": 2}]


def test_list_expands_to_multiple_records():
    """A top-level list field expands into one record per element."""
    data = {"name": "series", "points": [{"v": 1}, {"v": 2}, {"v": 3}]}
    result = normalize_to_records(data)
    assert len(result) == 3
    assert {"name": "series", "points.v": 1} in result
    assert {"name": "series", "points.v": 2} in result
    assert {"name": "series", "points.v": 3} in result


def test_nested_list_in_time_series_entry_not_dropped():
    """
    Nested list within a time_series entry must not silently drop data.

    This is the core regression case: a time_series entry that contains a
    nested list (e.g., production_registering_unit) must expand into multiple
    records — one per nested element — rather than silently losing all but one.
    """
    data = [
        {
            "period": "2020-01-01",
            "production_registering_unit": [
                {"name": "unit_a", "type": "solar"},
                {"name": "unit_b", "type": "wind"},
            ],
        }
    ]
    result = normalize_to_records(data)
    assert len(result) == 2, (
        "Expected one record per nested list element; nested data must not be dropped"
    )
    assert {
        "period": "2020-01-01",
        "production_registering_unit.name": "unit_a",
        "production_registering_unit.type": "solar",
    } in result
    assert {
        "period": "2020-01-01",
        "production_registering_unit.name": "unit_b",
        "production_registering_unit.type": "wind",
    } in result


def test_nested_dict_containing_list_produces_sub_records():
    """
    A dict field that itself contains a list must produce multiple sub-records.

    This covers the case raised in code review: a dict value that expands into
    more than one sub_record must be collected and cross-joined with the base
    fields, not silently discarded.
    """
    data = {
        "ts_id": "ts-1",
        "group": {
            "label": "g1",
            "items": [{"id": "a"}, {"id": "b"}],
        },
    }
    result = normalize_to_records(data)
    assert len(result) == 2, "Expected one record per element in the nested dict's list"
    assert {"ts_id": "ts-1", "group.label": "g1", "group.items.id": "a"} in result
    assert {"ts_id": "ts-1", "group.label": "g1", "group.items.id": "b"} in result


def test_cross_join_of_multiple_list_fields():
    """Multiple list fields at the same level are cross-joined."""
    data = {
        "colors": [{"c": "red"}, {"c": "blue"}],
        "sizes": [{"s": "S"}, {"s": "M"}],
    }
    result = normalize_to_records(data)
    assert len(result) == 4
    assert {"colors.c": "red", "sizes.s": "S"} in result
    assert {"colors.c": "red", "sizes.s": "M"} in result
    assert {"colors.c": "blue", "sizes.s": "S"} in result
    assert {"colors.c": "blue", "sizes.s": "M"} in result


def test_ignore_fields_removes_keys():
    """Fields listed in ignore_fields are excluded from all records."""
    data = {"m_rid": "secret", "value": 42, "points": [{"v": 1}, {"v": 2}]}
    result = normalize_to_records(data, ignore_fields=["m_rid"])
    assert all("m_rid" not in r for r in result)
    assert len(result) == 2


def test_primitive_list_elements():
    """A list of primitives (not dicts) creates one record per element."""
    data = {"tags": ["alpha", "beta", "gamma"]}
    result = normalize_to_records(data)
    assert len(result) == 3
    assert {"tags": "alpha"} in result
    assert {"tags": "beta"} in result
    assert {"tags": "gamma"} in result

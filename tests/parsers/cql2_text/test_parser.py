import datetime

from pygeofilter import ast
from pygeofilter.parsers.cql2_text import parse
from pygeofilter.values import Interval


def test_attribute_eq_true_uppercase():
    result = parse("attr = TRUE")
    assert result == ast.Equal(
        ast.Attribute("attr"),
        True,
    )


def test_attribute_eq_true_lowercase():
    result = parse("attr = true")
    assert result == ast.Equal(
        ast.Attribute("attr"),
        True,
    )


def test_attribute_eq_false_uppercase():
    result = parse("attr = FALSE")
    assert result == ast.Equal(
        ast.Attribute("attr"),
        False,
    )


def test_attribute_eq_false_lowercase():
    result = parse("attr = false")
    assert result == ast.Equal(
        ast.Attribute("attr"),
        False,
    )


def test_parse_temporal_filter():
    result = parse("T_AFTER(start_datetime,TIMESTAMP('2023-06-01T12:00:00.509000'))")
    assert result == ast.TimeAfter(
        ast.Attribute("start_datetime"), datetime.datetime(2023, 6, 1, 12, 0, 0, 509000)
    )


def test_parse_advanced_temporal_filter():
    result = parse(
        "T_CONTAINS(INTERVAL(start_datetime,end_datetime),INTERVAL(TIMESTAMP('2024-05-27T09:44:12.509000'),TIMESTAMP('2024-05-27T09:44:13.509000')))"
    )
    assert result == ast.TimeContains(
        Interval(
            start=ast.Attribute("start_datetime"), end=ast.Attribute("end_datetime")
        ),
        Interval(
            start=datetime.datetime(2024, 5, 27, 9, 44, 12, 509000),
            end=datetime.datetime(2024, 5, 27, 9, 44, 13, 509000),
        ),
    )

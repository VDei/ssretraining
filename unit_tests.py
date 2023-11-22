import pytest
import test3


def test_to_minutes():
    # Positive tests
    assert to_minutes(1) == 60
    assert to_minutes(1.5) == 90
    assert to_minutes(0.75) == 45
    assert to_minutes(0.25) == 15

    # Boundary values
    assert to_minutes(0) == 0
    assert to_minutes(-0.5) == -30

def test_to_hours():
    # Positive tests
    assert to_hours(60) == 1
    assert to_hours(45) == 0.75
    assert to_hours(15) == 0.25

    # Boundary values
    assert to_hours(0) == 0
    assert to_hours(-30) == -0.5

def test_is_whole_div():
    # Positive tests
    assert is_whole_div(10, 2) is True
    assert is_whole_div(10, 3) is False

    # Boundary values
    assert is_whole_div(0, 1) is True  # 0 ділиться на будь-яке число
    assert is_whole_div(1, 0) is False # Ділення на 0
    assert is_whole_div(0, 0) is False # Ділення 0 на 0

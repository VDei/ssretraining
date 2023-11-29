import pytest
from task3 import to_minutes, to_hours, is_whole_div

def test_to_minutes():
    assert to_minutes(1.5) == 90
    assert to_minutes(1) == 60
    assert to_minutes(0.5) == 30
    assert to_minutes(0) == 0
    assert to_minutes(-1) == -60

def test_to_hours():
    assert to_hours(12) == 0.2
    assert to_hours(60) == 1.0
    assert to_hours(75) == 1.25
    assert to_hours(0) == 0.0
    assert to_hours(-30) == -0.5

def test_is_whole_div():
    assert is_whole_div(2, 3) is False
    assert is_whole_div(12, 3) is True
    assert is_whole_div(5, 5) is True
    assert is_whole_div(0, 1) is True
    with pytest.raises(ZeroDivisionError):
        is_whole_div(1, 0)

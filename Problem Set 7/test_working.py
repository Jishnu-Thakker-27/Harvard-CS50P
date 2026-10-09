
import pytest
from working import convert


def test_valid_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"


def test_midnight_and_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12:30 AM to 12:45 PM") == "00:30 to 12:45"


def test_afternoon_and_overnight():
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"
    assert convert("11 PM to 1 AM") == "23:00 to 01:00"


def test_invalid_hours():
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")

    with pytest.raises(ValueError):
        convert("0 AM to 5 PM")


def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("12:60 AM to 5:00 PM")

    with pytest.raises(ValueError):
        convert("9:00 AM to 5:99 PM")


def test_invalid_formats():
    with pytest.raises(ValueError):
        convert("9:00AM to 5:00PM")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 PM extra")

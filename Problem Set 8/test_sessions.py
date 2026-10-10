
from datetime import date
from sessions import minutes_since_birth


def test_same_day():
    assert minutes_since_birth(
        date(2025, 1, 1), date(2025, 1, 1)
    ) == 0


def test_one_day():
    assert minutes_since_birth(
        date(2025, 1, 1), date(2025, 1, 2)
    ) == 1440


def test_one_year():
    assert minutes_since_birth(
        date(2001, 1, 1), date(2002, 1, 1)
    ) == 365 * 24 * 60


def test_leap_year():
    assert minutes_since_birth(
        date(2000, 1, 1), date(2001, 1, 1)
    ) == 366 * 24 * 60


def test_multiple_years():
    assert minutes_since_birth(
        date(2020, 1, 1), date(2023, 1, 1)
    ) == (366 + 365 + 365) * 24 * 60


import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0


def test_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar(2.5)

    with pytest.raises(ValueError):
        Jar("12")

    with pytest.raises(ValueError):
        Jar(True)


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

    jar.deposit(2)
    assert jar.size == 5


def test_deposit_exceeds_capacity():
    jar = Jar(3)
    jar.deposit(3)

    with pytest.raises(ValueError):
        jar.deposit(1)

    assert jar.size == 3


def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(2)

    assert jar.size == 2
    assert str(jar) == "🍪🍪"


def test_withdraw_too_many():
    jar = Jar(5)
    jar.deposit(2)

    with pytest.raises(ValueError):
        jar.withdraw(3)

    assert jar.size == 2


def test_invalid_cookie_counts():
    jar = Jar(5)

    for n in (-1, 2.5, "2", True):
        with pytest.raises(ValueError):
            jar.deposit(n)

        with pytest.raises(ValueError):
            jar.withdraw(n)


def test_zero_capacity():
    jar = Jar(0)
    assert jar.capacity == 0
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.deposit(1)


def test_zero_operations():
    jar = Jar(3)
    jar.deposit(2)
    jar.deposit(0)
    jar.withdraw(0)

    assert jar.size == 2

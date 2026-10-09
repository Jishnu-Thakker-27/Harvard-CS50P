
from numb3rs import validate


def test_valid_addresses():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("8.8.8.8") == True


def test_invalid_ranges():
    assert validate("256.1.1.1") == False
    assert validate("275.3.6.28") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.1.256") == False


def test_invalid_formats():
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("cat.dog.bird.fish") == False
    assert validate("192.168.1") == False


def test_empty_and_missing_parts():
    assert validate("") == False
    assert validate("1.2..4") == False
    assert validate(".1.2.3") == False
    assert validate("1.2.3.") == False

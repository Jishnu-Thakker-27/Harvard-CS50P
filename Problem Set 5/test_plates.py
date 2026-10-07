from plates import is_valid


def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("ABC") == True
    assert is_valid("HELLO") == True


def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_first_two_characters():
    assert is_valid("50CS") == False
    assert is_valid("5CS50") == False


def test_numbers():
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("CS50") == True


def test_punctuation():
    assert is_valid("CS-50") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS.50") == False
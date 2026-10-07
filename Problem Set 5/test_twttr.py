from twttr import shorten


def test_lowercase():
    assert shorten("hello") == "hll"


def test_uppercase():
    assert shorten("HELLO") == "HLL"


def test_mixed_case():
    assert shorten("Hello World") == "Hll Wrld"


def test_numbers():
    assert shorten("CS50") == "CS50"


def test_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"
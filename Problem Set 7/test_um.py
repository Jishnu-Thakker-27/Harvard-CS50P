
from um import count


def test_basic():
    assert count("hello, um, world") == 1
    assert count("um um um") == 3
    assert count("hello world") == 0


def test_case_insensitive():
    assert count("UM Um uM um") == 4
    assert count("I think, UM, this works") == 1


def test_word_boundaries():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("album") == 0
    assert count("umami") == 0


def test_punctuation():
    assert count("um, um! (um?)") == 3
    assert count("um.um;um") == 3


def test_empty_string():
    assert count("") == 0

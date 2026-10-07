from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0


def test_h():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("How are you?") == 20


def test_other():
    assert value("good morning") == 100
    assert value("What's up?") == 100
    assert value("Good evening") == 100


def test_hello_with_extra_text():
    assert value("hello there") == 0
    assert value("Hello, how are you?") == 0
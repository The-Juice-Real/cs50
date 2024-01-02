from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_h_start():
    assert value("hi") == 20
    assert value("How are you?") == 20

def test_no_h():
    assert value("Fuck you") == 100
    assert value("shut up") == 100

def test_corners():
    assert value("100") == 100
    assert value("!hey") == 100
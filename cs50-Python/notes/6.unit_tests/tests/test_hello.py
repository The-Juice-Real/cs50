from hello import hello

def test_hello():
    assert hello("Tom") == "hello, Tom"

def test_argument():
    assert hello() == "hello, world"
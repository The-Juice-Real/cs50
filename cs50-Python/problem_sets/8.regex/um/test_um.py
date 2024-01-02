from um import count

def test_lone_um():
    assert count("hello um world") == 1
    assert count("Hello um um world") == 2

def test_quote_dot_um():
    assert count("hello, um, world") == 1
    assert count("Eyy, um...") == 1
    assert count("um... um....") == 2
    assert count("Um... um? (um)") == 3

def test_fullword():
    assert count("Opium") == 0
    assert count("Um... um") == 2


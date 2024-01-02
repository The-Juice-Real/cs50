from jar import Jar
import pytest
import re

def test_init():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar(0.5)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(12)
    with pytest.raises(ValueError):
        jar.deposit(13)


def test_withdraw():
    jar = Jar(12)
    with pytest.raises(ValueError):
        jar.withdraw(1)
    
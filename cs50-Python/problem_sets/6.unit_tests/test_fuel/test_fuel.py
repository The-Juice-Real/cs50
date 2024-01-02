import pytest

from fuel import convert, gauge

def test_convert():
    assert convert("1/100") == 1
    assert convert("1/3") == 33
    assert convert("1/1") == 100

def test_ValueError():
    with pytest.raises(ValueError):
        convert("1.5/3")


def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"






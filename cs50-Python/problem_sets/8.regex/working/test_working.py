import pytest
from working import convert


def test_errors():
    with pytest.raises(ValueError):
        convert("5:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("5 to 6")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("13:00 AM to 16:00 PM")


def test_correct():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"
    assert convert("1 AM to 1 AM") == "01:00 to 01:00"
    assert convert("1 PM to 1 PM") == "13:00 to 13:00"
    assert convert("9:10 PM to 5:45 AM") == "21:10 to 05:45"

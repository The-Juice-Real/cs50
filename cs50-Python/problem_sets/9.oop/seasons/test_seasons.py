from seasons import convert
from seasons import to_words
import pytest


def test_convert():
    assert convert("2001-09-26") == (2001, 9, 26)
    with pytest.raises(SystemExit):
        convert("cat")
    with pytest.raises(SystemExit):
        convert("2000")
    with pytest.raises(SystemExit):
        convert("2000-13-20")
    with pytest.raises(SystemExit):
        convert("2000-12-32")
    with pytest.raises(SystemExit):
        convert("20000-10-10")

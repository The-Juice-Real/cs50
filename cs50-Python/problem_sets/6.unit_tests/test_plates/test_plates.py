from plates import is_valid

def test_one_letter():
    assert is_valid("a") == False
    assert is_valid("1") == False

def test_two_letters():
    assert is_valid("NF") == True
    assert is_valid("N1") == False
    assert is_valid("1N") == False
    assert is_valid("11") == False

def test_six_letters():
    assert is_valid("AAAAAA") == True
    assert is_valid("999999") == False
    assert is_valid("AA9AA") == False
    assert is_valid("AA999") == True
    assert is_valid("0000") == False
    assert is_valid("AA0000") == False

def test_corners():
    assert is_valid("!fuck") == False
    assert is_valid("KS.IFL") == False
    assert is_valid("K S I") == False

def test_over_six():
    assert is_valid("AAAAAAA") == False
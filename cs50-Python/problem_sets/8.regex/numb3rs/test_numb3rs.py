from numb3rs import validate

def test_letters():
    assert validate("a.b.c.d") == False
    assert validate("cat") == False

def test_out_of_range():
    assert validate("256.256.256.256") == False
    assert validate("-1.-1.-1.-1") == False

def test_floats():
    assert validate("2,5.2,5.2,5.2,5") == False
    assert validate("1.1.1.1.1") == False

def test_correct():
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("255.7.1.10") == True

def test_missing():
    assert validate("10.2750.2570.2750") == False
    assert validate("1.") == False
    assert validate("1.1") == False
    assert validate("1.1.") == False
    assert validate("1.1.1") == False
    assert validate("1.1.1.") == False
    assert validate("275.3.6.28") == False

def test_misc():
    assert validate("1.2.3.1000") == False
    assert validate("1.2.3000.1") == False
    assert validate("1.2000.3.1") == False
    assert validate("1000.2.3.1") == False
    assert validate("199.911.288.882") == False
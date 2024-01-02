from twttr import shorten

def test_shorten():
    assert shorten("Harry Potter") == "Hrry Pttr"
    assert shorten("twitter") == "twttr"



def test_vowel_first():
    assert shorten("A huge booty") == " hg bty"

def test_numbers():
    assert shorten("CS50") == "CS50"
    assert shorten("247 Service") == "247 Srvc"

def test_punctuations():
    assert shorten("?,.<>:;'^!") == "?,.<>:;'^!"
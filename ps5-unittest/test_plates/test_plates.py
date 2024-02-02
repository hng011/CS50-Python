from plates import is_valid

def test_correct_format():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("YO") == True

def test_incorrect_format():
    assert is_valid("F") == False
    assert is_valid("PP300PP") == False
    assert is_valid("HNG000") == False
    assert is_valid("CS50P") == False
    assert is_valid("fo.bar") == False
    assert is_valid("99") == False
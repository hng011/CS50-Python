from numb3rs import validate

def test_valid():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.4") == True
    assert validate("11.22.33.44") == True

def test_invalid():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("1.256.256.256") == False

from working import convert
from pytest import raises

def test_with_minute():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 08:50 AM") == "22:30 to 08:50"

def test_value_err():
    with raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_err_format():
    with raises(ValueError):
        convert("9:00 PM - 9:32 AM")

def test_12():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 00:00 AM") == "12:00 to 00:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
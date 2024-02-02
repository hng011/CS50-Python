from fuel import convert, gauge
from pytest import raises

def test_convert():
    assert convert("5/6") == 83
    assert convert("4/4") == 100

    with raises(ValueError):
        convert("2/1")
    with raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(98) == "98%"
    assert gauge(1) == "E"
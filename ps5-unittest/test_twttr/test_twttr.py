from twttr import shorten

def test_string():
    assert shorten("Hello, World") == "Hll, Wrld"

def test_num():
    assert shorten("12345") == "12345"

def test_mix():
    assert shorten("Hell00, WO0rlD.") == "Hll00, W0rlD."
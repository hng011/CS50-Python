from bank import value

def test_greeting():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0

def test_only_h():
    assert value("How you doing?") == 20

def no_greeting():
    assert value("What's up?") == 100
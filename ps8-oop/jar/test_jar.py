from jar import Jar
from pytest import raises

def test_init():
    jar = Jar(capacity=3)
    assert jar.size == 0

    with raises(ValueError):
        jar = Jar(capacity=-1)

def test_str():
    jar = Jar(10)
    assert str(jar) == ""

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    assert jar.capacity == 7
    assert jar.size == 3
    
    jar.deposit(3) 
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"
    assert jar.capacity == 4

def test_deposit():
    with raises(ValueError):
        jar = Jar(capacity=3).deposit(4)

    jar = Jar(capacity=3)
    jar.deposit(2)
    assert jar.size == 2

def test_withdraw():
    with raises(ValueError):
        jar = Jar(capacity=0).withdraw(1)

    jar = Jar(capacity=3)
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.size == 1

    jar.withdraw(1)
    assert jar.size == 0
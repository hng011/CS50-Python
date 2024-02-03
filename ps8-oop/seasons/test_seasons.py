from seasons import Seasons
from pytest import raises

def test_fail():
    with raises(SystemExit):
        Seasons("2000/10/21").get_minutes_of_life()
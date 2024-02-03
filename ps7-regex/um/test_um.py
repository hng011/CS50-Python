from um import count

def test_valid():
    assert count("um") == 1

def test_with_symbol():
    assert count("um?") == 1

def test_mix():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um..., Um, thanks, album... um instrument umbrella,um") == 5
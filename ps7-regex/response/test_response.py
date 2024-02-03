from response import email_validator

def test_valid():
    assert email_validator("malan@harvard.edu") == "Valid"
    assert email_validator("test.test@gunadarma.ac.id") == "Valid"

def test_invalid():
    assert email_validator("malan@@@harvard.edu") == "Invalid"
    assert email_validator("test.test@gunadarma.ac..id") == "Invalid"
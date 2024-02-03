import validators

def email_validator(s:str) -> str:
    return "Valid" if validators.email(s.lower().strip()) else "Invalid"

def main() -> any:
    print(email_validator(input("What's your email address? ")))

if __name__ == "__main__":
    main()
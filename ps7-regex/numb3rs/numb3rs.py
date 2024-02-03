import re

def main() -> any:
    print(validate(input("IPv4 Address: ")))

def validate(ip:str=0) -> bool:
    ipv4 = r"([0-9]|([0-9][0-9])|([1][0-9][0-9])|([2][0-5][0-5])|([2][0-4][0-9]))"
    return True if re.search(r"^" + ipv4 + r"\." + ipv4 + r"\." + ipv4 + r"\." + ipv4 + r"$", ip.strip()) else False

if __name__ == "__main__":
    main()
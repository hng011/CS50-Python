import re

def main():
    print(count(input("Text: ")))

def count(s) -> int:
   total_um = re.findall(r"\bum\b", s, flags=re.IGNORECASE)
   print(total_um)
   return len(total_um)

if __name__ == "__main__":
    main()
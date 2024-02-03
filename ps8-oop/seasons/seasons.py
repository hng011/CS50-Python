from datetime import date
import inflect
import sys
import re

class Seasons:
    def __init__(self, birthDate):
        try:
            self.__birthDate = date.fromisoformat(birthDate)
        except:
            sys.exit("Invalid Format")

    def get_minutes_of_life(self) -> int:
        if date_minutes := re.search(r"^([\d]+\b)", str(((date.today() - self.__birthDate)*24)*60)):
            return int(date_minutes.group(1))

    def minutes_to_words(self) -> str:
        p = inflect.engine()
        return f"{p.number_to_words(self.get_minutes_of_life(), andword='').capitalize()} minutes"   

def get_minutes(s:str) -> str:
    return Seasons(s).minutes_to_words()

def main() -> any:
    print(get_minutes(input("Birth Date: ")))

if __name__ == "__main__":
    main()
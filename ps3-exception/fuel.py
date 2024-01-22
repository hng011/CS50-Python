def to_percentage() -> str:
    res = 0
    while True:
        try:
            x,y = input("Fraction: ").split("/")
            res = int(x)/int(y)*100
            if res > 100:
                pass
            elif res >= 99:
                return "F"
            elif res <= 1:
                return "E"
            else:
                return f"{res:.0f}%"
        except (ValueError, TypeError, ZeroDivisionError) as e:
            pass

def main() -> None:
    print(to_percentage())

main()

def main() -> None:
    print(meal_time(input("What time is it? ")))

def meal_time(x:str) -> str:
    h = convert(x)
    if h > 6 and h < 9:
        return "breakfast time"
    elif h > 11 and h < 14:
        return "lunch time"
    elif h > 17 and h < 20:
        return "dinner time"
    else:
        return ""

def convert(time:str) -> float:
    try:
        h, m = time.split(":")
        h = float(h)
        m = float(m)
        if m > 59:
            h += 1
            m -= 60
        return h+(m/60)
    except:
        print("Invalid Format")
        return 0.0

if __name__ == "__main__":
    main()
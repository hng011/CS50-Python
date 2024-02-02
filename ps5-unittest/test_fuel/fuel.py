import sys
# def to_percentage() -> str:
#     res = 0
#     while True:
#         try:
#             x,y = input("Fraction: ").split("/")
#             res = int(x)/int(y)*100
#             if res > 100:
#                 pass
#             elif res >= 99:
#                 return "F"
#             elif res <= 1:
#                 return "E"
#             else:
#                 return f"{res:.0f}%"
#         except (ValueError, TypeError, ZeroDivisionError) as e:
#             pass

def convert(fraction: str) -> float:
    while True:
        try:    
            x,y = fraction.split("/")
            res = round(float(x)/float(y)*100)
            if res > 100:
                raise ValueError
            else:
                return res
        except (ValueError, ZeroDivisionError, TypeError):
            fraction = input("Fraction: ")

def gauge(percentage: float) -> str:
    if percentage > 100:
        pass
    elif percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage:.0f}%"

def main() -> any:
    print(gauge(convert(input("Fraction: "))))

if __name__ == "__main__":
    main()

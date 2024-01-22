menus = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def place_order(data:dict) -> any:
    total = 0
    while True:
        try:
            data = {k.lower():v for k, v in data.items()}
            inp=input("Input: ").lower()
            if inp in data.keys():
                total += data[inp]
                print(f"Total: ${total:.2f}")
        except EOFError: #handle ctrl-D
            return 0
        except KeyError:
            pass

place_order(data=menus)
import inflect

def print_res(names:list) -> str:
    p = inflect.engine()
    return p.join(names)

def adieu() -> any:
    names = []
    try:
        while True:
            names.append(input("Name: "))
    except EOFError:
        pass
    finally:
        return f"\nAdieu, adieu, to {print_res(names)}"
        
print(adieu())
def is_greeted(x:str) -> int:
    x=x.lower()
    if "hello" in x:
        return 0
    elif x[0] == "h":
        return 20
    else:
        return 100

print(f"${is_greeted(input('Greeting: '))}")
def value(x:str) -> int:
    x=x.lower()
    if "hello" in x:
        return 0
    elif x[0] == "h":
        return 20
    else:
        return 100
        
if __name__ == "__main__":
    print(f"${value(input('Greeting: '))}")
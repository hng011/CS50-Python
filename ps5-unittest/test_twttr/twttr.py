def shorten(x:str) -> str:
    res = ""
    for c in x:
        if c.lower() in ('a','i','u','e','o'):
            continue
        res += c
    return res

if __name__ == "__main__":
    print(shorten(input("input: ")))
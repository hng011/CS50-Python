def remove_vowels(x:str) -> str:
    res = ""
    for c in x:
        if c.lower() in ('a','i','u','e','o'):
            continue
        res += c
    return res

print(remove_vowels(input("input: ")))
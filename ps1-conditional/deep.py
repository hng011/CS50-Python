def is_fortytwo(x:str) -> str:
    return "Yes" if("42" in x or ("forty" and "two" in x.lower())) else "No"

print(is_fortytwo(input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")))
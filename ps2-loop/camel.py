def to_snake(x:str) -> str:
    res = ""
    for y in x:
        if y.isupper(): 
            res += "_"
        res += y
    return res.lower()    
    
print("snake_case:",to_snake(input("camelCase: ")))
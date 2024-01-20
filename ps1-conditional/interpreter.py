def interpreter(exp:str) -> any:
    try:
        x, y, z = exp.split(" ")
        ops = {
            '+': lambda x,y: x+y,
            '-': lambda x,y: x-y,
            '*': lambda x,y: x*y,
            '/': lambda x,y: x/y,
        }
        return float(ops[y](int(x),int(z)))
    except:
        return "Invalid Expression" 

print(interpreter(input("Expression: ")))
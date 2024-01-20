def convert(x:str) -> str:
    return x.replace(":)", "🙂").replace(":(", "🙁")

print(convert(input()))
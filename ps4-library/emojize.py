import emoji 

def replace_emojis(x:str) -> str:
    return emoji.emojize(x, language="alias")

print("Output:",replace_emojis(input("Input: ")))
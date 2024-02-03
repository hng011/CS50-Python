import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    try:
        link = re.findall(r"src=.+/embed/.+\"", s)[0].split(" ")[0].split("/")[-1].replace('"','')
        return f"https://youtu.be/{link}"
    except:
        return None
    
if __name__ == "__main__":
    main()
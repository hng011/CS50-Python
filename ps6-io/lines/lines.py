import sys

def get_arg() -> str:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")
    else:
        return sys.argv[1]

def count_file_rows(file:str) -> int:
    counter = 0
    try:
        with open(file, "r") as f:
            for line in [line.strip() for line in f.readlines()]:
                if line.startswith("#") or len(line) == 0: continue
                counter += 1
        return counter
    except FileNotFoundError:
        sys.exit("File does not exist")

def main():
    print(count_file_rows(get_arg()))

main()
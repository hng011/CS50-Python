import sys, csv
from tabulate import tabulate

def get_arg() -> str:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    else:
        return sys.argv[1]

def get_file(arg:str) -> list:
    df = [] 
    try:
        with open(arg, "r") as f:
            for row in csv.reader(f):
                df.append(row)   
    except FileNotFoundError:
        sys.exit("File does not exist")    
    
    return df

def show_data(data:list) -> tabulate:
    return tabulate(data[1:], headers=data[0], tablefmt="grid")

def main():
    print(show_data(get_file(get_arg())))

main()
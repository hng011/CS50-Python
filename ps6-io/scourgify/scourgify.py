import sys, csv

def get_arg() -> tuple:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    else:
        return (sys.argv[1], sys.argv[2])
    
def modify_file(first_arg:str) -> list:
    df = []
    try:
        with open(first_arg, "r") as f:
            for row in csv.DictReader(f):
                l, f = row["name"].split(",")
                df.append({"first": f.strip(), "last": l.strip(), "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {first_arg}")
    
    return df

def store_data(data:list, second_arg:str):
    headers = data[0].keys()
    try:
        with open(second_arg, "w") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        sys.exit(f"Error messages: {e}")

def main():
    file_names = get_arg()
    data = modify_file(file_names[0])
    
    # Store file
    store_data(data, file_names[1])

main()
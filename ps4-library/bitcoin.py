import requests, sys

def btc_to_dollar(btc:int=0) -> float:
    try:
        endpoint = "https://api.coindesk.com/v1/bpi/currentprice.json"
        res = requests.get(endpoint).json()["bpi"]["USD"]["rate_float"] * btc 
        return res
    except requests.RequestException as e:
        print(e)

def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    
    try:
        btc = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    
    return f"${btc_to_dollar(btc):,.4f}"

print(main())
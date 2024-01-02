import sys
import requests
import json


try:
    btcn = float(sys.argv[1])
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too much shit bruh")
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    btc_data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    btc_rate = btc_data["bpi"]["USD"]["rate"]
except requests.RequestException:
    sys.exit("something's wrong with requests")

fst, snd = btc_rate.split(sep = ",")

btc_rate_pure = float(fst + snd)

total = btc_rate_pure * btcn

print(f"${total:,.4f}")




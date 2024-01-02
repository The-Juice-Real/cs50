import sys
import requests
import json

if len(sys.argv) != 3:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=" + sys.argv[2] + "&term=" + sys.argv[1]).json()
results = response["results"]

for result in results:
    print(result["trackName"])
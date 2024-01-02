import re
import sys

url = input("URL: ").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)", url, re.IGNORECASE):
    username = matches.group(1)
else:
    sys.exit("Invalid")



print(username)
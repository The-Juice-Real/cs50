import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")

#re.match - pretty much the same as re.search except you don't need the ^ at the beginning, it matches from the start automatically
#re.fullmatch - auto ^ and $
else:
    print("Invalid")
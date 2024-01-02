from pyfiglet import Figlet
import sys
from random import choice

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts:
            font_choice = sys.argv[2]
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("invalid usage")

elif len(sys.argv) == 1:
    font_choice = choice(fonts)
else:
    sys.exit("Invalid usage")

figlet.setFont(font=font_choice)
user_input = input("Input: ")
print(figlet.renderText(user_input))
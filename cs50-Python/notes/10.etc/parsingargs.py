import argparse

parser = argparse.ArgumentParser(description="Choose your path")
parser.add_argument("-w", default=0, help="What week? (0 - 10)", type=int)
parser.add_argument("-m", default="l", help="l for lecture, ps for problem set", type=str)
args = parser.parse_args()

week = args.w
mode = args.m


match week:
    case 0|1|2|3|4|5|6|7|8|9|10:
        print(f"Week {week}")
    case _:
        print("Invalid week")

if mode == "l":
    print("lecture")
elif mode == "ps":
    print("problem set")
elif mode == None:
    pass
else:
    print("Invalid mode")
import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    matches = re.fullmatch(r"([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)", ip)
    i = 1
    while i <= 4:
        try:
            if int(matches.group(i)) <= 255:
                i += 1
            else:
                return False
        except:
            return False

    return True



if __name__ == "__main__":
    main()
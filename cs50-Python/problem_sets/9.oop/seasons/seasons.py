from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    answer = input("Date of birth: ").strip()
    year, month, day = convert(answer)

    birth_date = date(year, month, day)
    current_date = date.today()

    time_elapsed = current_date - birth_date

    words = to_words(time_elapsed).capitalize()
    print(f"{words} minutes")



def convert(date):
    if matches := re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", date):
        s_year, s_month, s_day = matches.groups()
        y = int(s_year)
        m = int(s_month)
        d = int(s_day)
    else:
        sys.exit("Invalid date")

    if m > 12 or d > 31:
        sys.exit("Invalid date")

    return y, m, d

def to_words(delta):
    minutes = delta.days * 24 * 60
    words = p.number_to_words(minutes, andword = "")
    return words



if __name__ == "__main__":
    main()

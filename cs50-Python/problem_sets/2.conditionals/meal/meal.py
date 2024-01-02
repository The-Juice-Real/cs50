def main():
    userinput = input("What time is it? ##:## format: ").strip().lower()
    timevalue = convert(userinput)

    if timevalue >= 7 and timevalue <= 8:
        print("breakfast time")

    elif timevalue >= 12 and timevalue <= 13:
        print("lunch time")

    elif timevalue >= 18 and timevalue <= 19:
        print("dinner time")



def convert(time):
        a, b = time.split(":")
        hour = float(a)
        minute = float(b)/60
        return hour + minute


if __name__ == "__main__":
    main()
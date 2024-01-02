import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    matches = re.search(
        r"^([0-9]{1,2}(?::[0-9]{2})?) (AM|PM) to ([0-9]{1,2}(?::[0-9]{2})?) (AM|PM)$", s
    )
    if matches:
        start_time, start_mode, end_time, end_mode = matches.groups()
        converted_start = convert_time(start_time, start_mode)
        converted_end = convert_time(end_time, end_mode)

        return f"{converted_start} to {converted_end}"
    else:
        raise ValueError


def convert_time(time, mode):
    if re.search(r"[0-9]{1,2}:[0-9]{2}", time):
        hour_str, minute_str = time.split(sep=":")
        hour = int(hour_str)

    else:
        hour = int(time)
        minute_str = "00"

    if hour > 12 or int(minute_str) >= 60:
        raise ValueError

    if mode == "AM":
        hour = hour
    else:
        hour = hour + 12

    if mode == "AM" and hour == 12:
        hour = 0
    elif mode == "PM" and hour == 24:
        hour = 12

    if hour < 10:
        hour_str = f"0{hour}"
    else:
        hour_str = hour

    return f"{hour_str}:{minute_str}"


if __name__ == "__main__":
    main()

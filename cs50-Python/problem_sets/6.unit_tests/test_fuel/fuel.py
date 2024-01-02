def main():
    fraction = input("Fraction: ").strip()
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    xs, ys = fraction.split(sep = "/")
    try:
        x = int(xs)
        y = int(ys)
    except ValueError:
        raise ValueError
    if x < 0 or y < 0:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError
    else:
        return round(x * 100 / y)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()
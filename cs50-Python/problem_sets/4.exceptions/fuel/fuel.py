def main():
    fraction = get_fraction("What's the fraction on your fuel?")
    fuel_amount = fraction_to_percent(fraction)
    print(fuel_amount)



def get_fraction(prompt):
    while True:
        try:
            rawinput = input(prompt).strip()
            a, b = rawinput.split(sep = "/")
            x = int(a)
            y = int(b)
            the_fraction = x/y
        except ValueError:
            print("Either x or y is not an integer")
        except ZeroDivisionError:
            print("Cannot divide by zero")
        else:
            if x > y:
                print("x cannot be more than y")
                continue
            else:
                return the_fraction


def fraction_to_percent(a_fraction):
    percent = a_fraction * 100
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{round(percent)}%"



main()
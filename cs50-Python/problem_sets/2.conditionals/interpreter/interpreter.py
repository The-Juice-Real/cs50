def main():
    equation = input("What's the equation bro?")

    fn, y, sn = equation.split()

    x = float(fn)
    z = float(sn)

    print(round(calculation(x, y, z), 1))


def calculation(a, o, b):
    match o:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b if b != 0 else "can't divide by 0"
        case _:
            return "invalid operator"

main()
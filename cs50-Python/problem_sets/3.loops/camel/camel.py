def main():
    raw_var_name = input("What's the variable name?").strip()
    print(to_snake_case(raw_var_name))


def to_snake_case(var_name):
    snake_case = ""
    for letter in var_name:
        if letter.isupper():
            letter = f"_{letter.lower()}"
        snake_case = snake_case + letter
    return snake_case

main()
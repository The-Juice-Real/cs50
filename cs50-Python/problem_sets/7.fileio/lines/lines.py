import sys


def main():
    file_name = get_name()
    lines = count_lines(file_name)
    print(lines)


def get_name():
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        # checking validity of the name
        try:
            check, py = file_name.split(sep=".")
            if py != "py":
                raise ValueError
        except:
            sys.exit("Not a Python file")

        return file_name
    elif len(sys.argv < 2):
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def count_lines(file_name):
    try:
        with open(file_name, "r") as code:
            i = 0
            for line in code:
                # check if line is blank or comment
                if line.strip() != "" and line.strip()[0] != "#":
                    i += 1
                else:
                    continue

    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        return i


if __name__ == "__main__":
    main()

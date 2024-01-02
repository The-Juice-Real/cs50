from tabulate import tabulate
import sys
import csv

def main():
    file_name = get_name()
    table = tabulator(file_name)
    print(table)


def get_name():
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        # checking validity of the name
        try:
            check, csv = file_name.split(sep=".")
            if csv != "csv":
                raise ValueError
        except:
            sys.exit("Not a CSV file")

        return file_name
    elif len(sys.argv < 2):
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def tabulator(file_name):
    menu_raw = []
    try:
        with open(file_name, "r") as menu:
            reader = csv.reader(menu)
            for line in reader:
                menu_raw.append(line)

    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        return tabulate(menu_raw, headers = "firstrow", tablefmt="grid")

if __name__ == "__main__":
    main()
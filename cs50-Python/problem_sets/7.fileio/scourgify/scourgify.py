import csv
import sys


def main():
    dirty_name, clean_name = get_names()
    dirty_list = dirty_read(dirty_name)
    clean_dirty_data(dirty_list, clean_name)


def get_names():
    if len(sys.argv) == 3:
        dirty_name = sys.argv[1]
        clean_name = sys.argv[2]
        # checking validity of the name
        dirty_split = dirty_name.split(sep=".")
        clean_split = clean_name.split(sep=".")

        if dirty_split[-1] != "csv" and clean_split[-1] != "csv":
            sys.exit("Not csv file(s)")

        return dirty_name, clean_name

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def dirty_read(dirty_name):
    dirty_list = []
    try:
        with open(dirty_name, "r") as file:
            reader = csv.reader(file, quotechar="`")
            for row in reader:
                try:
                    dirty_list.append([row[0].strip('" '), row[1].strip('" '), row[2]])
                except:
                    continue
    except FileNotFoundError:
        sys.exit(f"Could not read {dirty_name}")
    else:
        return dirty_list


def clean_dirty_data(dirty_list, clean_name):
    with open(clean_name, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first","last","house"])
        writer.writeheader()
        for line in dirty_list:
            writer.writerow({"first" : line[1], "last" : line[0], "house" : line[2]})
            

if __name__ == "__main__":
    main()
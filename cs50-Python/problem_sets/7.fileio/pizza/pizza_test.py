import csv

menu_raw = []

with open("regular.csv") as menu:
    reader = csv.reader(menu)
    for line in reader:
        menu_raw.append(line)

print(menu_raw)
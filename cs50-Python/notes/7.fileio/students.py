import csv

with open("students.csv") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)

import csv

def check_performance():
    weeks = {str(i): [] for i in range(11)}

    with open("sorted_time.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            weeks[row["Week"]].append(row["Time"])

    with open("time_stats.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames = ["Week", "Start Time"])
        writer.writeheader()
        for i in range(len(weeks)):
            times = weeks[f"{i}"]
            try:
                writer.writerow({"Week": i, "Start Time": times[0]})
            except:
                pass
    
    with open("time_stats.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

            





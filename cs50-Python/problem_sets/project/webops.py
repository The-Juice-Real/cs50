import webbrowser
import csv
import datetime
import re
import os


def openweb(url):
    webbrowser.open(url)
    open_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if matches := re.search(r"2023/(.*)/(.*)", url):
        mode, week = matches.groups()
    time_handler(open_time, mode, week)
    time_delta_measurer()


def time_handler(time, mode, week):
    if os.path.exists("time.csv") == False:
        with open("time.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Week", "Mode", "Time"])
            writer.writeheader()
            writer.writerow({"Week": week, "Mode": mode, "Time": time})
    else:
        with open("time.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Week", "Mode", "Time"])
            writer.writerow({"Week": week, "Mode": mode, "Time": time})
 
def time_delta_measurer():
    with open("time.csv", "r") as file:
        reader = csv.DictReader(file)
        sorted_rows = sorted(reader, key=lambda row: row['Week'])
        #Get the first value of week and last value of week
        with open("sorted_time.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Week", "Mode", "Time"]) 
            writer.writeheader()
            for row in sorted_rows:
                writer.writerow(row)

import csv


class Week:
    def __init__(self, mode_raw, number):
        week = []
        mode = ""
        with open("info_x.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                week.append(row)

        self.info = week[number]
        match mode_raw:
            case "l" | "lec" | "weeks" | "week" | "w":
                mode = "weeks"
            case "s" | "sec" | "sections":
                mode = "sections"
            case "pp" | "practice" | "problems":
                mode = "problems"
            case "lb" | "lab" | "labs":
                mode = "labs"
            case "ps" | "pset" | "psets":
                mode = "psets"
            case "se" | "sem" | "seminar" | "seminars":
                mode = "seminars"
            case "f" | "fp" | "final" | "project":
                mode = "project"
            case None:
                mode = None

        try:
            if week[number][mode] == "TRUE":
                self.mode = mode
        except:
            pass

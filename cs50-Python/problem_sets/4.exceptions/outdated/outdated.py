months = {"January" :1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}

def main():
    month_str, day, year = get_date("Date: ")
    converted_date = convert_date(month_str, day, year)
    print(converted_date)

def get_date(prompt):
    while True:
        try:
            raw_date = input(prompt).strip()
            if raw_date[0].isdigit():
                month_str, day_str, year_str = raw_date.split(sep = "/")
                month = int(month_str)
                if month > 12:
                    print("Month can't be more than 12")
                    intentional_error = int("hell yeah")
            elif raw_date[0].isalpha():
                monthandday_str, year_str = raw_date.split(sep = ",")
                month_str, day_str = monthandday_str.split(sep = " ")
            day = int(day_str)

        except:
            print("invalid argument")
        else:
            if day > 31:
                print("day cannot be more than 31")
            else:
                return month_str, day, int(year_str)


def convert_date(month_str, day, year):
    if month_str in months:
        month = months[month_str]
    else:
        month = int(month_str)

    return f"{year}-{month:02}-{day:02}"





main()
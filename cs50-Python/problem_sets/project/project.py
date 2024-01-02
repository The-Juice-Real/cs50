import sys
from week import Week
from webops import openweb
from time_stats import check_performance

def main():
    start_state = get_state(sys.argv)
    link = handle_states(start_state, sys.argv)
    try:
        openweb(link)
    except:
        print("Not fetching link. Assuming stat check.")


def get_state(args):
    match len(args):
        case 1:
            return "menu"
        case 2:
            return case_two(args[1])
        case 3:
            return "execute"
        case _:
            return "invalid"
        
    
def case_two(value):
    try:
        int_check = int(value)
    except ValueError:
        if value == "stat":
            return "stat"
        else:
            sys.exit("invalid command")
    else:
        return "week check"
    
def handle_states(state, args):
    match state:
        case "menu":
            print("weeks:")
            for n in range(11):
                print(n, end = " ")
            print("\n\nother commands: \nstat")
            try:
                week_no = int(input("Choose: "))
                mode = check_week(Week(None,week_no))
            except:
                check_performance()
            else:
                return get_link(None, mode, week_no)

        case "week check":
            mode = check_week(Week(None,int(args[1])))
            return get_link(None, mode, args[1])
        case "execute":
            link = get_link(None, args[1], args[2])
            return link
        case "stat":
            check_performance()

    

def check_week(week):
    
    for element in week.info:
        if week.info[element] == "TRUE":
            if element == "weeks":
                print("lecture", end=" ")   
            else:
                print(element, end=" ")

    return input("\nChoose: ").strip().lower()


def get_link(*args):
    week = Week(args[1],int(args[2]))
    return f"https://cs50.harvard.edu/x/2023/{week.mode}/{args[2]}"

if __name__ == "__main__":
    main()
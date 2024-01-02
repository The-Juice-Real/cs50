def main():
    #Gets the user input and then forces it to be lowercase (this makes the conditionals case insensitive because no matter what the user inputs it's gonna be a lowercase text now)
    answer = input("Great Question of Life, the Universe and Everything").lower().strip()
    print(answer_check(answer))

def answer_check(i):
    match i:
        case "42" | "forty two" | "forty-two":
            return "Yes"
        case _:
            return "No"

main()
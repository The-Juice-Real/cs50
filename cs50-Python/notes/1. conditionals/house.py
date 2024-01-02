name = input("What's your name?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco" | "Tuguldur" | "The Juice":
        print("Slytherin")
    case _:
        print("Unimportant fella")
def main():
    greeting = input("Greet me bitch").strip().lower()
    print(penalty(greeting))

def penalty(i):
    if i.startswith("hello"):
        return "$0"
    elif i.startswith("h"):
        return "$20"
    else:
        return "$100"

main()
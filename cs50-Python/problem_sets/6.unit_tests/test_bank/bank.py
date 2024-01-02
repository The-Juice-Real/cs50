def main():
    greeting = input("Greet me bitch").strip()
    penalty = value(greeting)
    print(f"${penalty}")

def value(greeting):
    converted = greeting.lower()
    if converted.startswith("hello"):
        return 0
    elif converted.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
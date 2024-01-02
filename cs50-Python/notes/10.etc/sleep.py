def main():
    n = int(input("What's n? "))
    for s in bracket(n):
        print(s)

def bracket(n):
    for i in range(n):
        yield "[ ]" * i


if __name__ == "__main__":
    main()
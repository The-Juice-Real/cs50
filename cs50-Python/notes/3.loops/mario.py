def main():
    squaresize = int(input("what is the size of the brick?").strip())
    print_square(squaresize)


def print_square(size):
    for i in range(size):
        print("[ ]" * size)

main()
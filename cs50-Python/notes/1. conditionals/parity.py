def main():
    x = int(input("What's X"))
    if is_even(x):
        print("X is even")
    else:
        print("X is odd")


def is_even(n):
    #return True if n % 2 == 0 else False
    return n % 2 == 0
main()

# where all sub functions are called
def main():
    # input user text
    i = input("Text to lowercase:")
    # output user text in lowercase
    toLowercase(i)


# turn text into lowercase
def toLowercase(text):
    print(text.lower())


# this executes everything together
main()

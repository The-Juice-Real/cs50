def main():
    reps = getinput()
    meow(reps)

def getinput():
    while True:
        n = int(input("How many times do you want the cat to meow?").strip())
        if n > 0:
            return n
        else:
            print("Try again: ", end="")

def meow(reps):
    for _ in range(reps):
        print("meow")


main()

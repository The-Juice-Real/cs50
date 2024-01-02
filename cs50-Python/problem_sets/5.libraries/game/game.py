from random import randrange
import sys

def main():
    level = getint("Level: ")
    random_number = randrange(1, level + 1)
    game_loop(random_number, level)


def game_loop(n, level):
    guess = 0
    while guess != n:

        while True:
            guess = getint("Guess: ")
            if guess >= 0 and guess <= level:
                break
            else:
                pass

        if guess < n:
            print("Too small!")
        elif guess > n:
            print("Too large!")

    sys.exit("Just right!")



def getint(prompt):
    while True:
        try:
            uint = int(input(prompt).strip())
        except:
            pass
        else:
            if uint < 1:
                pass
            else:
                return uint


main()
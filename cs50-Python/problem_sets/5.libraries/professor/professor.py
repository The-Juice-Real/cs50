import random


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answered = False
        for _ in range(3):
            print(f"{x} + {y} = ", end="")
            try:
                answer = int(input().strip())
            except EOFError:
                exit()
            except:
                answer = -1
            if answer == x + y:
                answered = True
                score += 1
                break
            else:
                print("EEE")
        if answered == False:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level_choice = int(input("Level: "))
            if level_choice < 1 or level_choice > 3:
                raise ValueError
        except ValueError:
            pass
        else:
            return level_choice


def generate_integer(level):
    match level:
        case 1:
            return random.randrange(0, 10)
        case 2:
            return random.randrange(10, 100)
        case 3:
            return random.randrange(100, 1000)
        case _:
            raise ValueError


if __name__ == "__main__":
    main()

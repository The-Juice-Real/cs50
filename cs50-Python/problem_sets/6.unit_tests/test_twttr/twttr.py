def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")

def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    shortened = ""
    for letter in word:
        if letter not in vowels:
            shortened += letter
    return shortened



if __name__ == "__main__":
    main()
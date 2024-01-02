def main():
    full_text = input("Say the ting bruv ").strip()
    shorten(full_text)

def shorten(text):
    short_text = ""

    for letter in text:
        if is_vowel(letter) == False:
            short_text += letter
        else:
            continue
    print(short_text)


def is_vowel(letter):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_state = False
    for vowel in vowels:
        if vowel == letter.lower():
            vowel_state = True
    return vowel_state


main()



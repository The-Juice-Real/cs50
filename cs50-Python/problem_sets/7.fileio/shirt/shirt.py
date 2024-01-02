import sys
from PIL import Image
import PIL


def main():
    before, after = get_names()
    mesh(before, after)


def get_names():
    if len(sys.argv) == 3:
        before = sys.argv[1]
        after = sys.argv[2]

        sep_before = before.split(sep=".")
        sep_after = after.split(sep=".")

        if (
            sep_before[-1] != "jpg"
            and sep_before[-1] != "jpeg"
            and sep_before[-1] != "png"
        ):
            print(sep_before[-1])
            sys.exit("Invalid input")
        elif (
            sep_after[-1] != "jpg"
            and sep_after[-1] != "jpeg"
            and sep_after[-1] != "png"
        ):
            sys.exit("Invalid output")
        elif sep_after[-1] != sep_before[-1]:
            sys.exit("Input and output have different extensions")
        else:
            return before, after

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def mesh(before, after):
    try:
        raw = Image.open(before)
        shirt = Image.open("shirt.png")
        resized = PIL.ImageOps.fit(raw, shirt.size)
        # I'm pretty confused on this one but it seems like mask literally tells where the png starts maybe? (image, mask) - this is the syntax I'm following here.
        resized.paste(shirt, shirt)
        resized.save(after)

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()

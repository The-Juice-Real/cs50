def main():
    i = input("input the ting brudah")
    print(convert(i))

def convert(text):
    return text.replace(":)","🙂").replace(":(","🙁")

main()
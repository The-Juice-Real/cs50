def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    elif is_valid(plate) == False:
        print("Invalid")
    else:
        print("is_valid is not returning a bool value")




def is_valid(s):
    if len(s) > 2 and len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
        for i in s[2:len(s)]:
            if i.isdigit() and s[s.index(i):len(s)].isdigit() and i != "0":
                return True
            elif i.isalpha() and s[s.index(i):len(s)].isalpha():
                return True
            elif i.isalpha():
                continue
            else:
                return False
    elif len(s) == 2:
        if(s[0].isalpha() and s[1].isalpha()):
            return True
        else:
            return False
    else:
        return False



if __name__ == "__main__":
    main()
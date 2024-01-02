import inflect

p = inflect.engine()
name_list = []
while True:
    try:
        name = input("Name: ").strip()
    except EOFError:
        print()
        if len(name_list) == 1:
            print(f"Adieu, adieu, to {name_list[0]}")
        else:
            seperated_names = p.join(name_list)
            print(f"Adieu, adieu, to {seperated_names}")
        break
    else:
        name_list.append(name)
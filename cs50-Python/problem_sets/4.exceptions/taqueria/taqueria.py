menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total_amount()


def total_amount():
    amount = 0.00
    while True:
        try:
            current_item = input("Item: ").strip().lower().title()
            if current_item in menu:
                amount += menu[current_item]
        except EOFError:
            print()
            break
        except KeyError:
            pass
        else:
            print(f"Total: ${amount:.2f}")



main()




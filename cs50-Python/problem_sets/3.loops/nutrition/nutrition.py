def main():
    fruit = input("Input fruit: ").strip().lower()
    calories(fruit)

def calories(fruit):
    calory_data = {
        "apple" : 130,
        "avocado" : 50,
        "banana" : 110,
        "cantaloupe" : 50,
        "grapefruit" : 60,
        "grapes" : 90,
        "honeydew melon" : 50,
        "kiwifruit" : 90,
        "lemon" : 15,
        "line" : 20,
        "nectarine" : 60,
        "orange" : 80,
        "peach" : 60,
        "pear" : 100,
        "pineapple" : 50,
        "plums" : 70,
        "strawberries" : 50,
        "sweet cherries" : 100,
        "tangerine" : 50,
        "watermelon" : 80
    }

    if fruit in calory_data:
        print(f"Calories: {calory_data[fruit]}")
    else:
        print("")



main()
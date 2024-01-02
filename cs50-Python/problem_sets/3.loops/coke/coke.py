i = 50

while i > 0:
    print(f"Amount Due: {i}")
    coin = int(input("Insert coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        i -= coin


print(f"Change Owed: {0 - i}")

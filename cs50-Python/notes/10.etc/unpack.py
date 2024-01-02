def total(x, y, z):
    return x + y + z

coins = {"x": 100, "y": 50, "z": 25}


#if we use * before a list, Python unpacks it for me
#if we use * before a dict, it accesses the keys
#if we use ** before a dict, it passes in key=value pair (which is acceptable syntax for a fucntion)
print(total(**coins))


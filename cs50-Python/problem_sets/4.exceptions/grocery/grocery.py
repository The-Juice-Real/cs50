grocery_list = {}

while True:
    try:
        order = input().strip().upper()
        if order in grocery_list:
            grocery_list[order] += 1
        else:
            grocery_list[order] = 1
    except EOFError:
        break


alphabetical_list = sorted(grocery_list)

for index in range(len(alphabetical_list)):
    print(grocery_list[alphabetical_list[index]], alphabetical_list[index])

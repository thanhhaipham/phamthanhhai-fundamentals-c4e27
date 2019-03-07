items = ["T-shirt","Sweater"]
while True:
    Request = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    if Request =="R":
        print(items)
    elif Request =="C":
        new_items = input("Enter new item: ")
        items.append(new_items)
        print(items)
    elif Request == 'U':
        up_pos = int(input("Update position? : "))
        update_item = input(" New item ? : ")
        if up_pos <= len(items):
            items[up_pos-1] = update_item
        else: 
            print("Position is invalid. Please try again!")
        print('Our items:',items)
    elif Request == 'D':
        del_pos = int(input("Delete position ? :"))
        if del_pos <= len(items):
            items.remove(items[del_pos-1])
        else: 
            print("Position is invalid. Please try again!")
        print(items)
stock = []


def addItem():
    global stock

    name = input("The Name:")
    amount = input("Quantity:")
    price = input("Price:")
    item = (name, amount, price)
    stock.append(item)


def update():
    x = input("Item name:")
    index = -1
    for item in stock:
        if item[0] == x:
            index = stock.index(item)
    if index != -1:
        amount = input("New Quantity[Leave empty to keep old quantity]:")
        price = input("New Price[Leave empty to keep old price]:")
        name = stock[index][0]
        amount = stock[index][1] if amount == '' else amount
        price = stock[index][2] if price == '' else price
        stock.pop(index)
        stock.insert(index, (name, amount, price))
    else:
        print("Item not found.")


def display():
    for item in stock:
        print(f"{item[0]} | Count: {item[1]} Price: {item[2]}$")


def run():
    runner = True
    while runner:
        print(
            """What would you like to do?
            1) Add a new Item
            2) Update Stock
            3) Display stock
            4) Exit"""
        )
        x = int(input("Your Choice:"))
        match x:
            case 1:
                addItem()
            case 2:
                update()
            case 3:
                display()
            case 4:
                runner = False


run()

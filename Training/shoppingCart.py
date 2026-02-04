class items:
    def __init__(self, name=None, price=None):
        self.name = input("Enter The Name of Item:") if name == None else name
        self.price = float(input("Enter The Pirce of Item:")) if price == None else price

    def __repr__(self):
        return f"{self.name} — {self.price}/-"


class shoppingCart:
    listItems = []

    def menu(self):
        runner = True
        while runner:
            x = int(
                input(
                    """What would like to do?
                1) Add Item
                2) Display Items
                3) Delete Item
                4) Total Price
                5) Exit
               :"""
                )
            )
            match x:
                case 1:
                    self.addItem()
                case 2:
                    self.display()
                case 3:
                    self.deleteItem()
                case 4:
                    self.total()
                case 5:
                    runner = False

    def addItem(self):
        item = items()
        self.listItems.append(item)

    def display(self):
        for i, item in enumerate(self.listItems, 1):
            print(f"{i}) {item}")

    def deleteItem(self):
        self.display()
        x = int(input("Please Select:")) - 1
        self.listItems.pop(x)

    def total(self):
        total = 0
        for item in self.listItems:
            total += item.price
        print(f"Total Price: {total}")


if __name__ == "__main__":
    obj = shoppingCart()
    obj.menu()

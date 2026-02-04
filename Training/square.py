class square:
    def __init__(self, height=None):
        self.height = float(input("Enter Height of Square:")) if height == None else height

    def area(self):
        print(f"Area: {self.height ** 2}")

    def perimetre(self):
        print(f"Perimetre: {self.height * 4}")


obj = square()
obj.area()
obj.perimetre()

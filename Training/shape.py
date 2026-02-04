import math


class shape:
    def Calcarea(self, height, width):
        self.area = height * width

    def printArea(self):
        print(f"Area: {self.area:.2f}")


class circle(shape):
    def __init__(self, radius=None):
        self.radius = float(input("Enter Radius:")) if radius == None else radius

    def Calcarea(self):
        self.area = math.pi * self.radius**2


class Rectangle(shape):
    def __init__(self, height=None, width=None):
        self.height = float(input("Enter Height:")) if height == None else height
        self.width = float(input("Enter Width:")) if width == None else width

    def Calcarea(self):
        super().Calcarea(self.height, self.width)


cir = circle()
cir.Calcarea()
cir.printArea()

rec = Rectangle()
rec.Calcarea()
rec.printArea()

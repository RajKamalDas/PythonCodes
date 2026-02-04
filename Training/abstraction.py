from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self, len):
        pass


class Circle(Shape):
    def area(self, len):
        print(3.14 * len**2)

class Square(Shape):
    def area(self, len):
        print(len**2)


box = Square()
ball = Circle()

box.area(10)
ball.area(10)

class calc:
    def __init__(self):
        self.__a = int(input("Enter 1st Number:"))
        self.__b = int(input("Enter 2nd Number:"))

    def add(self):
        print(f"Sum = {self.__a + self.__b}")

    def minus(self):
        print(f"Subtraction = {self.__a - self.__b}")


obj = calc()
obj.add()
obj.minus()

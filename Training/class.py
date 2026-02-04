class test:
    a = 10
    _a = 11
    __a = 12

    def print(self):
        print(f"Public:{self.a}, Protected:{self._a}, Private:{self.__a}")


obj = test()
obj.print()

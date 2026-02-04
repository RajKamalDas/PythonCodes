class series:
    sum = 0
    def nat100(self):
        for i in range(1, 101):
            print(i, end=" + ") if i!=100 else print(i, end=" = ")
            self.sum += i
        print(self.sum)

obj = series()
obj.nat100()


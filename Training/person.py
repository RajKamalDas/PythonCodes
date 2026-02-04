class person:
    def __init__(self, name=None, age=None):
        self.name = input("Enter Name:") if name == None else name
        self.age = int(input("Enter Age:")) if age == None else age

    def print(self):
        for item in self.__dict__:
            print(f"{item.title()}: {self.__dict__[item]}")


class student(person):
    def __init__(self, name=None, age=None, studentID=None):
        super().__init__(name, age)
        self.ID = input("Enter ID:") if studentID == None else studentID


class exam(student):
    def __init__(self, name=None, age=None, studentID=None, marks=None):
        super().__init__(name, age, studentID)
        self.marks = input("Enter Marks:") if marks == None else marks


obj = exam()
obj.print()

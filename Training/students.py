class students:
    def __init__(self, name=None, age=None, grade=None):
        self.name = input("Enter Name:") if name == None else name
        self.age = int(input("Enter Age:")) if age == None else age
        self.grade = input("Enter Grade:") if grade == None else grade

    def print(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")


obj = students()
obj.print()

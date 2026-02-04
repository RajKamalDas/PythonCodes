class teacher:
    def __init__(self, name=None, age=None, salary=None):
        self.name = input("Enter Name:") if name == None else name
        self.age = input("Enter Age:") if age == None else age
        self.__salary = input("Enter Salary:") if salary == None else salary

    def print(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.__salary}")


obj = teacher()
print("-------------------------------")
obj.print()

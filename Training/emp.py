class employee:
    def __init__(self, name=None, post=None):
        self.name = input("Name:") if name == None else name
        self.post = input("Post:") if post == None else post

    def print(self):
        print(self.post + ": " + self.name)


obj1 = employee()
obj1.print()
obj2 = employee("Raj")
obj2.print()
obj3 = employee(post="Manager")
obj3.print()
obj4 = employee("Raj", "Team Lead")
obj4.print()

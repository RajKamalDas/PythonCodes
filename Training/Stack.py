class Stack:
    def __init__(self, maxSize=10):
        self.stack = []
        self.limit = maxSize

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == stack.limit, stack.limit - len(self.stack)

    def push(self, *vals, pushBeneath=False):
        check, limit = self.isFull()
        if check:
            print(f"OverFlow! {vals} weren't added.")
            return

        if limit < len(vals):
            print("Not all elements can be added.")

        for i, v in enumerate(vals):
            if i >= limit:
                print(f"{vals[i:]} were not pushed")
                break
            if pushBeneath:
                self.stack.insert(-1, v)
            else:
                self.stack.append(v)
            print(f"{v} was pushed")
            self.top = v

    def pop(self, keepTop=False):
        if self.isEmpty():
            print("UnderFlow.")
        else:
            if keepTop:
                popped = self.stack[-2]
                self.stack.reverse()
                self.stack.remove(popped)
                self.stack.reverse()
            else:
                popped = self.stack.pop()
            print(f"{popped} was popped.")
            self.top = self.stack[-1]
            return popped

    def peek(self):
        if self.isEmpty:
            print("The Satck is empty.")
            return None
        print(f"{self.top} is at the top.")
        return self.top

    def display(self):
        print("The Stack:", self.stack)


stack = Stack(5)

stack.push([10, 20], [30, 40], [50, 60], [70, 80])
stack.display()
stack.peek()

stack.push(40, 50)

stack.pop()
stack.display()

stack.peek()

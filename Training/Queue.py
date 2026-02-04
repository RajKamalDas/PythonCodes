class Queue:
    def __init__(self, maxLimit=10):
        self.queue = []
        self.limit = maxLimit

    def isEmpty(self):
        return len(self.queue) == 0

    def isFull(self):
        return len(self.queue) == self.limit, self.limit - len(self.queue)

    def enQueue(self, *vals):
        check, limit = self.isFull()
        if check:
            print(f"The Queue is Full! {vals} were not added.")
            return
        if len(vals) > limit:
            print("Not all elements were able to be added.")
        for i, v in enumerate(vals):
            if limit <= i:
                print(f"{vals[i:]} were not added.")
                break
            self.queue.append(v)
            print(f"{v} was EnQueued.")

    def deQueue(self):
        if self.isEmpty():
            print("The Queue is empty.")
            return None
        print(f"{self.queue.pop(0)} was DeQueued.")

    def display(self):
        print("The Queue:", self.queue)


queue = Queue(3)

queue.deQueue()
queue.display()

queue.enQueue(10, 20, 30, 40)
queue.display()
queue.enQueue(40, 50)

queue.deQueue()
queue.display()
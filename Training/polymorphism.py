class worker:
    def work(self):
        print("I Work!")


class manager(worker):
    def work(self):
        print("I Manage!")


class developer(worker):
    def work(self):
        print("I Develope!")


w = worker()
m = manager()
d = developer()

w.work()
m.work()
d.work()

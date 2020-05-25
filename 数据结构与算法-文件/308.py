class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q1 = Queue()
print(q1.isEmpty())
q1.enqueue('222')
print(q1.size())
print(q1.dequeue())

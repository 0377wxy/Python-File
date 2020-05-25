class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def divideBy2(decNumber):
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber //= 2
    binString = ''
    while not remstack.isEmpty():
        binString += str(remstack.pop())
    return binString


def baseConverter(decNumber, base):
    digits = '0123456789ABCDEF'
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber //= base
    binString = ''
    while not remstack.isEmpty():
        binString += digits[remstack.pop()]
    return binString


print(divideBy2(42))
print(baseConverter(25, 16))

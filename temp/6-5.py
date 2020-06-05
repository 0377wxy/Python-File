class XX:
    def __init__(self, a):
        self.a = a
    b = []


x1 = XX(1)
print(x1.a)
x1.b.append(3)
x1.b.append(6)
print(x1.b)
x2 = XX(2)
x2.b.append([1, 2])
print(x2.b)

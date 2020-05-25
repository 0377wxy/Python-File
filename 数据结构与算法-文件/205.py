import timeit


def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


t1 = timeit.timeit(
    stmt="test1()", setup="from __main__ import test1", number=1000)
t2 = timeit.timeit(
    stmt="test2()", setup="from __main__ import test2", number=1000)
t3 = timeit.timeit(
    stmt="test3()", setup="from __main__ import test3", number=1000)
t4 = timeit.timeit(
    stmt="test4()", setup="from __main__ import test4", number=1000)
print(t1)
print(t2)
print(t3)
print(t4)

t5 = timeit.repeat(
    stmt="test1()", setup="from __main__ import test1", number=1000, repeat=10)
print(t5)
print(sum(t5)/len(t5))
'''


t1 = Timer("test1()", "from __main__ import test1")
print "concat %f second\n " % t1.timeit(number=1000)
#print("concat {} second\n ".format(t1.timeit(number=1000)))

t2 = Timer("test2()", "from __mian__ import test2")
print "append %f second\n " % t2.timeit(number=1000)
#print("append {} second\n ".format(t2.timeit(number=1000)))
t3 = Timer("test3()", "from __main__ import test3")
print "comprehension %f second\n " % t3.timeit(number=1000)

t4 = Timer("test4()", "from __main__ import test4")
print "list range %f second\n " % t4.timeit(number=1000)
'''

import timeit


def text_list_pop():
    x1 = list(range(2000000))
    t1 = timeit.timeit(
        stmt="x1.pop()", setup="from __main__ import x1", number=1000)
    x2 = list(range(2000000))
    t2 = timeit.timeit(
        stmt="x2.pop(0)", setup="from __main__ import x2", number=1000)
    print(t1)
    print(t2)


text_list_pop()

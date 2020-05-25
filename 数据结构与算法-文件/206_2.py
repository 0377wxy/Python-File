import timeit
import random

for i in range(10000, 1000001, 20000):
    x1 = list(range(i))
    lst_time = timeit.timeit(stmt="random.randrange({}) in x1".format(
        i), setup="from __main__ import random,x1", number=1000)
    x2 = {j: None for j in range(i)}
    d_time = timeit.timeit(stmt="random.randrange({}) in x2".format(
        i), setup="from __main__ import random,x2", number=1000)
    print("{}   {}".format(lst_time, d_time))

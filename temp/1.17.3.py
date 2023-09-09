'''

a = input("a=  ")
b = input("b=  ")
a = int(a)
b = int(b)
c = (b+a)
if c > 5:
    print("a+b>5")
else:
    print("a+b不=5")
'''


'''
a = input("a=  ")
b = input("b=  ")
a = int(a)
b = int(b)

i = a
c = 1
while i < b+1:
    c = c*i
    i = i+1
    print(c, i)

print(c)
'''

'''
b = 7 % 3
c = 7//3
print(b, c)
'''

'''
num = [1, 3]
print(num, num[1])
print(type(num), type(num[1]))
num.append(4)
print(num)
'''

'''
a = input("a= ")
a = int(a)
abc = []
i = 0
while i < a+1:
    abc.append(i)
    i = i+1
print(abc)

abc[0]=10
'''

'''
i = 0
while 1:
    i = i+1
    if i > 10:
        break

#    if i > 3 and i < 6:
#        continue

    if not(i > 3 and i < 6):
        print(i)

'''

'''
ls = ["why", "wxy", "why"]
ls.append("abc")
print(ls)

b = ls.pop(0)
print(ls, b)

b = ls.index("why")
print(ls[-2])
'''

'''
a = input("a=  ")
a = int(a)
wxy = []


i = 0
while i < a+1:
    if i % 2 == 0:

        wxy.append(i)
    # print(i)
    i = i+1
print(wxy)
wxy.pop(1)
print(wxy)

wxy[-1] = 2
print(wxy)
b=wxy.index(2)
print(b)
'''

'''
ls = [3, 5, 1, 4, 2, 6, 0]
# b = len(ls)
i = 0  # 序号
end = len(ls)
f = -1
g = 0
while i < end:
    if ls[i] > f:
        f = ls[i]
        h = i
    i = i+1
g = ls[0]
ls[0] = ls[h]
ls[h] = g
print(ls)
'''


'''
ls = [9, 5, 7, 3, 6, 2, 8]

i = 0
bghdwz = 0
end_i = len(ls)

while i < end_i:
    pos = 0  # 最大值位置
    # 被交换的位置
    value = 10000  # 最大值
    kbz = 0  # 空杯子
    g = i
    end_g = len(ls)

    while g < end_g:
        if ls[g] < value:
            value = ls[g]
            pos = g
            print(g, value, pos)
        g = g+1


    kbz = ls[bghdwz]
    ls[bghdwz] = ls[pos]
    ls[pos] = kbz
    i = i+1
    bghdwz = bghdwz+1
    print(ls)
print(ls)
'''

'''
# 从大到小排列
ls = [6, 4, 8, 2, 5]
i = 0
end_i = len(ls)

while i < end_i:
    n = 0
    j = 0
    end_j = len(ls)-1
    h = 0

    while j < end_j:
        if ls[j] < ls[j+1]:
            h = ls[j]
            ls[j] = ls[j+1]
            ls[j+1] = h
            n = 1
        j = j+1

    i = i + 1

    # if n == 0:
        #
        # break
    print(ls)
print(ls)
'''

'''
# 计算三个数的和与积
def ab(a, b, c, f):
    d = a+b+c
    e = a*b*c
    print("函数內：", d, e)
    if f == 0:
        return d
    else:
        return e


a = 10
w = 12
f = ab(a, w, 2, 0)
g = ab(a, w, 2, 1)


print(f, g)
'''


'''
def fj(c, d, l, ls):

    f = 0
    i = c
    ls[0] = 1
    print("n内ls:", ls)
    if l == 0:
        while i < d+1:
            f = f+i
            i = i+1
        l = 4
        print("内L= ", l)
        return f
    else:
        while i < d+1:
            f = f*i
            i = i+1
        l = 4
        print("内L= ", l)
        return f


a = input("a=  ")
b = input("b=  ")
l = input("l=  ")

ls = [0, 0]
print("ls=", ls)
print("L= ", l)
a = int(a)
b = int(b)
j = fj(a, b, l, ls)
print(j)

print("ls=", ls)
print("L= ", l)
'''


'''
def add(a, ls):
    print("a=", a, " ls[0]=", ls[0])
    if a > 0:
        ls[0] = ls[0]+a
        add(a-1, ls)
    print("结束a=", a)

'''
'''
a = 2
ls = [0, 0]
add(a, ls)
print(ls[0])
'''

'''


def add_2(a):
    print("a=", a)
    c = 5
    if a > 0:
        b = a+add_2(a-1)
        print("b=", b)
        return b
    else:
        return 0


b = add_2(3)
print(b)
'''


'''
# 快速排序算法
def ksort(ls, start, end):
    pos = (start+end)//2  # 位置
    tar = ls[pos]  # 中间数

    ls2 = []
    ls2.append(tar)
    i = start
    while i < end:
        if ls[i] != tar:
            if ls[i] > tar:
                ls2.append(ls[i])
            else:
                ls2.insert(0, ls[i])
        i = i+1
    ls[start: end] = ls2
    print(ls)

    print("out:", ls)

    pos_2 = ls.index(tar)
    print(start, end, pos_2)
    if pos_2 > start+1:
        ksort(ls, start, pos_2)
    if end > (pos_2+1)+1:
        ksort(ls, pos_2+1, end)


ls = [5, 7, 9, 3, 6, 1]

ksort(ls, 0, len(ls))
'''


'''
def hn(n, start, end, mid):
    if n > 2:
        hn(n-1, start, mid, end)
        print(start, " --> ", end)
        hn(n-1, mid, end, start)
    else:
        print(start, " --> ", mid)
        print(start, " --> ", end)
        print(mid, " --> ", end)


hn(7, "A", "B", "C")
'''


'''
def F(n):
    if n > 2:
        b = F(n-1)
        c = F(n-2)
        n = b+c



else:
        if n == 1:
            n = 1
        else:
            n = 2

    return n


s = input("s= ")
s = int(s)
s = F(s)
print(s)

'''


'''
n = input("n=  ")
n = int(n)
g = 0
b = 2

c = 0
d = 0  # 列表位置
e = 0  # 最终结果
ls = [2, 3]

while c < n:
    g = b
    b = ls[b-1]+ls[b-2]
    ls.append(b)
    print(ls[-1])
    b = g
    b = b+1
    c = c+1
print(ls)


d = ls[n-1]
if n == 1:
    d = 2
if n == 2:
    d = 3
print(d)
'''

'''
ls = [0, 2, 3]
n = input("n=  ")
n = int(n)

if n < 3:
    print(ls[n])
else:
    i = 3
    while i <= n:
        ls.append(ls[i-1]+ls[i-2])
        i = i+1
    print(ls[n])
'''

'''
n = input("n=  ")
n = int(n)
ls = []
e = 0
b = 2
a = 2
d = 0
h = 0
while a < n:
    ls.append(a)
    a = a+1

while d < n//4:
    i = 2
    while i < n//2:
        c = i
        c = c*b
        d = ls.index(c)
        ls.pop(d)
        i = i+1
    d = d+1
print(ls)
while e < len(ls):
    h = ls[e]+h
    e = e+1
print(h)
'''
# ls=[0,0]
# ls.clear()


'''
start = input("start=  ")
end = input("end=  ")

start = int(start)

end = int(end)
a = start
b = a

d = b
ls = []
ls_2 = []
while a < end:
    n = b
    c = 1
    e = 0
    g = a
    h = 0
    b = d
    while b < end:
        ls.clear()
        d = 0
        c=1# print("---")
        while c>b/2:
            # print("g=", g, "end=", end)
            if b % c == 0:

                ls.append(c)
                c = c+1
                # print(ls)
            else:
                c = c+1
            # print("--------------")
            g = g+1
        # print("----")
        d = 0
        # print("ls= ", ls)
        while d < len(ls):
            # print("---")
            e = ls[d]+e
            # print("d=", d)
            d = d+1
        # print("e= ", e)
        g = e
        c = 1
        ls.clear()
        while g < end:

            if e % c == 0:
                ls.append(c)
                c = c+1
            else:
                c = c+1
            g = g+1
        d = 0
        print("ls= ", ls)
        while d < len(ls):
            # print("-")
            h = ls[d]+h
            d = d+1
            print("------", d, h)
        if h == e:
            ls_2.append(h)
            ls_2.append(e)
        b = b+1
    a = a+1

    print(ls)
print(ls_2)
'''
'''

def GH(start):
    a = start
    b = 1
    ls = []
    while b < a/2+1:
        if a % b == 0:
            ls.append(b)
            b = b+1
        else:
            b = b+1
    # print(ls)
    c = 0  # 列表位置
    d = 0  # 因数和
    while c < len(ls):
        d = d+ls[c]
        c = c+1
    # print(d)
    return(d)


start = input("start=  ")
start = int(start)
end = input("end=  ")
end = int(end)
while start < end+1:
    k = GH(start)
    l = GH(k)
    if l == start and k < start:
        print(k, end='--')
        print(start)
    start = start+1


#    n = input("n=")
 #   n = int(n)
 #   b = GH(n)
 #   print(b)

'''
'''



import math
def ss(n):
    a = 2
    b = 0

    while a < n//2+1:

        if n % a == 0:
            b = 0
            break
        else:
            a = a+1
    if a == n//2+1:

        b = 1
    return(b)
'''

'''
n = input("n=  ")
n = int(n)
while 1:
    b = 0
    a = 0
    a = ss(n)
    if a == 1:
        b = ss(n+2)
        if b == 1:
            print(n, end=' ')
            print(n+2)
            break
    n = n+1
'''
'''
n = input("n=  ")
n = int(n)
while 1:
    f = 0
    while 1:
        a = ss(n)
        if a == 1:
            break
        else:
            n = n+1
    b = ss(n+2)
    if b == 1:
        print(n, n+2)
        break
    n = n+1


b = math.pow(4, 3)
print(b)
'''
'''
#import math


end = 1000
start = 99

while start < end:
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    a = start % 100
    b = a % 10
    e = (start-a)/100
    f = math.pow(e, 3)
    c = math.pow(b, 3)
    a = (a-b)/10
    d = math.pow(a, 3)
    if f+c+d == start:
        print(start, end=' ')
    start = start+1


n = input("n= ")
n = int(n)
c = 0
# print(type(n), type(m))
a = 1
while n > 0:
    b = str(a)
    b = b+" "
    print(" "*(n-1), b*a)
    n = n-1
    a = a+1
'''

'''

import math as ma
def dbd(a, ls):
    while 1:
        b = a % 10
        a = a//10  # b = ma.pow(b, 3)
        ls.append(b)
        if a == 0:
            break


ls = []
n = input("n=  ")
n = int(n)
o = input("o= ")
o = int(o)
while n > -1:
    c = 0
    m = 0
    ls.clear()
    a = dbd(n, ls)
    while m < len(ls):
        b = ma.pow(ls[m], o)
        c = c+b
        m = m+1
    if c == n:
        print(n, end=' ')
    n = n-1
'''
'''
end = input("方案数=  ")
end = int(end)
a = 1  # 5分硬币数
d = 0  # 现在总钱
c = 100-1-a  # 1分硬币数
b = 1  # 2分硬币数

while a < end+1:

    c = 100-1-a  # 1分硬币数
    b = 1  # 2分硬币数
    d = (5*a)+(2*b)+(c*1)
    while b < 76:
        #print("b=", b, "---")
        b = b+1
        c = c-1
        d = d+1
        # print(d)
        if d == 150:
            print("------")
            print(a, end=' ')
            print(b, end=' ')
            print(c)
    a = a+1
'''
'''
n = input("层数=  ")
n = int(n)
ls = []
end = 0  # 最后结果
a = 1  # "2"的次数
b = n  # 当前值
ba = 0   # 当前"2"
if n % 2 == 0:
    end = end+1
while a < n/2+1:
    m = 0
    ba = 0
    ls.clear()
    while ba < a+1:
        ls.append(2)
        b = b-2
        ba = ba+1
    while b > 0:
        ls.append(1)
        b = b-1
    m = len(ls)
    m = -m

    a = a+1
print(end)
'''

'''
def cf(o, ls, ls_2):
    while 1:
        b = o % 10
        o = o//10
        ls.append(b)
        ls_2.append(b)
        if o == 0:
            break
    while len(ls) < 4:

        ls.append(0)

    # print(ls)
    c = 0
    b = 1
    d = len(ls)+1
    a = 0
    # print(a)
    while a < len(ls)-1:
        #print("b=", b, "c=", c)

        b = a+1

        #print("-----", "a=", a, "b=", b)
        while b < len(ls):

            #print("--------", "a=", a, "b=", b)
            #print(ls[a], ls[b], ls)
            if ls[a] == ls[b]:
                c = ls.pop(b)
            else:
                b = b+1

        a = a+1
    # print(ls)
    d = len(ls)
    return(d)


o = input("出生年份=")
o = int(o)
n = input("数字=")
n = int(n)
ls = []
ls_2 = []

m = o
while o < 3001:
    ls.clear()
    ls_2.clear()
    a = cf(o, ls, ls_2)
    # print(ls_2)
    k = 4-len(ls_2)
    #print("--", "a=", a, end=' ')
    #print("-", "o=", o)

    if a == n:
        m = o-m
        print(m, end=' ')
        print("0"*k, end='')
        print(o)
        break

    o = o+1
'''

'''
ls = [[1], [1, 1]]
n = input("n=")
n = int(n)
a = 2
b = 1
c = 1
while a < n:
    ls.append([1, 1])
    b = 1
    c = c+1
    while b < c:
        ls[a].insert(b, ls[a-1][b]+ls[a-1][b-1])
        b = b+1
    a = a+1
a = 1
b = 0
s = 0
print(1)
while a < len(ls):
    b = 0
    while b < a+1:
        if b < a:
            v = ls[a][b+1]
            s = 0
            while 1:
                v = v//10
                s = s+1
                if v == 0:
                    break
            s = 4-s
            print(ls[a][b], end=' '*s)

        else:
            print(ls[a][b])
        b = b+1
    a = a+1
'''
'''
fj = "ababdertaberabadj"
o = len(fj)
ls = [0 for i in range(o)]
jf = ""

a = input("删除字母=")
b = len(a)

c = 0  # 开始
d = b-1  # 结束
while d < len(fj)+1:
    if len(fj) < len(a):
        print(fj, "-----")
        break
    if fj[c:d+1] != a:
        c = c+1
    else:
        u = len(fj[c:d+1])
        ls[c:d+1] = [1 for i in range(u)]
        c = c+1
    d = d+1
a = 0
print(ls)
while a < len(fj):
    if ls[a] != 1:
        jf = jf+fj[a]
    a = a+1


print(jf)
'''
ha = input("行=")
ha = int(ha)
li = input("列=")
li = int(li)
#ls = input["ls="]

ls_2 = [[0 for s in range(ha)] for i in range(li)]

print(ls_2)
a = 0  # 行
b = 0  # 列

'''
a = input("请输入a的值： ")
b = input("请输入b：")

a = int(a)
b = int(b)

print(a, b)
print(type(a), type(b))


if a > 100 or b > 100:
    print("超出限制")
else:
    if a < b:
        print("a<b")
        if a > b:
            print("a>b")
        else:
            print("a=b")
'''

'''
d = input("d=   ")
e = input("e=   ")
d = int(d)
e = int(e)

f = 1
if d > e:
    g = 0
    g = d
    d = e
    e = g
h = d
print(d, e, h)

while h < e+1:
    f = f*h
    h = h+2
    print(f, h)

print(f)
'''

'''
a = input("a=  ")
b = input("b=  ")
a = int(a)
b = int(b)
e = 0
if a > b:
    f = 0
    f = a
    a = b
    b = f
c = a
c = int(c)
while c < b+1:
    if c % 3 == 0 and c % 4 == 0:
        print(c)
        e = e+c
    c = c+1
print(e)
'''

'''
a = input("a=  ")
b = input("b=  ")
a = int(a)
b = int(b)
f = 0
if a > b:
    c = 0
    c = a
    a = b
    b = c
e = b
while e > a-1:
    if e % 3 == 0 and e % 2 == 1:
        print(f, e)
        f = f+e
    e = e-1
print(f)
'''

'''
a = 1 > 2
print(a)
print(type(a))
b = int(a)
print(b)
'''

'''
ls = [3, 4, 5, 6, 84]
i = 1
end_i = len(ls)
while i < end_i:
    f = -1
    j = i-1
    end_j = len(ls)
    k = i-1
    g = 0
    h = 0
    while j < end_j:
        if ls[j] > f:
            f = ls[j]
            h = j
        j = j+1
    g = ls[k]
    ls[k] = ls[h]
    ls[h] = g
    i = i+1
print(ls)
'''

'''
ls = [0, 1, 2, 3]
print(ls[0])
print(ls[0:2])
ls[1:3] = [3, 2, 1]
print(ls)
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


k = 7
c = add_2(k)
print(c)



a = "3"
print(a)
b = a+" 4"
print(b)
print(b[0], b[2])

ls = [2, 3, 4, 5, 6]
a = len(ls)
print(a)

d = 2
j = 2
ls = []
ls.append(d*j)
s = len(ls)
print(ls, s)

n = 8
n = -n
print(n)
'''

'''
a = 4
b = 3
c = 2
d = 1
print("0"*3, end='')
print(a)


ls = []
ls = [[0, 1], [2, 3]]
print(ls)
ls.append([4, 5])
print(ls)
ls[0].append(10)
print(ls)
print(ls[0][2])
ls2 = [[0]*5]
print(ls2)
ls3 = [0 for i in range(5)]
print(ls3)


for i in ls:
    print(i)

ls = [[1], [1, 1], [1, 2, 1]]
ls[1].clear()
print(ls)
'''

'''
ls = [2, 3, 4, ]
d = ls[1]-4
print(ls)
print(12, end=" "*3)
a = 1234

b = str(a)

print(len(b))

a = "abcdabcabcac"
b = "abca"
ls = [0, 1, 2, 3, 4, 5, 6]
ls2 = ls[0:3]+ls[4:]
ls3 = a[:2]+a[5:]

print(ls2, ls3)
'''


jf = "udslhuafs"
a = "1"*4
jf[2:5] = a
print(jf)

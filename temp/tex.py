import math 

while True:

    raw = input()
    if raw ==  "":
        break

    raw = list(map(int, raw.split()))
    n=raw[0]
    m=raw[1]
    k=raw[2]

    da=[]
    for i in range(n):
        a = input().split()
        num=0
        for j in range(k):
            if a[0][j]=="1":
                num+=1
        a.append(num)
        da.append(a)
   
    res=[]
    for i in range(n-m+1):
        well =0
        for j in range(m):
            well+=da[i+j][1]
        res.append(well)
   
    print(min(res))

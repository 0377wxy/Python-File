import math 

while True:

    raw = input()
    if raw ==  "":
        break

    ra = raw.split()
    n=int(ra[0])

    da=[]
    for i in range(n):
        a = list(map(int, input().split()))
        da.append(a)
   
    energy_res=[]
    for i in range(n):
        energy=0
        for j in range(n):
            energy+=da[j][2]*(math.fabs(da[i][0]-da[j][0]) + math.fabs(da[i][1]-da[j][1]) )
        energy_res.append(energy)
    print(int(min(energy_res)))

   
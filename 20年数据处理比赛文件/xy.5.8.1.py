import numpy as np
import pandas as pd
import geohash2
from folium.plugins import HeatMap
import folium
import re
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


df = pd.read_csv(
    'D:\\Program_file\\python_file\\python.con\\mobike_train_data.csv', usecols=['starttime', 'geohashed_start_loc', 'geohashed_end_loc'])

df_start = pd.DataFrame(columns=['j1', 'w1', 'xx', 'xa'])
df_end = pd.DataFrame(columns=['j2', 'w2'])
df = df[197000:200000]

for i in range(df.shape[0]):
    an = re.search(
        '2017-05-(10|11|12|15|16|17|18|19|22|23)\s(06|07|08):\d\d:\d\d', df.iloc[i, 0])
    if(an):
        df_start = df_start.append(
            [{'j1': geohash2.decode(df.iloc[i][1])[0], 'w1': geohash2.decode(df.iloc[i][1])[1], 'xx':1, 'xa':2}], ignore_index=True)
        df_end = df_end.append(
            [{'j2': geohash2.decode(df.iloc[i][2])[0], 'w2':geohash2.decode(df.iloc[i][2])[1], 'xx':1, 'xa':2}], ignore_index=True)


dx = df_start.groupby(by=[df_start["j1"], df_start["w1"]])
di = dx.count()['xx']
start_Count = di.sort_values()
dx = df_end.groupby(by=[df_end["j2"], df_end["w2"]])
di = dx.count()['xx']
end_Count = di.sort_values()
d = {"start": start_Count, "end": end_Count}
Count = pd.DataFrame(d)
Count = Count.fillna(0)

Count["E-S"] = np.nan
Count["increase"] = np.nan
Count["reduce"] = np.nan
Count = Count.copy()
for i in range(Count.shape[0]):
    Count.iloc[i][2] = Count.iloc[i][0] - Count.iloc[i][1]
increace_max = Count["E-S"].max()
reduce_max = Count["E-S"].min()
for i in range(Count.shape[0]):
    if Count.iloc[i][2] > 0:
        Count.iloc[i][3] = Count.iloc[i][2] / increace_max
        Count.iloc[i][4] = 0
    else:
        Count.iloc[i][4] = Count.iloc[i][2] / reduce_max
        Count.iloc[i][3] = 0

print(Count)
'''
L3 = []
for i, j in zip(Count.index, Count["E-S"]):
    if j != 0:
        L3.append([float(i[0]), float(i[1]), j])
'''
x = []
y = []
z = []
for i, j in zip(Count.index, Count["E-S"]):
    if j != 0 and 38 <= float(i[0]) <= 41 and 113 <= float(i[1]) <= 117:
        x.append(float(i[0]))
        y.append(float(i[1]))
        z.append(j)

print('------------------------------------------------')
print(x)
print('------------------------------------------------')
print(y)
print('------------------------------------------------')
print(z)

C = []
for a in z:
    if a < -16:
        C.append('C0')
    elif a < -8:
        C.append('C2')
    elif a < 0:
        C.append('C9')
    elif a < 8:
        C.append('C6')
    elif a < 16:
        C.append('C1')
    elif a > 15:
        C.append('C3')


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_zlim(-30, 25)
ax.bar3d(x, y, 0, dx=0.005, dy=0.005, dz=z, alpha=0.5, color=C)
plt.rcParams['font.sans-serif'] = ['SimHei']
ax.set_xlabel('纬度')
ax.set_ylabel('经度')
ax.set_zlabel('自行车数量改变量')
plt.show()


'''        
L1 = []
for i, j in zip(Count.index, Count["increase"]):
    if j != 0:
        L1.append([float(i[0]), float(i[1]), j])
L2 = []
for i, j in zip(Count.index, Count["reduce"]):
    if j != 0:
        L2.append([float(i[0]), float(i[1]), j])

m = folium.Map([39.93, 116.38], radius=5, tiles='stamentoner', zoom_start=14)
HeatMap(L1).add_to(m)
m.save("D:\\Program_file\\python_file\\python.con\\inctrase.html")

n = folium.Map([39.93, 116.38], radius=5, tiles='stamentoner', zoom_start=14)
HeatMap(L2).add_to(n)
n.save("D:\\Program_file\\python_file\\python.con\\reduce.html")
'''

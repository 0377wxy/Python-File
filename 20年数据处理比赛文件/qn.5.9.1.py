import numpy as np
import pandas as pd
import geohash2
from folium.plugins import HeatMap
import folium
import re
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


df = pd.read_csv('D:/1.csv', usecols=['starttime', 'geohashed_start_loc', 'geohashed_end_loc'])

df7_start = pd.DataFrame(columns=['j1', 'w1', 'xx'])
df7_end = pd.DataFrame(columns=['j2', 'w2'])
df14_start = pd.DataFrame(columns=['j1', 'w1', 'xx'])
df14_end = pd.DataFrame(columns=['j2', 'w2'])


for i in range(df.shape[0]):
    an = re.search('2017-05-10\s06:\d\d:\d\d', df.iloc[i, 0])#2017-05-(10|11|12|15|16|17|18|19|22|23)\s(06|07|08):\d\d:\d\d
    if(an):
        df7_start = df7_start.append(
            [{'j1': geohash2.decode(df.iloc[i][1])[0], 'w1': geohash2.decode(df.iloc[i][1])[1], 'xx':1}], ignore_index=True)
        df7_end = df7_end.append(
            [{'j2': geohash2.decode(df.iloc[i][2])[0], 'w2':geohash2.decode(df.iloc[i][2])[1], 'xx':1}], ignore_index=True)
    
    an = re.search('2017-05-24\s06:\d\d:\d\d', df.iloc[i, 0])#2017-05-(10|11|12|15|16|17|18|19|22|23)\s(06|07|08):\d\d:\d\d
    if(an):
        df14_start = df14_start.append(
            [{'j1': geohash2.decode(df.iloc[i][1])[0], 'w1': geohash2.decode(df.iloc[i][1])[1], 'xx':1}], ignore_index=True)
        df14_end = df14_end.append(
            [{'j2': geohash2.decode(df.iloc[i][2])[0], 'w2':geohash2.decode(df.iloc[i][2])[1], 'xx':1}], ignore_index=True)


dx = df7_start.groupby(by=[df7_start["j1"], df7_start["w1"]])
di = dx.count()['xx']
start_count_1 = di.sort_values()
dx = df7_end.groupby(by=[df7_end["j2"], df7_end["w2"]])
di = dx.count()['xx']
end_count_1 = di.sort_values()
d = {"start": start_count_1, "end": end_count_1}
count_1 = pd.DataFrame(d)
count_1 = count_1.fillna(0)

count_1["E-S_7"] = np.nan
count_1 = count_1.copy()
for i in range(count_1.shape[0]):
    count_1.iloc[i][2] = count_1.iloc[i][0] - count_1.iloc[i][1]

#count_1.to_csv('D:/data_count1.csv')


#---------------------------------------
dx = df14_start.groupby(by=[df14_start["j1"], df14_start["w1"]])
di = dx.count()['xx']
start_count_2 = di.sort_values()
dx = df14_end.groupby(by=[df14_end["j2"], df14_end["w2"]])
di = dx.count()['xx']
end_count_2 = di.sort_values()
d = {"start": start_count_2, "end": end_count_2}
count_2 = pd.DataFrame(d)
count_2 = count_2.fillna(0)

count_2["E-S_14"] = np.nan
count_2 = count_2.copy()
for i in range(count_2.shape[0]):
    count_2.iloc[i][2] = count_2.iloc[i][0] - count_2.iloc[i][1]


#count_2.to_csv('D:/data_count2.csv')

count_1.drop(['start'],axis=1,inplace=True)
count_1.drop(['end'],axis=1,inplace=True)
count_2.drop(['start'],axis=1,inplace=True)
count_2.drop(['end'],axis=1,inplace=True)
count = pd.merge(count_1, count_2, left_index=True , right_index=True , how='outer')
count = count.fillna(0)

count["14-7"] = np.nan
count = count.copy()
for i in range(count.shape[0]):
    count.iloc[i][2] = count.iloc[i][1] - count.iloc[i][0]

count.to_csv('D:/data_count_count_14-7.csv')


'''
x = []
y = []
z = []
for i,j in zip(count_1.index, count_1["E-S"]):
    if j != 0 and 38<=float(i[0])<=41 and 113<=float(i[1])<=117:
        x.append(float(i[0]))
        y.append(float(i[1]))
        z.append(j)

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
ax.bar3d( x , y , 0 , dx = 0.005 , dy = 0.005 , dz = z , alpha = 0.5 , color = C )
plt.rcParams['font.sans-serif']=['SimHei']
ax.set_xlabel('纬度')
ax.set_ylabel('经度')
ax.set_zlabel('自行车数量改变量')
plt.show()
#plt.savefig("d:/temp.png",dpi=500,bbox_inches = 'tight')
'''
'''
L1 = []
for i, j in zip(count_1.index, count_1["increase"]):
    if j != 0:
        L1.append([float(i[0]), float(i[1]), j])
L2 = []
for i, j in zip(count_1.index, count_1["reduce"]):
    if j != 0:
        L2.append([float(i[0]), float(i[1]), j])

city_map_increase = folium.Map(
    location=[39.93, 116.38],
    zoom_start=15,
    tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}',
    attr="default"
    )
HeatMap(L1).add_to(city_map_increase)
city_map_increase.save('D:/city_map_increase.html')

city_map_reduce = folium.Map(
    location=[39.93, 116.38],
    zoom_start=15,
    tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}',
    attr="default"
    )
HeatMap(L2).add_to(city_map_reduce)
city_map_reduce.save('D:/city_map_reduce.html')
'''

'''
m = folium.Map([39.93, 116.38], radius=5, tiles='stamentoner', zoom_start=14)
HeatMap(L1).add_to(m)
m.save("D:\\Program_file\\python_file\\python.con\\inctrase.html")

n = folium.Map([39.93, 116.38], radius=5, tiles='stamentoner', zoom_start=14)
HeatMap(L2).add_to(n)
n.save("D:\\Program_file\\python_file\\python.con\\reduce.html")
'''
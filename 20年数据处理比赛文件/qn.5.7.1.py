import numpy as np
import pandas as pd
import geohash2
from folium.plugins import HeatMap
import folium
import re

df = pd.read_csv(
    'D:\\Program_file\\python_file\\python.con\\mobike_train_data.csv', usecols=['starttime', 'geohashed_start_loc', 'geohashed_end_loc'])

df_start = pd.DataFrame(columns=['j1', 'w1', 'xx', 'xa'])
df_end = pd.DataFrame(columns=['j2', 'w2'])
df = df[195000:200000]

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
start_count = di.sort_values()
dx = df_end.groupby(by=[df_end["j2"], df_end["w2"]])
di = dx.count()['xx']
end_count = di.sort_values()
d = {"start": start_count, "end": end_count}
Count = pd.DataFrame(d)
Count = Count.fillna(0)
'''
print(Count.iloc[2][0])
print(Count.iloc[6][1])
print(Count[8])
'''
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
# Count.to_csv("out.csv")

L1 = []
for i, j in zip(Count.index, Count["increase"]):
    if j != 0:
        L1.append([float(i[0]), float(i[1]), j])
L2 = []
for i, j in zip(Count.index, Count["reduce"]):
    if j != 0:
        L2.append([float(i[0]), float(i[1]), j])
'''
for i in range(len(L1)):
    print(L1[i], "--", L2[i])
'''

m = folium.Map([39.93, 116.38], radius=5, tiles='stamentoner', zoom_start=14)
HeatMap(L1).add_to(m)
m.save("D:\\Program_file\\python_file\\python.con\\inctrase.html")

n = folium.Map([39.93, 116.38], radius=5, tiles='stamentoner', zoom_start=14)
HeatMap(L2).add_to(n)
n.save("D:\\Program_file\\python_file\\python.con\\reduce.html")

print("--------------------------------------------")


'''
lis = []
j_min = di.min()
j_max = di.max()
for i, j in zip(di.index, di.values):
    lis.append([float(i[0]), float(i[1]), (j-j_min)/(j_max-j_min)])
print(lis)
'''


'''        
lis_start = []
lis_end = []
for j in range(df_start.shape[0]):
    lis_start.append([df_start.iloc[j][0],df_start.iloc[j][1],1])

for k in range(df_end.shape[0]):
    lis_end.append([df_end.iloc[k][0],df_end.iloc[k][1],1])
'''


'''   
city_map_start = folium.Map(
    location=[39.93, 116.38],
    zoom_start=15,
    tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}',
    attr="default"
    )
HeatMap(lis_start).add_to(city_map_start)
city_map_start.save('D:/map_start.html')

city_map_end = folium.Map(
    location=[39.93, 116.38],
    zoom_start=15,
    tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}',
    attr="default"
    )
HeatMap(lis_end).add_to(city_map_end)
city_map_end.save('D:/map_end.html1')

'''

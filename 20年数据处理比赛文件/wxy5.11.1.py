import numpy as np
import pandas as pd
import geohash2
from folium.plugins import HeatMap
import folium
import re

df = pd.read_csv(
    'D:\\Program_file\\python_file\\python.con\\mobike_train_data.csv', usecols=['starttime', 'geohashed_start_loc', 'geohashed_end_loc'])

df_start = pd.DataFrame(columns=['j1', 'w1', 'xx'])
df_end = pd.DataFrame(columns=['j2', 'w2', 'xx'])

for i in range(df.shape[0]):
    an = re.search(
        '2017-05-(10|11|12|13|14|15|16)\s20:\d\d:\d\d', df.iloc[i, 0])
    if(an):
        df_start = df_start.append(
            [{'j1': geohash2.decode(df.iloc[i][1])[0], 'w1': geohash2.decode(df.iloc[i][1])[1], 'xx':1}], ignore_index=True)
        df_end = df_end.append(
            [{'j2': geohash2.decode(df.iloc[i][2])[0], 'w2': geohash2.decode(df.iloc[i][2])[1], 'xx':1}], ignore_index=True)

dx = df_start.groupby(by=[df_start["j1"], df_start["w1"]])
di = dx.count()['xx']
start_d_values = di.sort_values()
dx = df_end.groupby(by=[df_end["j2"], df_end["w2"]])
di = dx.count()['xx']
end_d_values = di.sort_values()
d = {"start": start_d_values, "end": end_d_values}
d_values = pd.DataFrame(d)
d_values = d_values.fillna(0)

d_values["E-S"] = np.nan
d_values["increase"] = np.nan
d_values["reduce"] = np.nan
d_values = d_values.copy()
for i in range(d_values.shape[0]):
    d_values.iloc[i][2] = d_values.iloc[i][0] - d_values.iloc[i][1]
increace_max = d_values["E-S"].max()
reduce_max = d_values["E-S"].min()
for i in range(d_values.shape[0]):
    if d_values.iloc[i][2] > 0:
        d_values.iloc[i][3] = d_values.iloc[i][2] / increace_max
        d_values.iloc[i][4] = 0
    else:
        d_values.iloc[i][4] = d_values.iloc[i][2] / reduce_max
        d_values.iloc[i][3] = 0

L5 = []
for i, j in zip(d_values.index, d_values["increase"]):
    if j != 0:
        L5.append([float(i[0]), float(i[1]), j])
L6 = []
for i, j in zip(d_values.index, d_values["reduce"]):
    if j != 0:
        L6.append([float(i[0]), float(i[1]), j])

m = folium.Map([39.93, 116.38], radius=5, tiles='stamentoner', zoom_start=11)
HeatMap(L5).add_to(m)
m.save("D:\\Program_file\\python_file\\python.con\\inctrase_7_20.html")
m

n = folium.Map([39.93, 116.38], radius=5, tiles='stamentoner', zoom_start=11)
HeatMap(L6).add_to(n)
n.save("D:\\Program_file\\python_file\\python.con\\reduce_7_20.html")
n

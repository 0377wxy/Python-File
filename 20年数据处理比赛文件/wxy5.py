from mpl_toolkits.mplot3d import Axes3D
import re
import folium
from folium.plugins import HeatMap
import pandas as pd
import numpy as np
import geohash2
import matplotlib.pyplot as plt

df = pd.read_csv(
    'D:\\Program_file\\python_file\\python.con\\mobike_train_data.csv')

df['starttime'] = pd.to_datetime(df.starttime)
df = df.sort_values(by='starttime', ascending=True)
df.index = df['starttime']
#df = df['2017-05-15 06:00:00' : '2017-05-15 06:30:00']

dayTimeIndex = [x for x in range(0, 24)]
dayTime = [[0]*24, [0]*24]
Count = []
for a in range(10, 25):
    One = []
    for b in range(23):
        dx = df["2017-05-{:0>2d} {:0>2d}:00:00".format(
            a, dayTimeIndex[b]): "2017-05-{:0>2d} {:0>2d}:00:00".format(a, dayTimeIndex[b+1])]
        One.append(dx.shape[0])
        dayTime[0][b] += dx.shape[0]
        if dx.shape[0] != 0:
            dayTime[1][b] += 1
    dx = df["2017-05-{:0>2d} {:0>2d}:00:00".format(
            a, 23): "2017-05-{:0>2d} {:0>2d}:00:00".format(a + 1, 0)]
    One.append(dx.shape[0])
    dayTime[0][23] += dx.shape[0]
    if dx.shape[0] != 0:
        dayTime[1][23] += 1
    Count.append(One)


df = pd.read_csv(
    'D:\\Program_file\\python_file\\python.con\\mobike_train_data.csv', usecols=['starttime', 'geohashed_start_loc', 'geohashed_end_loc'])
fig = plt.figure(figsize=(18, 10))

for hour_one in range(8, 10):
    df7_start = pd.DataFrame(columns=['j1', 'w1', 'xx'])
    df7_end = pd.DataFrame(columns=['j2', 'w2'])
    df14_start = pd.DataFrame(columns=['j1', 'w1', 'xx'])
    df14_end = pd.DataFrame(columns=['j2', 'w2'])

    for i in range(df.shape[0]):
        # 2017-05-(10|11|12|15|16|17|18|19|22|23)\s(06|07|08):\d\d:\d\d
        an = re.search(
            '2017-05-(13|14)\s{:0>2d}:1\d:\d\d'.format(hour_one), df.iloc[i, 0])
        if(an):
            df7_start = df7_start.append(
                [{'j1': geohash2.decode(df.iloc[i][1])[0], 'w1': geohash2.decode(df.iloc[i][1])[1], 'xx':1}], ignore_index=True)
            df7_end = df7_end.append(
                [{'j2': geohash2.decode(df.iloc[i][2])[0], 'w2':geohash2.decode(df.iloc[i][2])[1], 'xx':1}], ignore_index=True)

        # 2017-05-(10|11|12|15|16|17|18|19|22|23)\s(06|07|08):\d\d:\d\d
        an = re.search(
            '2017-05-(13|14)\s{:0>2d}:1\d:\d\d'.format(hour_one), df.iloc[i, 0])
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

    # count_1.to_csv('D:/data_count1.csv')

    # ---------------------------------------
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

    # count_2.to_csv('D:/data_count2.csv')

    count_1.drop(['start'], axis=1, inplace=True)
    count_1.drop(['end'], axis=1, inplace=True)
    count_2.drop(['start'], axis=1, inplace=True)
    count_2.drop(['end'], axis=1, inplace=True)
    count = pd.merge(count_1, count_2, left_index=True,
                     right_index=True, how='outer')
    count = count.fillna(0)

    count["14-7"] = np.nan
    count = count.copy()
    for i in range(count.shape[0]):
        count.iloc[i][2] = count.iloc[i][1] - \
            count.iloc[i][0]*((Count[10][hour_one]+Count[11]
                               [hour_one])/(Count[3][hour_one]+Count[4][hour_one]))

    # count.to_csv('D:/data_count_count_14-7.csv')
    # -----------------------------------------------------

    x = []
    y = []
    z = []
    for i, j in zip(count_2.index, count_2["E-S_14"]):
        if j != 0 and 39 <= float(i[0]) <= 41 and 116 <= float(i[1]) <= 118:
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
    plt.subplot(2, 2, (hour_one-7)*2-1)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_zlim(-30, 25)
    ax.bar3d(x, y, 0, dx=0.005, dy=0.005, dz=z, alpha=0.5, color=C)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    ax.set_xlabel('纬度')
    ax.set_ylabel('经度')
    ax.set_zlabel('自行车改变量')

    # -------------------------------------------

    x = []
    y = []
    z = []
    for i, j in zip(count.index, count["14-7"]):
        if j != 0 and 39 <= float(i[0]) <= 41 and 116 <= float(i[1]) <= 118:
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

    plt.subplot(2, 2, (hour_one-7)*2)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_zlim(-30, 25)
    ax.bar3d(x, y, 0, dx=0.005, dy=0.005, dz=z, alpha=0.5, color=C)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    ax.set_xlabel('纬度')
    ax.set_ylabel('经度')
    ax.set_zlabel('自行车改变量')
fig.show()
fig.savefig("xxx.png", dpi=1000)

import pandas as pd
import numpy as np
import geohash2

df = pd.read_csv("D:\\Program_file\\python.con\\mobike_train_data.csv")
df['starttime'] = pd.to_datetime(df.starttime)
df = df.sort_values(by='starttime', ascending=True)
df.index = df['starttime']
df = df['2017-05-15 06:00:00':'2017-05-15 06:30:00']
df["J1"] = np.nan
df["W1"] = np.nan
df["J2"] = np.nan
df["W2"] = np.nan
for i in range(df.shape[0]):
    df.iloc[i, 7], df.iloc[i, 8] = geohash2.decode(df.iloc[i][5])
    df.iloc[i, 9], df.iloc[i, 10] = geohash2.decode(df.iloc[i][6])

dx = df.groupby(by=[df["J1"], df["W1"]])
di = dx.count()["userid"]
di = di.sort_values()
# print(di)
lis = []
j_min = di.min()
j_max = di.max()
for i, j in zip(di.index, di.values):
    lis.append([float(i[0]), float(i[1]), (j-j_min)/(j_max-j_min)])

#x1 = np.array(di)
print(lis)

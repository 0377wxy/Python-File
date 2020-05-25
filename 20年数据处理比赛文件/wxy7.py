import pandas as pd
import numpy as np
import geohash2

df = pd.read_csv("D:\\Program_file\\python_file\\contest\\test2.csv")
print(df)

df["J1"] = np.nan
df["W1"] = np.nan
df["J2"] = np.nan
df["W2"] = np.nan
for i in range(df.shape[0]):
    df.iloc[i, 7], df.iloc[i, 8] = geohash2.decode(df.iloc[i][5])
    df.iloc[i, 9], df.iloc[i, 10] = geohash2.decode(df.iloc[i][6])
print(df)

dx = df.groupby(by=[df["J1"], df["W1"], df["J2"], df["W2"]])
di = dx.count()["userid"]
print(di)
"""
print("----------------------------")
print(df.shape, "    ", df.shape[0])
print("----------------------------")
c1 = df["geohashed_start_loc"]
c2 = df["geohashed_end_loc"]
print("----------------------------")
d1 = np.array(c1)
d2 = np.array(c2)
print(d1)
print("----------------------------")
e1 = list(map(geohash2.decode, d1))
e2 = list(map(geohash2.decode, d2))
#f1 = np.dstack(e1, e2)
xa = pd.DataFrame(columns=["J1", "W1", "J2", "W2"])
for i in range(len(e1)):
    xa = xa.append({"J1": float(e1[i][0]), "W1": float(
        e1[i][1]), "J2": float(e2[i][0]), "W2": float(e2[i][1])}, ignore_index=True)
print(xa)

su = df.join(xa)
print(su)

dx = su.groupby(by=[su["J1"], su["W1"], su["J2"], su["W2"]])
di = dx.count()["userid"]
print(di)
"""

"""
x = [float(b[0]) for b in e]
print(x)
print("----------------------------")
sx = df.loc[1]["userid": "starttime"]
print(sx)
print("----------------------------")
d1 = np.array(df["biketype"])
print(d1)
print("----------------------------")
dp = df[df["biketype"] == 1]
print(dp)
print("----------------------------")
dx = dp.groupby(by=[df["geohashed_start_loc"], df["geohashed_end_loc"]])
di = dx.count()["userid"]
print(di)
print("----------------------------")
x1 = pd.DataFrame(data=e, index=[i for i in range(len(e))] , columns=["N"])
x2 = df.merge(x1, how="outer")
print(x2)
"""

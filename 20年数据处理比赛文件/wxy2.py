import pandas as pd
import numpy as np
import geohash2
import math

df = pd.read_csv(
    "D:\\Program_file\\python_file\\python.con\\mobike_train_data.csv")
df = df[:30]
df["J1"] = np.nan
df["W1"] = np.nan
df["J2"] = np.nan
df["W2"] = np.nan
df["distance"] = np.nan
Sum = 0
for i in range(df.shape[0]):
    df.iloc[i, 7], df.iloc[i, 8] = geohash2.decode(df.iloc[i][5])
    df.iloc[i, 7], df.iloc[i, 8] = float(df.iloc[i, 7]), float(df.iloc[i, 8])
    df.iloc[i, 9], df.iloc[i, 10] = geohash2.decode(df.iloc[i][6])
    df.iloc[i, 9], df.iloc[i, 10] = float(df.iloc[i, 9]), float(df.iloc[i, 10])
    X = math.sin(df.iloc[i, 8])*math.sin(df.iloc[i, 10])+math.cos(df.iloc[i, 8]) * \
        math.cos(df.iloc[i, 10]) * math.cos(df.iloc[i, 7] - df.iloc[i, 9])
    X = float("{:.6f}".format(X))
    df.iloc[i, 11] == math.acos(X)*6371000
    #df.iloc[i, 11] = C
    Sum += df.iloc[i, 11]
average = Sum / df.shape[0]
print(df)
print(average)

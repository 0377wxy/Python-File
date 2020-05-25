import numpy as np
import pandas as pd
import geohash2
import re
import matplotlib.pyplot as plt
from math import radians, cos, sin, asin, sqrt,atan,tan,acos, fabs
import math

df = pd.read_csv('D:/1.csv')


#df.userid.unique().size
#df.biketype.unique().size
df = df.sample(frac=0.001)


start = pd.DataFrame(columns=['j1', 'w1'])
end = pd.DataFrame(columns=['j2', 'w2'])
#distance = []


for i in range(df.shape[0]):
        start = start.append(
            [{'j1': geohash2.decode(df.iloc[i][5])[0], 'w1': geohash2.decode(df.iloc[i][5])[1], }], ignore_index=True)
        end = end.append(
            [{'j2': geohash2.decode(df.iloc[i][6])[0], 'w2':geohash2.decode(df.iloc[i][6])[1], }], ignore_index=True)


def get_distance_hav(lon1, lat1, lon2, lat2): 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2*asin(sqrt(a))*6371*1000 
    c = round(c/1000, 3)
    return c
'''
def hav(theta):
    s = sin(theta / 2)
    return s * s

def get_distance_hav(lat0, lng0, lat1, lng1):
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    lng0 = radians(lng0)
    lng1 = radians(lng1)
    dlng = fabs(lng0 - lng1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
    distance = 2 * 6371 * asin(sqrt(h))
 
    return distance
'''
distance1 = []

for i in range (start.shape[0]):
    distance1.append(get_distance_hav(float(start.iloc[i][1]),float(start.iloc[i][0]),float(end.iloc[i][1]),float(end.iloc[i][0])))


sns = plt.figure()
start_end_distance = df["distance1"]
start_end_distance = start_end_distance.loc[start_end_distance<5000]
sns.distplot(start_end_distance)
plt.show()


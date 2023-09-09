from re import X
import socket
import numpy as np
import matplotlib.pyplot as plt
import math

# 创建一个客户端的socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置服务端的ip地址
host = "192.168.43.250"
# 设置端口
port = 8266
# 连接服务端
client.connect((host, port))

print("连接完成")

acc = [i for i in range(9)]

acc_fix = [0, 0, 0]
acc_sum = [0, 0, 0, 0]
acc_aver = [0, 0, 0]

gry_sum = [0, 0, 0]
gry_e = [0, 0, 0]
gry_fix = [0, 0, 0]

plt.axis([0, 300, -1.5, 1.5])
plt.ion()

xs = [0, 0]
y1 = [0, 0]
y2 = [0, 0]
y3 = [0, 0]

j = 0
v = 0


'''
x = -0.0186379793976819
y = 0.0139829653389583
z = 0.113640075656928
k1 = 0.981822364557898
k2 = 0.977233901465048
k3 = 0.958756265236508
'''
x = -0.0186453641113768
y = 0.0143049921931562
z = 0.113666102894666
k1 = 0.981834341086976
k2 = 0.977472681652496
k3 = 0.958741749125294

sum_aa = [0, 0, 0, 0, 0, 0]
aver_aa = [0, 0, 0, 0, 0, 0]


for j in range(400):

    msg = client.recv(1024)
    for i in range(6):
        val = int.from_bytes(msg[2*i: 2*i+2], byteorder='little', signed=True)
        acc[i] = val
    for i in range(3):
        acc[i] = acc[i] / 16384
    for i in range(3, 6):
        acc[i] = acc[i] * 250 / 32768

    print(j, end="  ")
    for i in range(6):
        print(acc[i], end="   ")
    print("")

    for i in range(6):
        sum_aa[i] += acc[i]


for i in range(6):
    aver_aa[i] = sum_aa[i] / 400
aver_aa[2] -= 0.97936
for i in range(3):
    aver_aa[i] = aver_aa[i] * 16384
for i in range(3, 6):
    aver_aa[i] = aver_aa[i] / 250 * 32768

for i in range(6):
    print(aver_aa[i], end="   ")

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

for i in range(100):

    msg = client.recv(1024)
    for i in range(6):
        val = int.from_bytes(msg[2*i: 2*i+2], byteorder='little', signed=True)
        acc[i] = val
    for i in range(3):
        acc[i] = acc[i] / 16384
    for i in range(3, 6):
        acc[i] = acc[i] * 250 / 32768

    acc_fix[0] = acc[0] * k1 + x
    acc_fix[1] = acc[1] * k2 + y
    acc_fix[2] = acc[2] * k3 + z

    acc_sum[0] += acc_fix[0]
    acc_sum[1] += acc_fix[1]
    acc_sum[2] += acc_fix[2]

    gry_sum[0] += acc[3]
    gry_sum[1] += acc[4]
    gry_sum[2] += acc[5]


x = acc_sum[0]/100
y = acc_sum[1]/100
z = acc_sum[2]/100

gry_e[0] = gry_sum[0] / 100
gry_e[1] = gry_sum[1] / 100
gry_e[2] = gry_sum[2] / 100


an1 = math.acos(math.sqrt(x**2+z**2)/math.sqrt(x**2+y**2+z**2))
an2 = math.acos(math.sqrt(y**2+z**2)/math.sqrt(x**2+y**2+z**2))
an3 = math.acos(math.sqrt(x**2+y**2)/math.sqrt(x**2+y**2+z**2))


x = -0.0186453641113768
y = 0.0143049921931562
z = 0.113666102894666
k1 = 0.981834341086976
k2 = 0.977472681652496
k3 = 0.958741749125294


while True:

    j = j+1
    msg = client.recv(1024)

    for i in range(6):
        val = int.from_bytes(msg[2*i: 2*i+2], byteorder='little', signed=True)
        acc[i] = val
    for i in range(3):
        acc[i] = acc[i] / 16384
    for i in range(3, 6):
        acc[i] = acc[i] * 250 / 32768

    acc_fix[0] = acc[0] * k1 + x
    acc_fix[1] = acc[1] * k2 + y
    acc_fix[2] = acc[2] * k3 + z

    acc_sum[0] += acc_fix[0]
    acc_sum[1] += acc_fix[1]
    acc_sum[2] += acc_fix[2]

    acc_aver[0] = acc_sum[0]/j
    acc_aver[1] = acc_sum[1]/j
    acc_aver[2] = acc_sum[2]/j

    gry_fix[0] = acc[3] - gry_e[0]
    gry_fix[1] = acc[4] - gry_e[1]
    gry_fix[2] = acc[5] - gry_e[2]

    acc_sum[3] = math.sqrt((acc_fix[0])**2 +
                           (acc_fix[1])**2 +
                           (acc_fix[2])**2)

    print(sum[0], end="  ")
    print(acc[6], end="  ")
    print(acc[7], end="  ")
    print(acc[8], end="  ")
    print(sum[3])

    xs[0] = xs[1]
    xs[1] = j

    y1[0] = y1[1]
    y1[1] = acc[0]*0.6+y1[0]*0.4

    y2[0] = y2[1]
    y2[1] = acc[1]

    y3[0] = y3[1]
    y3[1] = y3[0]+acc[0]

    plt.plot(xs, y1, color='b')
    #plt.plot(xs, y3, color='r')
    #plt.plot(xs, y2, color='g')
    plt.pause(0.1)


# 关闭客户端
client.close()

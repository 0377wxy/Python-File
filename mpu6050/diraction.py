from re import X
import socket
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import math
import time
from mpl_toolkits.mplot3d import Axes3D

# 原始数据，直接从WIFI接收
raw_data_acc = [0, 0, 0]
raw_data_ang = [0, 0, 0]

# 加速度纠正参数
ex = -0.0186453641113768
ey = 0.0143049921931562
ez = 0.113666102894666
k1 = 0.981834341086976
k2 = 0.977472681652496
k3 = 0.958741749125294

# 角速度的零偏
ang_dev = [0, 0, 0]

# 纠正后加速度
acc_fix = [0, 0, 0]

# 纠正后角速度
ang_fix = [0, 0, 0]

# 由重力决定的方向的 直角坐标
rec_coordinate = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# 由重力决定的方向的 角度坐标（与面的夹角）
ang_coordinate = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# 由重力决定的方向的 角度坐标（与轴的夹角），cos值
cos_coordinate = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 加速度在重力坐标下的分解
acc_resolution = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 加速度在重力坐标下的合并
acc_merge = [0, 0, 0]

# 加速度的累计
acc_sum = [0, 0, 0]

pic_dir = [[], [], []]


# 连接到WIFI


def Tcp_Connection():
    # 创建一个客户端的socket对象
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置服务端的ip地址
    host = "192.168.43.250"
    # 设置端口
    port = 8266
    # 连接服务端
    client.connect((host, port))
    print("tcp连接成功")


# 关闭客户端


def Tcp_Close():
    client.close()


# 叉乘 A X B = C


def Cross_Product(A, B, C):
    C[0] = A[1] * B[2] - A[2] * B[1]
    C[1] = -(A[0] * B[2] - A[2] * B[0])
    C[2] = A[0] * B[1] - A[1] * B[0]


# 计算角加速度计零偏，获取g的方向


def Start_Up_Preparation():

    # 读取次数
    frequency = 100

    # 加速度、加速度累积
    acc_fix_sum = [0, 0, 0]
    ang_sum = [0, 0, 0]

    # 读数据
    for i in range(frequency):

        # 读取
        msg = client.recv(1024)
        # print(time.time())
        for i in range(6):
            val = int.from_bytes(
                msg[2*i: 2*i+2], byteorder='little', signed=True)
            if i < 3:
                raw_data_acc[i] = val
            else:
                raw_data_ang[i-3] = val

        # 单位变化
        for i in range(3):
            raw_data_acc[i] = raw_data_acc[i] / 16384
            raw_data_ang[i] = raw_data_ang[i] * 250 / 32768

        # 加速度纠正
        acc_fix[0] = raw_data_acc[0] * k1 + ex
        acc_fix[1] = raw_data_acc[1] * k2 + ey
        acc_fix[2] = raw_data_acc[2] * k3 + ez

        # 累计加速度与角速度
        for i in range(3):
            acc_fix_sum[i] += acc_fix[i]
            ang_sum[i] += raw_data_ang[i]

    # 关tcp
    Tcp_Close()
    print("初始读取结束")

    # 加速度均值，z坐标方向
    for i in range(3):
        rec_coordinate[2][i] = acc_fix_sum[i]/frequency

    # 角速度均值，零偏
    for i in range(3):
        ang_dev[i] = ang_sum[i]/frequency

    # y坐标方向
    Cross_Product([1, 0, 0], rec_coordinate[2], rec_coordinate[1])

    # x坐标方向
    Cross_Product(rec_coordinate[2], rec_coordinate[1], rec_coordinate[0])


# 计算初始角度坐标(单位/弧度)


def Ang_Coordinate_Calculation():
    for i in range(3):
        length = \
            math.sqrt(rec_coordinate[i][0]**2 +
                      rec_coordinate[i][1]**2 +
                      rec_coordinate[i][2]**2)
        ang_coordinate[i][0] = math.acos(
            math.sqrt(rec_coordinate[i][1]**2 +
                      rec_coordinate[i][2]**2) / length)
        ang_coordinate[i][1] = math.acos(
            math.sqrt(rec_coordinate[i][0]**2 +
                      rec_coordinate[i][2]**2) / length)
        ang_coordinate[i][2] = math.acos(
            math.sqrt(rec_coordinate[i][0]**2 +
                      rec_coordinate[i][1]**2) / length)

        for j in range(3):
            if rec_coordinate[i][j] < 0:
                ang_coordinate[i][j] = -ang_coordinate[i][j]


# 姿态改变


def Posture_Change():

    ang_sum = [0, 0, 0]

    # plt.ion()
    x1 = [0, 1]
    y1 = [0, 1]
    z1 = [0, 1]

    # 读数据
    for k in range(500):

        # 读取
        msg = client.recv(1024)
        # print(time.time())
        for i in range(6):
            val = int.from_bytes(
                msg[2*i: 2*i+2], byteorder='little', signed=True)
            if i < 3:
                raw_data_acc[i] = val
            else:
                raw_data_ang[i-3] = val

        # 单位变化
        for i in range(3):
            raw_data_acc[i] = raw_data_acc[i] / 16384
            raw_data_ang[i] = raw_data_ang[i] * 250 / 32768

        # 加速度纠正
        acc_fix[0] = raw_data_acc[0] * k1 + ex
        acc_fix[1] = raw_data_acc[1] * k2 + ey
        acc_fix[2] = raw_data_acc[2] * k3 + ez

        # 角速度纠正，单位变为：弧度
        for i in range(3):
            ang_fix[i] = math.radians(raw_data_ang[i] - ang_dev[i])
            ang_sum[i] += ang_fix[i] * 0.02

        # 转动角度累计
        for i in range(3):
            ang_coordinate[i][1] -= ang_fix[0] * 0.02
            ang_coordinate[i][2] += ang_fix[0] * 0.02

            ang_coordinate[i][2] -= ang_fix[1] * 0.02
            ang_coordinate[i][0] += ang_fix[1] * 0.02

            ang_coordinate[i][0] += ang_fix[2] * 0.02
            ang_coordinate[i][1] -= ang_fix[2] * 0.02

        # 计算与轴的夹角
        for i in range(3):
            for j in range(3):
                cos_coordinate[i][j] = math.pi/2 - ang_coordinate[i][j]

        # 计算加速度的分解
        for i in range(3):
            for j in range(3):
                acc_resolution[i][j] = acc_fix[j] * \
                    math.cos(cos_coordinate[i][j])

        # 加速度在重力坐标方向上合并
        for i in range(3):
            acc_merge[i] = 0
            for j in range(3):
                acc_merge[i] += acc_resolution[i][j]
        acc_merge[2] = acc_merge[2]-0.97936

        for i in range(3):
            acc_sum[i] += int(acc_merge[i] * 0.02 * 1000) / 1000
        #print(acc_sum[0], acc_sum[1], acc_sum[2])
        #print(acc_merge[0], acc_merge[1], acc_merge[2])
        #print(acc_fix[0],  acc_fix[1],  acc_fix[2])
        #print(acc_resolution[2][0],  acc_resolution[2][1],  acc_resolution[2][2])
        #print(ang_sum[0], ang_sum[1], ang_sum[2], time.time())
        #print(ang_coordinate[2][0],  ang_coordinate[2][1],  ang_coordinate[2][2])
        print(cos_coordinate[2][0],  cos_coordinate[2]
              [1],  cos_coordinate[2][2])

        for i in range(3):
            pic_dir[i].append([cos_coordinate[i][0],
                               cos_coordinate[i][1],
                               cos_coordinate[i][2]])

        # print(time.time())
'''
        plt.ioff()  # 关闭画图窗口
        plt.clf()  # 清除之前画的图
        fig = plt.gcf()  # 获取当前图
        ax = fig.gca(projection='3d')  # 获取当前轴
        ax.set_xlim3d(-1, 1)
        ax.set_ylim3d(-1, 1)
        ax.set_zlim3d(-1, 1)
        x1[1] = math.cos(cos_coordinate[2][0])
        y1[1] = math.cos(cos_coordinate[2][1])
        z1[1] = -math.cos(cos_coordinate[2][2])
        ax.plot(x1, y1, z1)
        x1[1] = math.cos(cos_coordinate[1][0])
        y1[1] = math.cos(cos_coordinate[1][1])
        z1[1] = -math.cos(cos_coordinate[1][2])
        ax.plot(x1, y1, z1)
        x1[1] = math.cos(cos_coordinate[0][0])
        y1[1] = math.cos(cos_coordinate[0][1])
        z1[1] = -math.cos(cos_coordinate[0][2])
        ax.plot(x1, y1, z1)
'''
#print(ang_coordinate[2][0], ang_coordinate[2][1], ang_coordinate[2][2])

# plt.pause(0.001)


# 主函数
Tcp_Connection()
Start_Up_Preparation()
Ang_Coordinate_Calculation()

print("角度坐标（单位/度）：")
for i in range(3):
    s = 0
    for j in range(3):
        print(math.degrees(ang_coordinate[i][j]), end="   ")
        s += ang_coordinate[i][j]**2
    print("")

print("角速度零偏（单位/度）")
for i in range(3):
    print(ang_dev[i], end="  ")
print("")

print("初始化完成")

Tcp_Connection()
Posture_Change()


plt.ion()
x1 = [0, 1]
y1 = [0, 1]
z1 = [0, 1]
print(len(pic_dir[0]))
for i in range(len(pic_dir[0])):

    plt.clf()  # 清除之前画的图
    fig = plt.gcf()  # 获取当前图
    ax = fig.gca(projection='3d')  # 获取当前轴
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)
    x1[1] = math.cos(pic_dir[0][i][0])
    y1[1] = math.cos(pic_dir[0][i][1])
    z1[1] = -math.cos(pic_dir[0][i][2])
    print(pic_dir[0][i][0], pic_dir[0][i][1], pic_dir[0][i][2])
    ax.plot(x1, y1, z1)
    x1[1] = math.cos(pic_dir[1][i][0])
    y1[1] = math.cos(pic_dir[1][i][1])
    z1[1] = -math.cos(pic_dir[1][i][2])
    ax.plot(x1, y1, z1)
    x1[1] = math.cos(pic_dir[2][i][0])
    y1[1] = math.cos(pic_dir[2][i][1])
    z1[1] = -math.cos(pic_dir[2][i][2])
    ax.plot(x1, y1, z1)
    plt.pause(0.02)
    plt.ioff()  # 关闭画图窗口
plt.show()

from re import X
import socket
import numpy as np
import matplotlib.pyplot as plt
import math
import time
import serial

ser = serial.Serial(port="COM4",
                    baudrate=57600,
                    bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    timeout=None)    # 打开COM17，将波特率配置为115200，其余参数使用默认值
if ser.isOpen():                        # 判断串口是否成功打开
    print("打开串口成功。")
    print(ser.name)    # 输出串口号
else:
    print("打开串口失败。")


# 创建一个客户端的socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置服务端的ip地址
host = "192.168.43.250"
# 设置端口
port = 8266
# 连接服务端
client.connect((host, port))

print("连接完成")

a = time.time()


acc = [0, 0, 0]
acc_change = [0, 0, 0]
acc_sum = [0, 0, 0]
dis = [0, 0, 0]
t = time.time()
order = 0

while(1):

    msg = client.recv(1024)

    for i in range(3):
        val = int.from_bytes(
            msg[2*i: 2*i+2], byteorder='little', signed=True)
        acc[i] = val

    write_len = ser.write(msg[0:6])

    for i in range(3):
        print('%d' % acc[i], end="   ")
    print(time.time()-t, time.time()-a)
    t = time.time()

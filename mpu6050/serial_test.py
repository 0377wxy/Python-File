import serial
import time

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


bytes_temp = b'\x23\x23\x34\x25\x56\x67\x78\x89\x90'


while(1):
    #write_len = ser.write("ABCDEFG".encode('utf-8'))
    # ("串口发出{}个字节。".format(write_len))
    write_len = ser.write(bytes_temp[0:6])
    ("串口发出{}个字节。".format(write_len))

    time.sleep(1)

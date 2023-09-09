import socket

# 链接服务端
HOST = '192.168.91.130'    # The remote host
PORT = 8001           # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# 数据请求
while True:
    msg = bytes(input(">>:"), encoding="utf8")
    s.sendall(msg)
    data = s.recv(1024)
    # print(data)

    # repr格式化输出
    print('Received', repr(data))
s.close()

import socket

s = socket.socket()
s.connect(('192.168.1.103', 8099))  # 连接服务器端
while True:
    data = input('自己：')
    s.send(data.encode())  # 发送数据
    recvMsg = s.recv(1024).decode()
    print(recvMsg)
    if data == 'close':
        break
        s.close()
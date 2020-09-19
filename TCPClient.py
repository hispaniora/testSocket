import socket

s = socket.socket()
s.connect(('192.168.0.104', 8099))  # 连接服务器端
while True:
    data = input('自己：')
    s.send(data.encode())  # 发送数据
    recvMsg = s.recv(1024).decode()
    print('服务器端：', recvMsg)
    if data == 'close':
        break
s.close()

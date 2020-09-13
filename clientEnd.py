import socket

# 客户端使用UDP时，无需建立连接，直接用sendto()给服务器发信息
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('客户端——')
while True:
    data = input('自己：')
    s.sendto(data.encode(), ('192.168.0.104', 8099))  # 客户端明确知道服务器端的IP和port
    recvMsg = s.recv(1024)  # 接收返回的信息
    print('服务器:', recvMsg.decode())

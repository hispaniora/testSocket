import socket

# 客户端使用UDP时，无需建立连接，直接用sendto()给服务器发信息
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = input('请输入发送内容：')
s.sendto(data.encode(), ('127.0.0.1', 8099))  # 发送信息
recvMsg = s.recv(1024)  # 接收返回的信息
print(recvMsg.decode())
s.close()

import socket

# SOCK_DGRAM指定了这个socket是UDP类型
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定地址和端口
s.bind(('127.0.0.1', 8099))
print('服务器端——')
while True:
    # 接收数据，自动阻塞等待客户端请求
    data, addr = s.recvfrom(1024)  # 接收客户端发送过来的数据内容和地址
    data = data.decode()
    print(addr, ':', data)
    msg = input('回复：')
    s.sendto(msg.encode(), addr)  # 给客户端发送消息

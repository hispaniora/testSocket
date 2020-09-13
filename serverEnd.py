import socket

# SOCK_DGRAM指定了这个socket是UDP类型
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定地址和端口
s.bind(('192.168.0.104', 8099))  # 服务器端绑定自己的IP和端口号，客户端端口可以不用绑定用随机分配的
print('服务器端——')
while True:
    # 接收数据，自动阻塞等待客户端请求
    data, addr = s.recvfrom(1024)  # 接收客户端发送过来的数据内容和地址，recvfrom(1024)返回的是数组
    ip, port = addr  # 将数组格式的地址拆分为ip和port
    data = data.decode()
    print(ip, '-', port, ':', data)
    msg = input('回复：')
    s.sendto(msg.encode(), addr)  # 给客户端发送消息

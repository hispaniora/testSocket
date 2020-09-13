import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM表示为TCP连接
s.bind(('192.168.1.103', 8099))  # 服务器端绑定自己的IP和端口号
s.listen(128)  # 设置监听，同时能连接的客户端数
while True:
    print('等待下一个客户端的消息……')
    client, addr = s.accept()  # 接收到客户端的socket和地址
    print('接收到client数据', addr)
    while True:
        data = client.recv(1024)  # 获取客户端的信息
        data = data.decode()
        ip, port = addr
        if not data or data == 'bye':
            # 如果没有发送过来数据就表示客户端close了，或者发送‘bye’表示要断开
            print('服务结束', addr)
            client.close()  # 断开连接
        else:
            print(ip, '-', port, ':', data)
            msg = input('回复：')
            client.send(msg.encode())  # 给客户端回复
    s.close()

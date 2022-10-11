import socket

# 1）创建客户端套接字对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2）和服务端套接字建立连接
client_socket.connect(('127.0.0.1', 8080))

# 3）接收数据
while True:
    recv_msg = client_socket.recv(1024)
    print(f'当前北京时间：{recv_msg.decode()}')

# 4）关闭客户端套接字
client_socket.close()
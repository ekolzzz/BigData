"""
TCP客户端程序开发
学习目标：理解 TCP 客户端程序的开发流程
"""
import socket
"""
TCP客户端程序开发步骤：
1）创建客户端套接字对象
2）和服务端套接字建立连接
3）发送数据
4）接收数据
5）关闭客户端套接字
"""

# 1）创建客户端套接字对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2）和服务端套接字建立连接
client_socket.connect(('127.0.0.1', 8080))

# 3）发送数据
send_msg = input('请输入发送给服务端的消息：')
client_socket.send(send_msg.encode())
# 4）接收数据
recv_msg = client_socket.recv(1024)
print(f'接收到服务端的响应消息：{recv_msg.decode()}')

# 5）关闭客户端套接字
client_socket.close()
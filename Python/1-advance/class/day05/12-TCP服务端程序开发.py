"""
TCP 服务端程序开发
学习目标：理解 TCP 服务端程序的开发流程
"""
import socket
"""
TCP服务端程序开发步骤：
1）创建服务端监听套接字对象
2）绑定端口号
3）设置监听
4）等待接受客户端的连接请求
5）接收数据
6）发送数据
7）关闭套接字
"""
# 1）创建服务端监听套接字对象
# socket.AF_INET：表示使用IPV4
# socket.SOCK_STREAM：表示使用TCP协议
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2）绑定端口号
server_socket.bind(('127.0.0.1', 8080))

# 3）设置监听
server_socket.listen(128)
print('服务器开始监听...')

# 4）等待接受客户端的连接请求
# service_client_socket：也是一个socket 类的对像，专门和客户端通信的套接字
# ip_port：客户端的 IP 地址和端口号
service_client_socket, ip_port = server_socket.accept()
print(f'服务器接收到来自{ip_port}的请求')

# 5）接收数据
# 接收客户端发送的消息，最多接收 1024 给字节
recv_msg = service_client_socket.recv(1024) # 接收的消息为 bytes 类型
print('客户端发送的消息为：', recv_msg.decode())

# 6）# 给客户端发送响应消息
send_msg = input('请输入响应的消息：') # type(send_msg) -> str
service_client_socket.send(send_msg.encode())

# 7）关闭服务端的 socket
# 没有先后
service_client_socket.close()
server_socket.close()








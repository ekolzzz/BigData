"""
TCP 服务端程序开发
学习目标：理解 TCP 服务端程序的开发流程
"""
import socket

# ① 创建一个服务端的socket【用于接收客户端的连接请求，理解为：门童、门迎】
# socket.AF_INET：表示使用 IPV4 的地址
# socket.SOCK_STREAM：表示使用 TCP 协议
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ② 设置服务端使用的 IP 和 端口
# server_socket.bind(('127.0.0.1', 8080))
server_socket.bind(('192.168.33.75', 8080))

# ③ 设置服务端同一时间最多可以接收多少个客户端的连接请求
server_socket.listen(128)

# ④ 设置完成，等待接收客户端的连接请求
print('服务端等待接收客户端的连接请求...')
# service_client_socket：也是一个 socket 类的对象【负责和连接的客户端进行数据的接收和发送，理解为：专门的服务员】
service_client_socket, ip_port = server_socket.accept()
print(f'接收到来自于{ip_port}的连接...')

# ⑤ 接收客户端发送的消息
# 1024：一次 recv，最多接收多个字节
# 当另外一端没有发送信息过来时，recv也会阻塞等待
recv_msg = service_client_socket.recv(1024) # bytes
print(f'客户端发送的消息为：{recv_msg.decode()}')

# ⑥ 给客户端发送响应的消息
send_msg = input('请输入给客户端回应的消息：') # str
service_client_socket.send(send_msg.encode())

# ⑦ 关闭服务端的 socket
service_client_socket.close()
server_socket.close()
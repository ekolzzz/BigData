"""
TCP客户端程序开发
学习目标：理解 TCP 客户端程序的开发流程
"""
import socket

# ① 创建一个客户端 socket
# socket.AF_INET：表示使用 IPV4 的地址
# socket.SOCK_STREAM：表示使用 TCP 协议
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 注意：通常来说，TCP客户端程序不需要设置ip和端口，程序运行之后，操作系统会自动给客户端程序分配一个端口

# ② 通过客户端的 socket 连接服务端程序
client_socket.connect(('192.168.33.75', 8080))

# ③ 客户端给服务端发送消息
send_msg = input('请输入发送给服务端的消息：') # str
client_socket.send(send_msg.encode())

# ④ 客户端接收服务端的响应消息
recv_msg = client_socket.recv(1024) # bytes
print(f'接收到服务端的响应消息：{recv_msg.decode()}')

# ⑤ 关闭客户端的 socket
client_socket.close()
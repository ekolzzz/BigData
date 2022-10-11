"""
Web 服务器
"""
import socket
import os

# 创建一个服务端监听套接字socket对象（门迎）
# socket.AF_INET：表示使用IPV4
# socket.SOCK_STREAM：表示使用 TCP 协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定服务端程序监听 IP 和 PORT
server.bind(('127.0.0.1', 8080))

# 设置服务器监听，127表示同一时间处理127个客户端连接请求
server.listen(127)
print('服务器开始进行监听……')

while True:
    # 等待接收客户端的连接：如果没有客户端连接时，这句代码会阻塞等待，知道有客户端连接
    # server_client：和客户端进行通信的 socket 对象 （服务员）
    # ip_port：客户端的 IP 和 PORT
    server_client, ip_port = server.accept()
    print(f'接收到来自客户端{ip_port}的连接请求……')

    # 接收客户端发送的消息，1024表示最多接收1024个字节
    # 如果客户端没有发消息，recv方法会阻塞等待
    recv_msg = server_client.recv(1024) # 返回值是 bytes 类型
    print('客户端发送的消息为：')
    print(recv_msg.decode())

    # 组织一个响应报文，发送给浏览器
    # 响应行
    response_line = b'HTTP/1.1 200 OK\r\n'
    # 响应头
    response_headers = b'Server: YYDS;\r\nContent-Type: text/html;charset=utf-8\r\n'
    # 空行

    # 响应体
    # 1）返回 Hello, World!
    # response_body = '<h1>Hello, World!</h1>'

    # 2) 返回固定 html 内容
    # with open('./sources/html/gdp.html', 'r', encoding='utf=8') as f:
    #     response_body = f.read()

    # 3) 返回任意 html 内容
    # request_msg = recv_msg.decode() # str
    # request_line = request_msg.split('\r\n') # list
    # request_line_tags = request_line[0].split(' ') # list
    # request_url = request_line_tags[1]

    request_url = recv_msg.decode().split('\r\n')[0].split(' ')[1]

    if request_url == '/':
        file_path = '../sources/html/gdp.html'
    else:
        file_path = '../sources/html' + request_url

    if os.path.isfile(file_path):
        with open(file_path, 'rb') as f:
            response_body = f.read()
    else:
        response_body = b'<h1>Not Found!</h1>'

    # 拼接成一个响应报文
    response_msg = response_line + response_headers + b'\r\n' + response_body
    # 将响应报文的内容发送给浏览器
    server_client.send(response_msg)
    # 关闭和客户端通信的套接字、监听套接字
    server_client.close()

server.close()














"""
简单Web服务器-返回任意html内容
学习目标：能够实现Web服务器给浏览器返回任意html内容
"""
import os
import socket

# 创建一个服务端监听套接字socket对象
# socket.AF_INET：表示使用 IPV4 地址
# socket.SOCK_STREAM：表示使用 TCP 协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 门迎

# 绑定服务端程序监听的 IP 和 PORT
server.bind(('127.0.0.1', 8080))

# 设置服务器监听，127表示同一时间最多处理127个客户端连接请求
server.listen(127)
print('服务器开始进行监听...')


while True:
    # 等待接受客户端的连接：如果没有客户端连接时，这句代码会阻塞等待，直到有客户端连接
    # server_client：和客户端进行通信的 socket 对象，服务员
    # ip_port：客户端的 IP 和 Port
    server_client, ip_port = server.accept()
    print(f'接受到来自客户端{ip_port}的连接请求...')

    # 接受客户端发送的消息，1024表示最多接受1024个字节
    # 如果客户端没有发消息，recv方法会阻塞等待
    recv_msg = server_client.recv(1024) # 返回值是 bytes 类型
    print('客户端发送的消息为：')
    print(recv_msg.decode())
    # TODO：解析请求报文，从请求报文中提取资源路径
    request_msg = recv_msg.decode() # str
    # 首先将请求报文按照 \r\n 进行分割，分割之后获取请求行的内容
    request_tags = request_msg.split('\r\n') # list
    request_line = request_tags[0]
    # 然后将请求行按照空格进行分割，分割之后获取资源路径
    request_line_tags = request_line.split(' ') # list
    request_url = request_line_tags[1]
    print('提取的资源路径为：', request_url)

    # 组织一个响应报文，发送给浏览器
    # 响应行
    response_line = 'HTTP/1.1 200 OK\r\n'
    # 响应头
    response_headers = 'Server: YYDS;\r\nContent-Type: text/html;charset=utf-8\r\n'
    # 响应体
    # TODO: 根据请求的资源来读取对应网页的内容，作为响应报文中的响应体
    # 如果访问的资源路径是 /，默认返回 gdp.html 的内容
    if request_url == '/':
        file_path = './sources/html/gdp.html'
    else:
        # 拼接完整路径
        file_path = './sources/html' + request_url

    # 先判断文件是否存在，存在才读取，否则将响应体设置为：Not Found!
    if os.path.isfile(file_path):
        # 文件存在
        with open(file_path, 'r', encoding='utf8') as f:
            response_body = f.read()
    else:
        # 文件不存在
        response_body = 'Not Found!'

    # 拼接成一个响应报文
    response_msg = response_line + response_headers + '\r\n' + response_body
    # 将响应报文的内容发送给浏览器
    server_client.send(response_msg.encode())

    # 关闭和客户端通信的套接字、监听套接字
    server_client.close()

server.close()






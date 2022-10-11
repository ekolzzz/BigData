import socket
import time
import datetime

# 1）创建服务端监听套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2）绑定端口号
server_socket.bind(('127.0.0.1', 8888))

# 3）设置监听
server_socket.listen(128)
print('服务器开始监听...')

# 4）等待接受客户端的连接请求
# service_client_socket：也是一个socket 类的对像，专门和客户端通信的套接字
# ip_port：客户端的 IP 地址和端口号
service_client_socket, ip_port = server_socket.accept()
print(f'服务器接收到来自{ip_port}的时间请求')

# 5）给客户端发送时间

while True:
    # 获取代码执行时间的当前时间
    over_time = datetime.datetime(2022, 5, 23)
    now_time = datetime.datetime.now()
    result = now_time - over_time

    hours = int(result.seconds / 3600)
    minutes = int(result.seconds % 3600 / 60)
    seconds = result.seconds % 3600 % 60

    time_str = f'{result.days}天{hours}时{minutes}分{seconds}秒'
    time.sleep(1)  # 每隔一秒

    service_client_socket.send(time_str.encode())
# 6）关闭服务端的 socket
# 没有先后
service_client_socket.close()
server_socket.close()
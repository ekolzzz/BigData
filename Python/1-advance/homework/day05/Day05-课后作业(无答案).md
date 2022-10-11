[TOC]

## Python进阶-day05

### 基础概念题

#### 1. 什么是IP地址？如何查看IP地址？

**参考答案:**

```bash
# 你的答案
IP地址：通俗点讲就是电脑身份证，是标识网络中唯一的一台设备，是IP协议提供的一种统一的地址格式，它为互联网上的每一个网络和每一台主机分配一个逻辑地址，以此来屏蔽物理地址的差异。
Windows： ipconfig
MacOS/Linux：ifconfig
```

#### 2. 什么是端口？什么是端口号？知名端口号和动态端口号的范围是什么？

**参考答案:**

```bash
# 你的答案
端口是用来给运行的应用程序提供传输数据的通道。
端口号是用来区分和管理不同端口的，通过端口号能找到唯一个的一个端口。
知名端口号：1-1023
动态端口号：1024-65535
```

#### 3. TCP 协议是什么？有什么特点？

**参考答案:**

```bash
# 你的答案
TCP协议是网络传输控制协议
特点：
面向连接(三次握手)
可靠传输：保证数据不丢包\不乱序
```

#### 4. 什么是socket？

**参考答案:**

```bash
# 你的答案
socket (简称 套接字) 是进程之间通信一个工具，是操作系统提供的网络编程接口，屏蔽通过TCP/IP及端口进行网络数据传输的细节
```

### 代码练习题

#### 1. 完成课上的代码【1-3遍】

#### 2. 编写一个TCP网络程序，功能如下：

1）客户端：每隔1秒中，将客户端的时间发送给服务器

```python
from datetime import datetime
# 获取代码执行时间的当前时间
now_time = datetime.now()
# 将时间格式化成字符串
time_str = now_time.strftime("%Y-%m-%d %H:%M:%S")
```

2）服务端：每次接收到客户端发送的时间，进行打印显示

**参考答案**：

1）客户端程序

```python
import socket

# 1）创建客户端套接字对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2）和服务端套接字建立连接
client_socket.connect(('127.0.0.1', 8080))

# 3）接收数据
while True:
    recv_msg = client_socket.recv(1024)
    print(f'北京时间：{recv_msg.decode()}')

# 4）关闭客户端套接字
client_socket.close()
```

2）服务端程序

```python
import socket
import time
from datetime import datetime

# 1）创建服务端监听套接字
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
print(f'服务器接收到来自{ip_port}的时间请求')

# 5）给客户端发送时间

while True:
    # 获取代码执行时间的当前时间
    now_time = datetime.now()
    
    # 将时间格式化成字符串
    time_str = now_time.strftime("%Y-%m-%d %H:%M:%S")
    time.sleep(1)  # 每隔一秒
    service_client_socket.send(time_str.encode())

# 6）关闭服务端的 socket
# 没有先后
service_client_socket.close()
server_socket.close()
```

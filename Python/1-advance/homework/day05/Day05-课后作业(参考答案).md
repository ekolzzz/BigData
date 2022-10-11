[TOC]

## Python进阶-day05

### 基础概念题

#### 1. 什么是IP地址？如何查看IP地址？

**参考答案:**

```
IP地址的作用：标识网络中唯一的一台设备

查看IP地址：ipconfig
- `Windows`: `ipconfig`
- `Linux`和`mac OS`: `ifconfig`
```

#### 2. 什么是端口？什么是端口号？知名端口号和动态端口号的范围是什么？

**参考答案:**

```
端口：标识一台设备上的一个网络应用程序
端口号：一台计算机一共有65536个端口，为了区分端口，每个端口都有编号：`0-65535`，编写网络程序时，可以设置网络程序使用的端口号。

知名端口：范围是0到1023，系统预留的一些端口号，不建议使用
动态端口：范围是从1024到65535，建议使用
```

#### 3. TCP 协议是什么？有什么特点？

**参考答案:**

```
概念：TCP(Transmission Control Protocol) 是一种网络传输控制协议，它是一种面向连接的、可靠的、基于字节流的传输层通信协议。

特点：
- 面向连接: 必须建立连接才能通信
- 可靠传输: 保证数据不丢包\不乱序
```

#### 4. 什么是socket？

**参考答案:**

```
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

# 创建客户端 socket 套接字对象
# socket.AF_INET：表示 IPV4
# socket.SOCK_STREAM：表示 TCP 传输协议
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 客户端请求和服务端程序建立连接
client.connect(('127.0.0.1', 8000))
print('客户端连接服务器成功！')

# 给服务端程序发送客户端的当前时间
from datetime import datetime
import time

while True:
    # 获取代码执行时间的当前时间
    now_time = datetime.now()
    # 将时间格式化成字符串
    time_str = now_time.strftime("%Y-%m-%d %H:%M:%S")
    # 给服务端发送客户端的时间
    client.send(time_str.encode())
    # 休眠1秒中
    time.sleep(1)


# 关闭客户端套接字
client.close()
```

2）服务端程序

```python
import socket

# ① 创建一个服务端负责监听的 socket，这个socket只负责接收客户端的连接请求，理解为：门迎、门童
# socket.AF_INET：表示使用 IPV4 的地址
# socket.SOCK_STREAM：表示使用 TCP 网络协议
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ② 服务端程序绑定IP地址和端口
server_socket.bind(('127.0.0.1', 8000))

# ③ 服务端程序设置监听
# 127：表示服务端程序最多同时支持 127 个客户端发起链接请求
server_socket.listen(127)

# ④ 设置完成之后，服务端等待客户端进行链接
print('等待接收来自于客户端连接请求...')
service_client, client_ip_port = server_socket.accept()
print(f'接收到来自于{client_ip_port}的连接')

# ⑤ 接收客户端发送的时间
# 1024：表示一次最多接收 1024 个字节的数据
# recv：接收客户端发送的消息，客户端没有发送消息的时候，recv会阻塞等待
while True:
    recv_msg = service_client.recv(1024) # bytes
    print('客户端时间为：', recv_msg.decode())

# ⑦ 关闭服务端的 socket
# 关闭和连接的客户端进行的通信的socket
service_client.close()
# 关闭接收客户端连接请求的socket
server_socket.close()
```

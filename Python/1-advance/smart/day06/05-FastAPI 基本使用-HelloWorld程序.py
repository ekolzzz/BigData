"""
FastAPI基本使用-HelloWorld程序
学习目标：能够使用 FastAPI 完成 HelloWorld 案例程序
"""
# 需求：使用 fastapi 编写一个 web 程序，当浏览器访问 /index 这个资源路径时，给浏览器返回 Hello World

# 导入 FastAPI 这个类
from fastapi import FastAPI
# 导入 uvicorn
import uvicorn

# 创建一个 FastAPI 这个类的实例对象
app = FastAPI()


# 定义资源路径以及对应的处理函数
# 注意：只要浏览器访问了这个服务器 /index 资源路径，index 处理函数就会被调用，函数的返回值就是响应体的内容
# 指定 /index 对应的处理函数是 index，get代表请求方式
@app.get('/index')
def aaa():
    # 函数的返回值就是响应体的内容
    return 'Hello World'


if __name__ == '__main__':
    # 启动 fastapi 这个程序
    # 注意：uvicorn其实就是 web 服务器
    uvicorn.run(app, host='127.0.0.1', port=8080)






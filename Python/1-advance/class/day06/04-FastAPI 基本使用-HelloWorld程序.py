"""
FastAPI基本使用-HelloWorld程序
学习目标：能够使用 FastAPI 完成 HelloWorld 案例程序
"""
# 导入 FastAPI 类
from fastapi import FastAPI
# 导入 uvicorn
import uvicorn

# 创建 FastAPI 对象
app = FastAPI()


# 定义业务处理函数并设置对应的 URL 地址
# get：表示请求方式
# /index：表示请求的 URL 地址
@app.get('/index')
def index():
    # 'Hello World'是响应体的内容
    return 'Hello World'


if __name__ == '__main__':
    # 启动 Web 服务器
    # host：指定 Web 服务器监听的IP
    # port：指定 Web 服务器监听的端口
    uvicorn.run(app, host='127.0.0.1', port= 8080)
# 导入FastAPI 这个类
from fastapi import FastAPI
# 导入 uvicorn
import uvicorn

# 创建一个FastAPI 这个类的实例对象
app = FastAPI()


# 定义资源路径以及对应的处理函数
# 注意：只要浏览器访问了这个服务器 /index 资源路径， index 处理函数就会被调用，函数的返回值就是响应体的内容
# 指定 /index 对应的处理函数是 index, get代表请求方式
@app.get('/index')
def index():
    # 函数的返回值就是响应体的内容
    return 'Hello World'

if __name__ == '__main__':
    # 启动的 fastapi 这个程序
    # 注意：uvicorn 其实就是 web 服务器
    uvicorn.run(app, host='127.0.0.1', port = 8080)
"""
FastAPI 基本使用-返回html内容
学习目标：能够使用 FastAPI 定义处理函数返回 html 内容
"""
# 导入 FastAPI 类
from fastapi import FastAPI
# 导入 Response 类
from fastapi import Response
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


# TODO：定义处理函数，访问 / 和 /gdp.html 地址时，返回 gdp.html 内容
@app.get('/')
@app.get('/gdp.html')
def gdp_html():
    # 读取 gdp.html 文件的内容
    with open('./sources/html/gdp.html', 'r', encoding='utf8') as f:
        content = f.read()

    # 返回一个响应 Response 对象
    return Response(content, media_type='text/html')


# TODO：定义处理函数，访问 /render.html 地址时，返回 render.html 内容
@app.get('/render.html')
def render_html():
    # 读取 render.html 文件的内容
    with open('./sources/html/render.html', 'r', encoding='utf8') as f:
        content = f.read()

    # 返回一个响应 Response 对象
    return Response(content, media_type='text/html')


if __name__ == '__main__':
    # 启动 Web 服务器
    # uvicorn.run(app, host='127.0.0.1', port=8080)
    # reload=True：当 uvicorn 检测到代码发生改变之后，会自动进行重启
    uvicorn.run('06-FastAPI 基本使用-返回html内容:app',
                host='127.0.0.1', port=8080, reload=True)

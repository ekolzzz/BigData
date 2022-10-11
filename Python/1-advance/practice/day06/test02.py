# 导入 FastAPI 类
from fastapi import FastAPI
# 导入 Response 类
from fastapi import Response
# 导入 uvicorn
import uvicorn

# 创建一个 FastAPI 这个类的实例对象
app = FastAPI()

# 1) HelloWorld程序
@app.get('/index')
def index():
    # 函数的返回值就是响应体的内容
    return 'Hello, World!'

@app.get('/')
@app.get('/gdp.html')
def gdp_html():
    with open('../sources/html/gdp.html', 'r', encoding = 'utf8') as f:
        content = f.read()

    # 返回一个响应 Response 对象
    return Response(content, media_type='text/html')\

@app.get('/render.html')
def gdp_html():
    with open('../sources/html/render.html', 'r', encoding = 'utf8') as f:
        content = f.read()

    # 返回一个响应 Response 对象
    return Response(content, media_type='text/html')\

@app.get('/index.html')
def gdp_html()
    with open('../sources/html/index.html', 'r', encoding = 'utf8') as f:
        content = f.read()

    # 返回一个响应 Response 对象
    return Response(content, media_type='text/html')

if __name__ == '__main__':
    # 启动 Web 服务
    # uvicorn.run(app, host='127.0.0.1', port=8080)
    # reload=True: 当 uvicorn 检测到代码发生改变之后，会自动进行重启
    uvicorn.run('test02:app',
                host='127.0.0.1', port = 8080, reload=True)
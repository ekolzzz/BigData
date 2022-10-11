"""
爬虫示例-爬虫单张图片数据
学习目标：能够使用 requests 爬取单张图片数据并保存
"""

# 需求：使用 requests 编写爬虫程序，爬取 http://127.0.0.1:8080/images/3.jpg 图片数据并保存。
import requests
# 准备请求的url地址
# url = 'http://127.0.0.1:8080/images/3.jpg'
url = 'https://img.photos18.com/images/image/2181/21814114.webp?1657884424'
# 使用 request 发送请求， 获取响应
response = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})

# 获取响应体的内容，并保存成一个图片文件
with open('./3.jpg','wb') as f:
    f.write(response.content)


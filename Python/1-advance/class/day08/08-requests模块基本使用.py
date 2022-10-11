"""
requests模块基本使用
学习目标：能够使用 requests 模块请求URL地址并获取响应内容
"""

# TODO：需求：使用 requests 请求百度，并获取响应内容
import requests

# 准备请求目标 url 目标
# url = 'https://www.baidu.com'
url = 'https://www.4399.com'

# 使用 requests 发送请求，获取响应
response = requests.get(url)

# 获取响应体的内容
# response.content: 响应体的原始内容，bytes 类型
print(response.content.decode(encoding='gbk'))


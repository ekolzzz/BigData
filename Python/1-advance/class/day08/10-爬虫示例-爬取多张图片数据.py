"""
爬虫示例-爬虫多张图片数据
学习目标：能够使用 requests 爬取多张图片数据并保存
"""

import requests
import re

# 需求：访问 http://127.0.0.1:8080/index.html 网址，获取页面上的所有图片保存到本地。

# 准备目标的 url 地址，使用 requests 发送请求，获得响应内容

url = 'http://127.0.0.1:8080/index.html'

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'})
html_str = response.content.decode()
print(html_str)

# 注意：findall 使用的正则如果没有分组，结果中的每个元素就是整个正则匹配的内容
# 如果 findall 使用的正则中分组的，结果中的每个元素就是正则中分组匹配到的内容

image_list = re.findall('<img src="(.*?)"', html_str) # list
print(image_list)

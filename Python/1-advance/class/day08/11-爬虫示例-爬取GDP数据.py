"""
爬虫示例-爬取GDP数据
学习目标：能够使用 requests 爬取GDP数据并保存
"""
import requests
import re

# 需求：访问 http://127.0.0.1:8080/gdp.html 网址，提取页面上的国家和GDP数据并保存到本地。

url = 'http://127.0.0.1:8080/gdp.html'

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'})
html_str = response.content.decode()
print(html_str)

gdp_list = re.findall('<a href=""><font>(.*?)</font></a>.*?<font>￥(.*?)亿元</font>', html_str, flags=re.S)
print(gdp_list)
with open('./sources/spider/gdp.txt', 'w', encoding='utf-8') as f:
    for items in gdp_list:
        f.write(str(items))
        f.write('\n')
    # content = str(gdp_list)
    # f.write(content)
    print('写入完成！')
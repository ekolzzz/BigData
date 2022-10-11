"""
re模块：正则匹配分组操作
学习目标：能够使用 re 模块进行正则匹配分组操作
"""
import re

"""
示例1：正则匹配分组操作
语法：(正则表达式)
"""

# import re
#
# my_str = '13155667788'
#
# # 需求：使用正则提取出手机号的前3位、中间4位以及后 4 位数据
# res = re.match(r'(\d{3})(\d{4})(\d{4})', my_str)
# print(res.group())
# print(res.group(1))
# print(res.group(2))
# print(res.group(3))
# print(res.group(1) + '*' * 4 + res.group(3))


"""
示例2：给正则分组起别名
语法：(?P<分组别名>正则表达式)
"""
my_str = '<div><a href="https://www.itcast.cn" target="_blank">传智播客</a><p>Python</p></div>'

# 需求：使用正则提取出 my_str 字符串中的 `传智播客` 文本
res = re.search(r'<a.*>(?P<text>.*)</a>', my_str)
print(res)
print(res.group())
print(res.group(1))
print(res.group('text'))


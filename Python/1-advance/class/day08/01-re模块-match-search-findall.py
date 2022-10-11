"""
re 正则模块：match、search、findall
学习目标：能够使用 re 模块中 match、search、findall 三个函数进行字符串的匹配
"""
# import re

"""
match函数：re.match(pattern, string, flags=0)
功能：尝试从字符串起始位置匹配一个正则表达式
        1）如果不能从起始位置匹配成功，则返回None；
        2）如果能从起始位置匹配成功，则返回一个匹配的对象
"""

# my_str = 'abc_123_DFG_456'
#
# # 匹配字符串bc(注：从头开始)
# res = re.match('bc', my_str)
# print(res)
#
# # 匹配字符串abc(注：从头开始)
# res = re.match('abc', my_str)
# print(res) # 匹配成功，返回一个 Match 对象
#
# # 获取匹配的内容：Match对象.group()
# print(res.group())

"""
search函数：re.search(pattern, string, flags=0)
功能：根据正则表达式扫描整个字符串，并返回第一个成功的匹配
        1）如果不能匹配成功，则返回None；
        2）如果能匹配成功，则返回一个匹配对象
"""

# my_str = 'abc_123_DFG_456'

# 匹配连续的3位数字
# 在 Python 的字符串中，反斜杠\具有特殊含义，可能会和正则中的\ 有冲突
# r: raw string ,原生字符串

# res = re.search(r'\d{3}', my_str)
# print(res) # 匹配成功，返回一个 Match 对象
# print(res.group())

"""
findall函数：re.findall(pattern, string, flags=0)
功能：根据正则表达式扫描整个字符串，并返回所有能成功匹配的子串
        1）如果不能匹配成功，则返回一个空列表；
        2）如果能匹配成功，则返回包含所有匹配子串的列表
"""

# my_str = 'abc_123_DFG_456'
#
# # 匹配字符串中的所有连续的3位数字
# res = re.findall(r'\d{3}', my_str)
# print(res) # list

import re

my_str = '13155667788'

# 需求：使用正则提取出手机号的前3位、中间4位以及后 4 位数据

# res = re.match(r'(\d{3})(\d{4})(\d{4})', my_str)
res = re.match(r'(\d{3})(\d{4})(\d{4})', my_str)
print(type(res), res)

# 获取整个正则表达式匹配的内容
print(res.group())

# 获取正则表达式指定分组匹配到的内容
# Match对象.group(组号)
print(res.group(1) + '*' * 4 + res.group(3)) # 7788
print(res.group(1) + '*' * 4 + res.group(3))
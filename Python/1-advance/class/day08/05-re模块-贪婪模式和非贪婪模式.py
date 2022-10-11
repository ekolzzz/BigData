"""
贪婪模式和非贪婪模式
学习目标：知道正则中贪婪模式和非贪婪模式的区别
"""

"""
贪婪模式：在整个表达式匹配成功的前提下，尽可能多的匹配
非贪婪模式：在整个表达式匹配成功的前提下，尽可能少的匹配
正则中的量词包括：{m,n}、?、*和+，这些量词默认都是贪婪模式的匹配，可以在这些量词后面加?将其变为非贪婪模式。
"""

import re

my_str = '<div>test1</div><div>test2</div>'

# 贪婪模式：在整个表达式匹配成功的前提下，尽可能多的匹配
re_obj = re.match('<div>.*</div>', my_str)
print(re_obj)
print(re_obj.group()) # 获取整个正则表达式匹配的内容

print('=' * 25 + '一条美丽的分割线' + '=' * 25)

# 非贪婪模式：在整个表达式匹配成功的前提下，尽可能少的匹配
re_obj = re.match('<div>.*?</div>', my_str)
print(re_obj)
print(re_obj.group())

print('=' * 25 + '一条美丽的分割线' + '=' * 25)

re_obj = re.match('<div>.{1,5}?</div>', my_str)
print(re_obj)
# print(re_obj.group())



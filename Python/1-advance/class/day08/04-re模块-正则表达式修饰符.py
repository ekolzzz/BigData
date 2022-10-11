"""
正则表达式修饰符
学习目标：知道re.I、re.M、re.S三个正则表示式修饰符的作用
"""

"""
re.I：匹配时不区分大小写
re.M：多行匹配，影响 ^ 和 $
re.S：影响 . 符号，设置之后，.符号就能匹配\n了
"""

import re

# 1) re.I：匹配时不区分大小写
my_str = 'aB'

res = re.match('ab', my_str, flags=re.I)
print(bool(res))
print(res.group())

print('=' * 25 + '一条美丽的分割线' + '=' * 25)

# 2) re.M：多行匹配，影响 ^ 和 $
my_str = 'aabb\nbbcc'

res = re.findall(r'^[a-z]{4}$', my_str, flags=re.M)
print(bool(res))
print(res)

print('=' * 25 + '一条美丽的分割线' + '=' * 25)

# 3) re.S：影响 . 符号，设置之后，.符号就能匹配\n了
my_str = '\nabc'

res = re.match(r'.', my_str, flags=re.S)
print(bool(res))
print(res.group())
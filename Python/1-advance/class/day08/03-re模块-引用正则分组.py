"""
re模块：引用正则分组
学习目标：能够在正则匹配时使用分组序号或分组名称引用分组内容
"""

"""
需求：写一个正则表达式，匹配字符串形如：'xxx xxx xxx'
注意：xxx可以是任意多位的数字，但是这三个xxx必须一致，比如：'123 123 123'
"""

"""
引用正则分组的方式：
1）\num：引用正则中第 num 个分组匹配到的字符串<br/>例如：`\1`表示第一个分组，`\2`表示第二个分组...
2）(?P=name)：引用正则中别名为 name 分组匹配到的字符串 # ?P<分组别名>正则表达式)
"""
import re

my_str = '123 123 123'
# 正则：'(/d+)/s/1/s/1'
res = re.match(r'(\d+)\s\1\s\1', my_str)
print(res)
print(-res.group())
print(res.groups())

res = re.match(r'(?P<num>\d+)\s(?P=num)\s(?P=num)', my_str) # (?P<分组别名>正则表达式)
print(res)
print(res.group())



"""
非0即为真：当if条件是一个数字时，非0就表示为真，0才表示假
非空字符串即为真：当if条件是一个字符串时，非空字符串就表示为真，空字符串('')才表示假
"""

num = 1

# 本质：python解释器自动将 num 转换为一个 bool 值，当变量是数字的时，非0就转换为True，0转换为False
# if bool(num):
if num:
    print('条件成立')
else:
    print('条件不成立')

print('==============================================')

# 注意：空字符串就是没有任何内容的字符串，两边只有引号
str1 = ''

# if bool(str1)
if str1:
    print('条件成立')
else:
    print('条件不成立')

print('==============================================')

str2 = 'False'

res1 = bool(str2)
# <class 'bool'> True
print(type(res1), res1)

# 注意：eval可以把字符串'False'转换为bool类型的False
res2 = eval(str2)
# <class 'bool'> False
print(type(res2), res2)












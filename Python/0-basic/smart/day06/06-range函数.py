"""
range函数：产生一段指定范围内的列表数字，一般配合for循环进行使用

使用：range(起始数字, 结束数字, 步长=1)

注意：产生的列表数据中，包含起始数字，不包含结束数字
"""
# 需求：生成一个列表：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = range(1, 11) # range是一个类型数据
print(res)
print(type(res), list(res))

# for 循环遍历产生的每个数字
for i in res:
    print(i)

print('=======================')

for i in range(1, 11):
    print(i)

print('=======================')

"""
示例：for循环计算1-100的数字和
"""
_sum = 0

for i in range(1, 101):
    _sum += i

print(_sum)
print('=======================')

"""
示例：for循环计算1-100的偶数和
"""
_sum = 0

for i in range(0, 101, 2):
    _sum += i

print(_sum)

print('=' * 20)

_sum = 0

for i in range(0, 101):
    if i % 2 == 0:
        _sum += i

print(_sum)

"""
列表推导式：快速生成列表元素的表达形式，通过for添加列表元素的简洁写法
推导式基本格式： [计算公式 for 循环 if 判断]
特点：
    1）每循环一次，将计算公式的结果添加到列表中
    2）计算公式可以使用遍历出的数据
    3）for 遍历出的数据 必须满足 if 判断 才会使用计算公式生成元素
"""

"""
需求：产生列表[0, 1, 2, 3, 4]
"""

my_list = []

for i in range(0, 5):
    my_list.append(i)

print(my_list)

# 形式1：[计算表达式 for 循环]
my_list = [i for i in range(0, 5)]
print(my_list)

"""
需求：产生列表[0, 2, 4, 6, 8, 10]
"""

my_list = [i for i in range(0, 11, 2)]
print(my_list)

my_list = [i * 2 for i in range(0, 6)]
print(my_list)

"""
需求：有一个字符串'hello'，生成['h', 'e', 'l', 'l', 'o']
"""

# print(list('hello'))
my_list = [c for c in 'hello']
print(my_list)

"""
需求：有一个列表[2, 1, 3, 4, 8, 9, 7]，需要将列表中的偶数筛选出来，存成一个新列表：[2, 4, 8]
"""
my_list = [2, 1, 3, 4, 8, 9, 7]

# 思路：遍历 my_list 中的每个数据，判断数据是否为偶数，如果是偶数，则添加到新列表中
ret = []
for i in my_list:
    if i % 2 == 0:
        ret.append(i)

print(ret)

# 形式2：[计算表达式 for 循环 if 条件]
ret = [i for i in my_list if i % 2 == 0]
print(ret)
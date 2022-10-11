"""
列表(list)：python中用来存储一组数据的类型，其中存储的每个数据称为'元素'
定义：列表变量名 = [数据1, 数据2, ...]
访问：列表变量名[位置标号]，列表中元素的位置编号从0开始，位置编号也被称为索引或下标
"""


# 定义一个列表数据：保存 'smart', 'yoyo', 'rock', 'lily' 四个数据

name_list = ['smart', 'yoyo', 'rock', 'lily']
print(type(name_list),'\n',name_list, end='\n')

print(name_list[1])
print(name_list[-3])

# IndexError: list index out of range
# 索引错误：列表的索引超出了范围，也叫索引越界错误
# 注意：根据下标（索引）从列表中获取数据时，下标（索引），不能超列表的范围，否则会出错
# print(name_list[/10]) # 获取列表中第十一位数据

name_list = ['smart', 'yoyo', 'rock', 'lily']
print(name_list, '\n', type(name_list))

import random

print(random.randint(1, 520))
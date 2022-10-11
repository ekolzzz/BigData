"""
集合：也可以用来存储一组数据，数据唯一，重复元素只保留一个，集合元素不能根据下标取值
定义：
    集合变量 = {数据1, 数据2, 数据3, ...}
"""


# 定义一个集合数据
my_set = {1, 2, 3, 2, 1, 3}
# <class 'set'>
print(type(my_set), my_set)

# 使用集合对列表数据进行去重
name_list = ['smart', 'rock', 'yoyo', 'smart']
name_set = set(name_list)
print(name_set)

# 如何定义一个空集合？
set1 = {} # 这是一个空字典
# <class 'dict'>
print(type(set1), set1)

set2 = set() # 这才是一个空集合
# <class 'set'>
print(type(set2), set2)

# 向集合中添加数据
set2.add(1)
set2.add(3)
set2.add(5)
set2.add(3)

print(type(set2), set2)

# 从集合中删除数据
set2.remove(3)
print(type(set2), set2)

set2.add('smart')
print(type(set2), set2)



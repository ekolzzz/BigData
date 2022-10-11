"""
元祖(tuple)：python中用来存储一组数据的类型，其中存储的每个数据称为'元素'
定义：元组变量名 = (数据1, 数据2, ...)
访问：元组变量名[位置标号]，列表中元素的位置编号从0开始，位置编号也被称为索引或下标

元组和列表的最主要区别：元组中的元素不可改变
"""

# 定义一个元组数据：存储 'smart', 'yoyo', 'rock', 'lily' 四个数据

tuple = ('smart', 'yoyo', 'rock', 'lily')
print(tuple)
print(type(tuple))


# 定义一个空元组
tuple_0 = ()
print(tuple_0)
print(type(tuple_0))

# 元组转列表
print(list(tuple))
print(type(list(tuple)))


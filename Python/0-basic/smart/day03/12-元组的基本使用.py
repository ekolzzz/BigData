"""
元祖(tuple)：python中用来存储一组数据的类型，其中存储的每个数据称为'元素'
定义：元组变量名 = (数据1, 数据2, ...)
访问：元组变量名[位置标号]，列表中元素的位置编号从0开始，位置编号也被称为索引或下标

元组和列表的最主要区别：元组中的元素不可改变
"""

# 定义一个元组数据：存储 'smart', 'yoyo', 'rock', 'lily' 四个数据
# 从左到右        0        1       2       3
# 从右到左       -4       -3      -2       -1
name_tuple = ('smart', 'yoyo', 'rock', 'lily')
# <class 'tuple'>
print(type(name_tuple), name_tuple)

# 获取元祖中的 'lily' 数据
print(name_tuple[3])
print(name_tuple[-1])

# IndexError: tuple index out of range
# 索引越界错误
# print(name_tuple[10])

# 尝试把元祖中的 'rock' 改成 'rose'
# TypeError: 'tuple' object does not support item assignment
# 原因：元祖中的数据只能读，不能增、删、改
# name_tuple[2] = 'rose'

# 注意：我们定义一个元祖时，如果元祖中只有一个元素，元素的后面一定要添加一个逗号
my_tuple1 = (10)
# <class 'int'>
print(type(my_tuple1), my_tuple1)

my_tuple2 = (10,)
# <class 'tuple'>
print(type(my_tuple2), my_tuple2)


# 定义一个空元祖
# my_tuple3 = ()
my_tuple3 = tuple()
print(type(my_tuple3), my_tuple3)










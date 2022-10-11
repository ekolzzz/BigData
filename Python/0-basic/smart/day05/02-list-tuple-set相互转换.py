"""
list(x)	将 x 转换为列表类型
tuple(x)	将 x 转换为元组类型
set(x)	将 x 转换为集合类型
"""

# 列表转元组、集合 类型
my_list = [1, 2, 3, 5, 3, 5]
print(type(my_list), my_list)

# 列表转换为元组类型
my_tuple = tuple(my_list)
print(type(my_tuple), my_tuple)

# 列表转换为集合类型
my_set = set(my_list)
print(type(my_set), my_set)

print('============华丽分割线============')

# 元组转列表、集合 类型
my_tuple = (1, 2, 3, 5, 3, 5)
print(type(my_tuple), my_tuple)

# 元组转换为列表 类型
my_list = list(my_tuple)
print(type(my_list), my_list)

# 元组转换为集合 类型
my_set = set(my_tuple)
print(type(my_set), my_set)


print('============华丽分割线============')

# 集合转元组、列表 类型
my_set = {1, 2, 3}
print(type(my_set), my_set)

# 集合转换为列表 类型
my_list = list(my_set)
print(type(my_list), my_list)

# 集合转换为元组 类型
my_tuple = tuple(my_set)
print(type(my_tuple), my_tuple)


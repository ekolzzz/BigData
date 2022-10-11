"""
len(item)	计算容器中元素个数
max(item)	返回容器中元素最大值	如果是字典，只针对 key 比较
min(item)	返回容器中元素最小值	如果是字典，只针对 key 比较
"""

my_list = [1, 3, 2, 5, 8, 7]

print(len(my_list))
print(max(my_list))
print(min(my_list))

"""
切片：适合于字符串、列表、元组
    数据[起始索引:结束索引:步长]
"""

# 示例：从 my_list 中截取 [3, 2, 5, 8]
#          0  1  2  3  4  5
my_list = [1, 3, 2, 5, 8, 7]

result = my_list[1:5]
print(type(result), result)

# 示例：从 my_tuple 中截取 (2, 1, 3)
#           0  1  2  3  4  5
my_tuple = (2, 8, 1, 9, 3, 4)

result = my_tuple[:5:2]
print(type(result), result)
print('============华丽分割线============')

"""
+	[1, 2] + [3, 4]	[1, 2, 3, 4]	合并	字符串、列表、元组
*	[1, 2] * 2	[1, 2, 1, 2]	重复	字符串、列表、元组
in	3 in (1, 2, 3)	True	元素是否存在	字符串、列表、元组、字典
not in	4 not in (1, 2, 3)	True	元素是否不存在	字符串、列表、元组、字典
> >= == != < <=	(1, 2, 6) < (1, 3, 4)	True	元素比较	字符串、列表、元组
"""

new_list = [1, 2] + [3, 4]
print(type(new_list), new_list)

new_tuple = (1, 2) + (3, 4)
print(type(new_tuple), new_tuple)
print('============华丽分割线============')

new_list = [1, 2] * 2
print(type(new_list), new_list)

new_tuple = (1, 2) * 3
print(type(new_tuple), new_tuple)

new_str = 'hello' * 2
print(type(new_str), new_str)

print('============华丽分割线============')

# 判断一个数据是否在元组中存在
print(3 in (1, 2, 3))

my_str = 'hello'
# 判断一个字符是否在字符串中存在
print('a' in my_str)

# 判断字典中是否包含某个key
user_dict = {'name': 'smart', 'age': 18, 'city': '上海'}
print('name' in user_dict)
print('============华丽分割线============')

print((1, 2, 6) < (1, 3, 4))

# 字符串的比较
# ascii码
print('hello' < 'hallo')
print('A' < 'a')
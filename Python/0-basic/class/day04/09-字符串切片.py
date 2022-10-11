"""
切片：slice，截取一部分
切片 使用 索引值 来限定范围，根据 步长 从原序列中 取出一部分 元素组成新序列
切片 方法适用于 字符串、列表、元组
字符串[开始索引:结束索引:步长]
"""
"""
截取从 b ~ e 位置 的字符串
截取从 b ~ 末尾 的字符串
截取从 开始 ~ e 位置 的字符串
从开始位置，每隔一个字符截取字符串
截取字符串末尾两个字符
字符串的逆序（面试题）
"""

#         01234567
# my_str = 'abcdefgh'
#
# # 1）截取从 b ~ e 位置 的字符串
# # 注意：截取字符串，包含开始索引，不包含结束索引
# print(my_str[1:5:1]) # 步长不写默认是1
# print(my_str[0:7:2])
#
# # 截取的思路
#
# # 2）截取从 b ~ 末尾 的字符串
# print(my_str[1:8])
#
# print(my_str[1:])
#
# # 3）截取从 开始 ~ e 位置 的字符串
# print(my_str[0:5])
#
# # 4）从开始位置，每隔一个字符截取字符串
# print(my_str[::2])

# 5）截取字符串末尾两个字符
my_str = 'abcdefgh'
print(my_str[6:8:1])
print(my_str[1])

# 6）字符串的逆序（面试题）
# abcdefgh
# hgfedcba

#         01234567
# my_str = 'abcdefgh'
# print(len(my_str))
# print(my_str[-1::-1])

my_str = input('请输入一个字符串：')
print(my_str)

print(my_str[-1:-(len(my_str)+1):-1]) # 步长为-1时，起始索引默认为-1，结束索引默认为-(len(my_str)+1)
print(my_str[::-1])


# 先确定步长
print(my_str[1:-2:1])

print(my_str[-6:6:-1])
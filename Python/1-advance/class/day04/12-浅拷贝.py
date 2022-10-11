# 浅拷贝：
# 可变容器类型，进行浅拷贝时，只会对第一层数据重新开辟内存，进行拷贝。
# 不可变容器类型，进行浅拷贝时，不会重新开辟内存，等同于=号赋值。
import copy

# 简单列表
my_li1 = [3, 5, 1]

# 浅拷贝
my_li2 = my_li1
my_li3 = copy.copy(my_li1)

print('id(my_li1)：', id(my_li1))
print('id(my_li2)：', id(my_li2))
print(my_li1)

print(my_li1)
my_li1[0] = 1
print(my_li1)
print(my_li3)
print('id(my_li1)：', id(my_li1))
print('id(my_li3)：', id(my_li3))

print('id(my_li1[0])：', id(my_li1[0]))
print('id(my_li3[0])：', id(my_li3[0]))

print('=' * 20)

# 嵌套列表
my_li2 = [[2, 4], 6, 7]

# 浅拷贝
my_li4 = copy.copy(my_li2)

print('id(my_li2)：', id(my_li2))
print('id(my_li4)：', id(my_li4))

print('id(my_li2[0])：', id(my_li2[0]))
print('id(my_li4[0])：', id(my_li4[0]))

print('=' * 20)

# 简单元祖
my_tuple1 = (2, 3, 5)

# 浅拷贝
my_tuple3 = copy.copy(my_tuple1) # -> my_tuple3 = my_tuple1

print('id(my_tuple1)：', id(my_tuple1))
print('id(my_tuple3)：', id(my_tuple3))

print('=' * 20)

# 嵌套元祖
my_tuple2 = ([3, 5], 2, 1)

# 浅拷贝
my_tuple4 = copy.copy(my_tuple2)

print('id(my_tuple2)：', id(my_tuple2))
print('id(my_tuple4)：', id(my_tuple4))

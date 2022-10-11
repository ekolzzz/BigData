"""
组包：= 右边有多个数据时，会自动包装为元组赋值给 = 左边的变量
"""
my_test = 'a', 'b', 'c'
print(type(my_test), my_test)



"""
拆包：多个变量 = 容器数据，当变量数量等于容器长度时，容器中的每个元素会按照次序一一赋值给 = 号左边的变量

注意：= 号左边变量的数量必须和 = 号右边容器的长度相等
"""


a, b, c = (1, 2, 3)
print(type(a), a, type(b), b, type(c), c)
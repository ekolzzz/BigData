"""
应用1：交换 a，b 两个变量的值
"""

a = 10
b = 20

print(f'交换之前：a={a}, b={b}')
# 先将 = 号右边 b 和 a 的值组装成了一个元祖 (20, 10)
# 然后再将元祖 (20, 10) 数字拆解出来，分别赋值给 = 号左边的 a 和 b
a, b = b, a
print(f'交换之后：a={a}, b={b}')


"""
应用2：函数同时返回多个结果
"""


def func():
    # 这里其实会把1,2,3先组装成一个元祖(1,2,3)，然后把元祖(1,2,3)作为函数的返回值返回
    return 1, 2, 3


result = func()
# <class 'tuple'> (1, 2, 3)
print(type(result), result)

# 将 func 函数返回的 (1, 2, 3)，拆解出来分别赋值给 = 号左边的变量 a, b, c
a, b, c = func() # a, b, c = (1, 2, 3)
print(a)
print(b)
print(c)


"""
应用3：字典元素拆包
"""

user_dict = {'name': 'smart', 'age': 18}

# 同时遍历字典的 key 和 value
for key, value in user_dict.items():
    print(key, value)

for item in user_dict.items():
    print(type(item), item)
"""
在 python 中，等号赋值的本质是引用（也可以理解为是一种指向）。
"""

a = 10
b = a
a = 20

# 假设有两个人：老张和老王，这两个人两个月的工资都是：3000,5000
# 假设老王第二个的工资给老婆买了一个礼物，花了1000，还剩4000

lao_zhang = [3000, 5000]
lao_wang = lao_zhang
lao_wang[1] = 4000

print(lao_zhang, lao_wang)
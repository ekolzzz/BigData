# 需求：产生1-10之间的一个随机的整数
# 注意：这里导入的其实是当前目录下的 random 模块，不是 python 解释器内置的
import random

# 报错：自己的 random 模块里面根本就没有 randint 函数
# module 'random' has no attribute 'randint'
res = random.randint(1, 10)
print(res)
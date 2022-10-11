"""
使用模块时起别名
学习目标：能够在使用模块时通过as关键字起别名，解决名称冲突的问题
"""

"""
情况1：给模块起别名
    import 模块名 as 别名
    
情况2：给模块中导入的内容起别名
    from 模块名 import 内容 as 别名

注意：一旦起了别名之后，那么只能通过别名使用相应的内容
"""

# 情况1：给模块起别名
#     import 模块名 as 别名
import smart as sm

print(sm.num)

res = sm.my_sum(1, 2)
print(res)

# 情况2：给模块中导入的内容起别名
#     from 模块名 import 内容 as 别名
from smart import my_sum as sm_sum


def my_sum(*args):
    """计算任意多个数字的和"""
    res = 0

    for i in args:
        res += i

    return res


result = my_sum(1, 2)
print(result)


result = sm_sum(3, 1)
print(result)




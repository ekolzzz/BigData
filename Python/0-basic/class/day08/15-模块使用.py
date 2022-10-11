"""
模块的使用
学习目标：知道如何使用模块中的变量、函数、类等
"""

"""
方式1：导入整个模块，然后通过`模块名.要使用的内容`进行使用
    import 模块名

方式2【推荐】：从模块中导入指定要使用的内容，然后进行使用【推荐】
    from 模块名 import 要使用的内容

方式3【不推荐】：导入模块中的所有内容，然后进行使用
    from 模块名 import *
"""
import ekol

print(ekol.num)

print(ekol.my_sum(1, 2))

print(ekol.my_sub(4, 1))
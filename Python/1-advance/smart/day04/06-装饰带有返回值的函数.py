"""
装饰带有返回值的函数
学习目标：能够编写装饰器装饰带有返回值的函数
"""

"""
需求：编写一个装饰器，装饰 my_sum 函数，计算 my_sum 的执行时间
"""


def my_sum(n):
    """计算1-n之间的数字和并返回"""
    result = 0

    # 遍历计算 1-n 之间的数字和
    for i in range(1, n + 1):
        result += i

    # 返回计算的结果
    return result




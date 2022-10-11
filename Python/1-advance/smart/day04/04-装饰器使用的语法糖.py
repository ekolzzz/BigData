"""
装饰器使用的语法糖
学习目标：能够通过语法糖的形式使用装饰器
"""

import time


# 装饰器函数
def get_time(func):
    def wrapper():
        s1 = time.time()
        func()
        s2 = time.time()
        print('执行时间：', s2 - s1)

    return wrapper


def func1():
    _sum = 0
    for i in range(1000000):
        _sum += i
    return _sum


def func2():
    _res = 1
    for i in range(1000000):
        _res *= i
    return _res



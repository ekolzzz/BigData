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

# 本质： func1 = get_time(func1)
@get_time
def func1():
    _sum = 0
    for i in range(1000000):
        _sum += i
    return _sum

# 本质： func2 = get_time(func2)
@get_time
def func2():
    _res = 0
    for i in range(1000000):
        _res *= i
    return _res

func1()
func2()

"""
装饰器的基本使用
学习目标：能够使用装饰器统计函数的执行时间
"""

"""
需求：统计 func1 和 func2 函数调用时的执行时间
"""
import time

# time.time()：获取代码执行时的时间戳：秒


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



"""
装饰器统计函数调用的执行时间：
    装饰器的本质是闭包函数，可以在不改变原始函数(被装饰函数)代码和调用的情况下，对原始函数进行功能的扩展
    
装饰器定义的基本形式：
    # 注意：装饰器的外部函数必须有一个形参(有且只有一个)，这个形参将来传入的实参就是要扩展功能的函数名(原始函数，也叫被装饰函数)
    def decorator(fn):
        def inner():
            # TODO：执行函数之前
            fn() # 调用被装饰的函数
            # TODO：执行函数之后
        return inner
"""




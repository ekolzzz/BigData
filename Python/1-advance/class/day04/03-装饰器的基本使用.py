"""
装饰器的基本使用
学习目标：能够使用装饰器统计函数的执行时间
"""

"""
需求：统计 func1 和 func2 函数调用时的执行时间
"""
import time

# time.time()：获取代码执行时的时间戳：秒

# def func1():
#     _sum = 0
#     for i in range(1000000):
#         _sum += i
#     return _sum
#
#
# def func2():
#     _res = 0
#     for i in range(1000000):
#         _res *= i
#     return _res

# t1 = time.time()
# func2()
# t2 = time.time()
# print(t2 - t1)

"""
装饰器统计函数调用的执行时间：
    装饰器的本质是闭包函数，可以在不改变原始函数(被装饰函数)代码和调用的情况下，对原始函数进行功能的扩展

1) 注意：闭包的三个条件也需要满足：函数嵌套，外部函数返回内部函数，内部函数调用外部函数变量（包括外部函数的参数）
2) 外部函数必须有且只有一个形参，而且这个形参将来传递的实参，必须是一个函数名（这个函数名就是要扩展功能的那个函数名字）

装饰器定义的基本形式：
    def decorator(fn):
        # 注意：调用外层函数时，传入的fn必须是一个函数，此函数即为要扩展功能的函数，也叫被装饰函数
        def inner():
            # TODO：执行函数之前
            fn() # 执行被装饰的函数
            # TODO：执行函数之后
        return inner
"""
def get_time(func):
    #
    def inner():
        t1 = time.time()
        func() # func() -> fun1()
        t2 = time.time()
        print(f'函数执行了{t2 - t1}秒')

    return inner # get_time函数返回inner函数

# @get_time
def func1():
    _sum = 0
    for i in range(1000000):
        _sum += i
    return _sum

# @get_time
def func2():
    _res = 0
    for i in range(1000000):
        _res *= i
    return _res

# get_time(func1)()
func1 = get_time(func1) # func1 -> inner
func1() # func1() -> inner()
#
func2 = get_time(func2)
func2()

# 总结：如果被装饰的函数带有参数，则装饰器的内部函数需要设置对应的参数
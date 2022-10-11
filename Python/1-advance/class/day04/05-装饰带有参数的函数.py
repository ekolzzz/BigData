"""
装饰带有参数的函数
学习目标：能够编写装饰器装饰带有参数的函数
"""

"""
需求：编写一个装饰器，装饰 my_sum 函数，计算 my_sum 的执行时间
"""
import time

# 装饰器函数
def get_time(func):
    def wrapper(num): # 如果wrapper()内没有形参会报错 -> TypeError: wrapper() takes 0 positional arguments but 1 was given
        s1 = time.time()
        func(num) # 如果func()内没有形参会报错 -> TypeError: my_sum() missing 1 required positional argument: 'n'
        s2 = time.time()
        print('执行时间：', s2 - s1)

    return wrapper

@get_time # 装饰器的语法糖
def my_sum(n):
    """计算1-n之间的数字和"""
    result = 0

    # 遍历计算 1-n 之间的数字和
    for i in range(1, n + 1):
        result += i

    # 打印计算的结果
    print('结果为：', result)

# print(my_sum)
my_sum(10000000)

# 结论：如果被装饰的函数带有参数，则装饰器的内部函数需要设置对应数量的参数
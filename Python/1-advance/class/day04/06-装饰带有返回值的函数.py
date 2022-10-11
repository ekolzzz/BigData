"""
装饰带有返回值的函数
学习目标：能够编写装饰器装饰带有返回值的函数
"""

"""
需求：编写一个装饰器，装饰 my_sum 函数，计算 my_sum 的执行时间
"""
import time

# 装饰器函数
def get_time(func):
    def wrapper(num):
        s1 = time.time()
        # 调用被装饰的原始函数时，需要将内部函数接收到的参数再返回
        result = func(num) # 接收被装饰的原始函数的返回值
        s2 = time.time()
        print('执行时间：', s2 - s1)
        return result  # 将被装饰的原始函数的返回值作为自己的返回值返回

    return wrapper

# @get_time # 装饰器的语法糖
def my_sum(n):
    """计算1-n之间的数字和并返回"""
    result = 0

    # 遍历计算 1-n 之间的数字和
    for i in range(1, n + 1):
        result += i

    # 返回计算的结果
    return result

res = my_sum(1000000)
print(res)

# 如果被装饰的函数带有返回值，则装饰器的内部函数需要将被装饰函数的返回值作为自己的返回值再返回。
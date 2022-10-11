"""
思考：如何编写一个通用的装饰器，计算函数的执行时间，要求可以装饰任意函数（带任何参数或返回值）
"""


def func1():
    """func1函数无参数，也无返回值"""
    _sum = 0
    for i in range(1000000):
        _sum += i
    return _sum


def func2(m, n):
    """计算m-n之间的数字和，func2函数有两个参数，也有返回值"""
    result = 0

    # 遍历计算 m-n 之间的数字和
    for i in range(m, n + 1):
        result += i

    # 返回计算的结果
    return result





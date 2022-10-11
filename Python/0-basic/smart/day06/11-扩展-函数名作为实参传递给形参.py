"""
函数名其实也是一个变量，它可以作为实参传递给形参
"""


def my_add(a, b):
    """计算两个数的和"""
    return a + b


def my_sub(a, b):
    """计算两个数的差"""
    return a - b


def my_calc(func, num1, num2):
    """
    func：这个形参接收的是一个函数名
    num1：接收一个数字
    num2：接收另一个数字
    """
    # 调用 func
    res = func(num1, num2)
    print('结果为：', res)


# 调用 my_calc 函数
my_calc(my_add, 2, 3)
my_calc(my_sub, 3, 1)

# 定义一个匿名函数
# func1 = lambda a, b: a * b

# res = func1(2, 3)
# print(res)

# 调用 my_calc 函数
# my_calc(func1, 1, 3)

# 把 lambda a, b: a * b 传递给形参 func
my_calc(lambda a, b: a * b, 2, 3)
# 把 lambda a, b: a / b 传递给形参 func
my_calc(lambda a, b: a / b, 4, 2)


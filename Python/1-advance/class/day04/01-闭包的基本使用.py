"""
闭包的基本使用
学习目标：能够使用闭包统计函数的调用次数
"""

"""
需求：如何统计 sub 函数的调用次数？？？
- 要求在每次调用 sub 函数时，打印出第几次调用该函数
"""
# 定义一个全局变量,来统计sub函数的调用次数
count = 0

def sub(a, b):
    """计算两个数之差"""
    global count
    count += 1
    return a - b


# 测试进行函数调用
sub(2, 1)
sub(3, 2)
sub(5, 3)


"""
利用闭包统计函数的调用次数

闭包的构成条件：
    1. 函数嵌套(外部函数中定义了一个内部函数)
    2. 外部函数返回了内部函数
    3. 内部函数使用了外部函数的变量(还包括外部函数的参数)
"""





# 1. 函数嵌套(外部函数中定义了一个内部函数)
def func_outer():

    count = 0

    def sub(a, b):
        # 3. 内部函数使用了外部函数的变量(还包括外部函数的参数)
        # 如果内部函数要对外部函数的变量进行重新赋值，需要进行nonlocal 声明
        nonlocal count
        count += 1
        print(f'第{count}次调用sub函数:\n{a}-{b} = {a - b}')
        return a - b
# 2. 外部函数返回了内部函数
    return sub

# 调用外部函数，创建一个闭包
func = func_outer() # func = sub

func(2, 1)
func(4, 2)
func(7, 3)
func(9, 4)












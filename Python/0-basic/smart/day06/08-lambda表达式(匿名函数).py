"""
lambda表达式：简单函数的简洁写法

lambda 形参1, 形参2, ... : 一行代码

注意：
1）匿名函数中不能使用 while 循环、for 循环，只能编写单行的表达式，或函数调用
2）匿名函数中返回结果不需要使用 return，表达式的运行结果就是返回结果
3）匿名函数中也可以不返回结果。例如： lambda : print('hello world')
"""


def func_sum(a, b):
    """
    计算a，b的和，返回结果
    """
    return a + b


# 使用 lambda 定义上面的函数
# 注意：如果单看 lambda a, b: a + b 表达式，它其实就是一个函数，但是没有名称，所以叫匿名函数
# 但是我们可以把 lambda 表达式赋值给一个变量，这个变量名就相当于函数名
func = lambda a, b: a + b


# res = func_sum(1, 3)
# print(res)

# 注意：函数名其实也是一个变量，也有数据类型
# <class 'function'>
print(type(func_sum))
# <class 'function'>
print(type(func))

res = func(2, 4)
print(res)

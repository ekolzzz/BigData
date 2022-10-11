"""
lambda表达式：简单函数的简洁写法

lambda 形参1, 形参2, ... : 单行表达式 或 函数调用

注意：
1）匿名函数中不能使用 while 循环、for 循环，只能编写单行的表达式，或函数调用
2）匿名函数中返回结果不需要使用 return，表达式的运行结果就是返回结果
3）匿名函数中也可以不返回结果。例如： lambda : print('hello world')
"""

# 无参有返回值匿名函数
# a) 匿名函数整体就是函数名字， 函数名字()就是函数调用

ret = (lambda: 1 + 1)()

print(ret)

# b) 给匿名函数起一个函数名字，函数名字()就是调用函数
func = lambda: 1 + 1  # 给匿名函数起一个函数名字叫func
ret = func()  # 返回值变量 = 函数名()
print(ret)

print('=' * 30)

# 有参有返回值匿名函数
# a. 直接调用匿名函数
ret = (lambda a, b: a - b)(30, 10)
print(ret)

# b. 先给匿名函数起名，再调用
func = lambda a, b: a - b
ret = func(30, 10)
print(ret)


# def func_sum(a, b):
#     """
#     计算a，b的和，返回结果
#     """
#     return a + b
#
# res = func_sum(1, 3)
# print(res)

def func_sum(a, b):
    return a+b

def func_sub(a, b):
    return a-b

my_func = (lambda a , b : func_sum(a, b))(1, 2)
print(my_func)


#
(lambda : print('hello world'))()

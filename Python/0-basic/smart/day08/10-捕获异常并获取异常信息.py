"""
程序异常处理
学习目标：能够捕获异常并获取异常信息
"""

"""
获取异常的信息描述
try:
    可能发生异常的代码
except 异常类型1 as 变量(异常对象):
    处理异常的代码

注：as后面的变量会自动和相应类型的异常实例对象进行绑定，
通过打印该异常对象可以获取系统提示的相应的错误信息
"""

# try:
#     print('================')
#     # FileNotFoundError
#     f = open('xxx.txt', 'r')
#     print('================')
# except FileNotFoundError as e:
#     print('发生了异常：', e)
#
# try:
#     print('================')
#     # ZeroDivisionError
#     num = 10 / 0
#     print('================')
# except ZeroDivisionError as e:
#     print('发生了异常：', e)

"""
捕获任意类型的异常同时获取信息描述
try:
    可能发生异常的代码
except Exception as 变量(异常对象):
    处理异常的代码

注意：
1）Exception 是 python 中所有内置异常的父类，
2）所有子类的异常都可以通过 try ... except 父类 进行捕获
"""

try:
    print('================')
    # FileNotFoundError
    # f = open('xxx.txt', 'r')
    # ZeroDivisionError
    num = 10 / 0
    print('================')
except Exception as e:
    print('发生了异常：', e)



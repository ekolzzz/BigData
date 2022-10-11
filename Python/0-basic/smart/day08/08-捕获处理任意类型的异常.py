"""
程序异常处理
学习目标：能够捕获任意类型的异常，防止程序异常导致意外终止
"""

"""
为什么要进行异常处理？防止程序退出，保证程序正常执行
"""

"""
捕获任意类型的异常

try:
    可能发生异常的代码
    ...
except:
    处理异常的代码

注意：如果try里面某句代码出现了异常，会自动跳转执行except里的代码
"""
# try:
#     print('===============')
#     # FileNotFoundError
#     f = open('xxx.txt', 'r')
#     print('===============')
# except:
#     print('try里发生了异常')

try:
    print('===============')
    # ZeroDivisionError
    num = 10 / 0
    print('===============')
except:
    print('try里面发生了异常')


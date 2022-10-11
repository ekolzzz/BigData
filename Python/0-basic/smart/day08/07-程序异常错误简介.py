"""
程序异常错误：
学习目标：知道异常是指程序运行过程中出现的错误
"""

"""
程序中的错误：
1）语法错误：在程序还未运行时，解释器就能检测出来的错误
2）异常错误：在语法正确的情况下，程序在执行过程中出现的错误

错误信息的最后一行告诉我们程序遇到了什么类型的错误。异常有不同的类型，
而其类型名称将会作为错误信息的一部分中打印出来。
"""

# 语法错误：SyntaxError: invalid syntax
# if True
#     print('hello world')

# 常见异常错误演示

# FileNotFoundError: [Errno 2] No such file or directory: 'xxx.txt'
# f = open('xxx.txt', 'r')

# io.UnsupportedOperation: not readable
# with open('aaa.txt', 'w') as f:
#     f.read()


# TypeError: '>=' not supported between instances of 'str' and 'int'
# age = input('请输入年龄：') # str
#
# if age >= 18:
#     print('成年了！')

# ZeroDivisionError: division by zero
# num = 10 / 0


# 语法错误：不应出现！！！
# 异常错误：很难避免！！！
# 不要过度依赖异常处理，因为有些异常错误通过对代码逻辑的完善是可以避免！！！


try:
    age = int(input('请输入年龄：')) # str
except Exception as e:
    print('发了异常，必须输入整型数字')
    # 退出程序
    exit(0)

if age >= 18:
    print('成年了！')
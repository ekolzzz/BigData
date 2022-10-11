 """
函数分为：无参函数和有参函数
1）无参函数：调用时不需要给函数传递参数
    def 函数名():
        # 函数中的代码

    调用：函数名()
2）有参函数：调用时需要给函数传递一下必要的参数
    def 函数名(参数1, 参数2, ...):
        # 函数中的代码

    调用：函数名(传递参数1，传递参数2)
"""

"""
需求：定义一个函数，能够计算并打印出两个数字之和
"""
# def my_sum(num1, num2):
#     """计算两数之和"""
#     result = num1 +num2
#     print('%d+%d=%d' % (num1, num2, result))


# num1 = int(input('请输入一个数：'))
# num2 = int(input('请输入另一个数：'))
# my_sum(num1,num2)

"""
需求：定义一个函数，能够计算并打印出两个数字之差
"""

def calc(num1, num2, task):
    #加法
    if task == '+' :
        result = num1 + num2
        print('%d+%d=%d' % (num1, num2 ,result))

    # 减法
    elif task == "-" :
        result = num1 - num2
        print('%d-%d=%d' % (num1, num2 ,result))

    # 乘法
    elif task == "*" :
        result = num1 * num2
        print('%d*%d=%d' % (num1, num2 ,result))

    # 除法
    elif task == "/" :
        result = num1 / num2
        print('%d/%d=%d' % (num1, num2 ,result))

    else:
        print('输入错误')

# num1 = int(input('请输入一个数：'))
# task = input('请输入运算符：')
# num2 = int(input('请输入另一个数：'))
#
# calc(num1, num2, task)

# python中内置函数：不需要咱们定义，python已经定义好了，我们可以直接调用

task = input('请输入要计算的公式：') # 字符串

num1 = int(task[0])
num2 = int(task[2])
task = task[1]
# print(task)
# print(type(num1), num1)
# print(type(num2), num2)

calc(num1, num2, task)
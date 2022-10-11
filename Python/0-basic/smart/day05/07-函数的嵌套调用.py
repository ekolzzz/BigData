"""
函数的嵌套调用：在一个函数的代码中调用了另外一函数
"""


def func01():
    print('开始调用func01')
    print('结束调用func01')


def func02():
    print('开始调用func02')
    # 调用func01
    func01()
    print('结束调用func02')


func02()

"""
需求：
1）设计一个函数，打印一行分隔线：可指定数量，可指定分隔线字符的样式 
    如： 一行分隔线字符的数量为5，字符样式为'$ '
    $ $ $ $ $

2）设计一个函数，打印n行分隔线，可指定一行分隔线字符的数量，可指定分隔线字符的样式 
    如：3行分隔线，一行分隔线字符的数量为5，字符样式为'$ '
    $ $ $ $ $
    $ $ $ $ $
    $ $ $ $ $
"""


# 定义函数
def print_line(num, char):
    """
    打印一行分割线
    参数：
    * num：接收一个数字，表示一行分割线打印字符的数量
    * char：接收一个字符串，表示表示一行分割线打印字符的样子
    """
    # 空语句，表示函数中什么代码都没有
    print(num * char)


# 调用函数
# print_line(6, '# ')

# 定义函数
def print_lines(line, a, b):
    """
    打印 n 行分割线
    参数：
    * line：接收一个数字，表示打印几行分割线
    * a：接收一个数字，表示每行打印的字符的数量
    * b：接收一个字符串，表示每行打印的字符的样式
    """
    i = 0

    while i < line:
        # print(a * b)
        # 调用 print_line 打印一行分割线
        print_line(a, b)
        i += 1


# 调用函数
# print_lines(3, 5, '$ ')



"""
需求：
1）设计一个函数求三个数的和
2）设计一个函数求三个数的平均值
"""


# 函数定义
def sum_3_number(num1, num2, num3):
    """计算三个数字的和"""
    # result = num1 + num2 + num3
    # return result
    return num1 + num2 + num3


# 函数定义
def avg_3_number(a, b, c):
    """计算三个数字的平均值"""
    # result = a + b + c
    # result = sum_3_number(a, b, c)
    # avg_result = result / 3
    # return avg_result

    # ① 首先调用 sum_3_number 这个函数计算 a、b、c 三个数字的和
    # ② 然后拿计算的结果除以3，求三个数的平均值
    # ③ 把计算的三个数的平均值返回
    return sum_3_number(a, b, c) / 3


# 调用函数
# res = sum_3_number(1, 2, 3)
# print(res)

res = avg_3_number(1, 2, 3)
print(res)







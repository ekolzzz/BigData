"""
局部变量：
1）函数的形参以及函数内部定义的变量，作用域只在函数内部(只在函数内部有效)
2）不同函数的局部变量可以同名，互不影响
3）局部变量的作用是存储需要临时存储的数据
"""


def func1(num):
    my_str = 'hello'
    print(num)
    print(my_str)


def func2(num):
    print(num)


func1(10)
func2(20)

# NameError: name 'num' is not defined
# print(num)

# NameError: name 'my_str' is not defined
# print(my_str)


"""
全局变量：
1）在函数外部定义的变量
2）全局变量能够在所有的函数中进行访问(不修改)
"""
# 这就是一个全局变量
num = 10


def func1():
    # 需求：假设要在func1函数中将全局变量num的值修改为：30
    # 注意：下面这句代码相当于在 func1 函数内部定义了一个局部变量，也叫 num，值是：30
    # num = 30
    # 全局变量声明：告诉python解释器，接下来函数中使用的num，是全局变量的num
    global num
    num = 30
    print('func1 num：', num)


def func2():
    print('func2 num：', num)


func1()
# func2()
print(num)



















"""
在调用函数时，给形参传递实参有如下2种方式：
位置参数(位置实参)：函数调用时，按形参的位置，从左到右，依次传递实参，缺一不可，不需要指定形参名称
关键字参数(关键字实参)：函数调用时，按照`形参名=值`的形式来传递实参，不必按照位置传递
    注意：对于同一形参不能重复传值
"""

# 位置参数(位置实参)

# def func1(num1, num2):
#     print('num1=', num1)
#     print('num2=', num2)
# func1(1,2)
#
# # 关键字参数
# def func1(num1, num2):
#     print('num1=', num1)
#     print('num2=', num2)
#
# func1(num2 = 2, num1 = 1)

"""
在函数定义时，函数的形参有如下4个分类：
* 普通形参：函数定义时，只要形参名称，调用函数时，普通形参必须传递实参
* 缺省形参：函数定义时，形参带有默认值，调用函数时，可以传实参，也可以不传实参，不传实参则会使用默认值
* 不定长形参：可以接收任意数量的实参
    * 元组不定长形参：用于接收任意数量的位置实参
    * 字典不定长形参：用于接收任意数量的关键字实参
"""


# 函数形参可以设置默认值
# 普通形参：函数定义时，只要形参名称，调用函数时，普通形参必须传递实参
# 缺省形参：函数定义时，形参带有默认值，调用函数时，可以传实参，也可以不传实参，不传实参则会使用默认值

# def func(a, b=20, c=10): # a为普通参数 b、c为缺省参数
#     print(a, b, c)
#
# # 函数调用
# func(1)  # a=1,b=20,c=10
# func(1, 2)  # a=1,b=2,c=10
# func(1, 3, 2)  # a=1,b=3,c=2



"""
不定长参数(可以接收任意数量实参的形参)：接收任意数量的实参
1）元组不定长参数：用于接收任意数量的位置实参
2）字 
"""
# a = 1
# b = 2
# c = 3
# d = 4
# print(a, b, c, d)

# *args 为不定长参数，可以接收0~多个实参
# 把实参的1,2,3, 包装成元组(1, 2, 3)再传递, 等价于args = (1, 2, 3)

# def func(*args):
#     # 函数内部使用，无需加*
#     print(args, type(args))
#
#
# # 函数调用
# func(1, 2, 3)   # (1, 2, 3) <class 'tuple'>

# 元组不定长参数：用于接收任意数量的位置实参
# def my_sum(*args):
#     res = 0
#
#     for i in args:
#         res += i
#
#     return res
#
# result = my_sum(1, 2, 3, 4, 5)
# print(result)

# 元组不定长参数本质：将用户传递的位置实参，包装成了元组，放到了 args 参数中


# 字典不定长参数：用于接收任意数量的关键字实参


# 字典不定长参数本质：将用户传递的关键字实参，包装成了字典，放到了 kwargs 参数


"""
函数调用实参传递的形式：
1）位置传递
2）关键字传递

函数形参的综合应用：
1）普通参数：必传的
2）缺省参数：带有默认值，可以不传，不传会使用默认值
3）元组不定长参数：接收任意数量的位置实参
4）字典不定长参数：接收任意数量的关键字实参

注意：多种类型参数需要注意次序
1）普通参数，元组不定长参数，缺省参数，字典不定长参数
"""

# *args
# **kwargs

# 把实参包装成 {'city': 'sz', 'age': 18}给kwargs传递
# kwargs = {'city': 'sz', 'age': 18}
def func(name, **kwargs):
    # 存在形参name, name不会被包装到字典中
    print(name)
    print(kwargs)  # 函数内部使用，无需加*


# 实参的写法： 变量=数据，变量=数据
func(name='mike', city='sz', age=18)




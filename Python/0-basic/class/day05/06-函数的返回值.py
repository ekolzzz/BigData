"""
调用函数之后，希望获取函数内部计算的结果，这就需要用到函数的返回值。

开发中，有时会希望 一个函数执行结束后，告诉调用者一个结果，以便调用者针对具体的结果做后续的处理。
返回值 是 函数给调用方提供的结果
"""

"""
变量 = input('提示信息')
变量 = len(容器数据)
"""

# num = input('请输入数字：')
# print(num)
#
# num_list = [1, 3, 2, 8, 9]
#
# _len = len(num_list)
# print(_len)


"""
函数需要通过 return 关键字返回值： return 结果

def 函数(参数1, 参数2):
    # 函数代码...
    return 返回值
    
注意：只要函数执行了 return 代码，函数调用就结束了，
如果函数中 return 之后还有代码，代码永远不会被执行到
"""

"""
需求：计算两个数的和，并返回计算的结果
"""
# def my_sum(num1 ,num2):
#     """计算两数之和"""
#     result = num1 + num2
#     return result
#
# res = my_sum(1,2)
# print(res)
# print(res ** 2)




"""
函数的默认返回值(其实也可以理解为函数没有返回值)
    如果没有在函数中使用return，函数默认也有返回值，是None
    函数 return 后面什么都没有，返回值也是 None
"""

def my_sum1(num1, num2):
    """计算两个数字的和"""
    result = num1 +num2
    return # 返回值None

res = my_sum1(1, 3)
print(res)




"""
def 函数():
    if 条件成立:
        # 函数结束，但是又不想有返回值
        return
    
    其他代码...
    其他代码...
    其他代码...
    其他代码...
"""
def func1(num1, num2):
    """计算一个数字乘以2的值"""

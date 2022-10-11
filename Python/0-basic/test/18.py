"""
18、定义一个参数为不定长（可变）类型的函数fun，同时传入一个列表和字典，求列表里的数字元素和字典里的value值它们的累积结果
例如：列表[1,2,3]，字典{‘a’: 4,‘b’: 5, ‘c’: 6},定义一个函数fun，输出它们的累积结果（1+2+3+4+5+6）
"""
# *args 元组不定长参数

# 忘了，等等就复习
def sum_fun(*args):

    args_sum = sum(args[0])

    my_dict = args[1]

    kwargs_sum = 0

    for value in my_dict.values():
        kwargs_sum += value

    return (args_sum+kwargs_sum)

print(sum_fun([1, 2, 3], {'a': 4, 'b': 5, 'c': 6}))
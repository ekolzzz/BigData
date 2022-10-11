import msg.splitLine as sl
"""
*args和**kwargs作为形参：
1）*args形参：元祖不定长形参，用于接收任意数量的位置实参
2）**kwargs形参：字典不定长形参，用于接收任意数量的关键字实参
"""

def funcl(*args,**kwargs):
    print(type(args),args) # (1,2,3,4)
    print(type(kwargs),kwargs) # {'a':5,'c':6,'d':7}



"""
*列表：传递实参时，如果在列表数据前加*，表示把列表中的每个元祖作为实参按位置传递给被调用函数的形参
**字典：传递实参时，如果在字典数据前加**，表示把字典中的每个key-value对作为一个关键字实参传递给被调用函数的形参，
       key相当于参数名，value相当于参数的值
"""


def func2(a,b,c):
    print(a)
    print(b)
    print(c)
    #func2(1,2,3)

my_list=[1,2,3]
#func2(my_list[0],my_list[1],my_list[2])
func2(*my_list)

sl.splitLine('分割线')

my_dict = {'a':1, 'b':2, 'c':3}
func2(**my_dict) # func2(a=1, b=2, c=3)
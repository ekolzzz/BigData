"""
魔法方法：__init__
学习目标：知道通过 __init__ 方法再创建实例对象时给对象添加属性
"""

"""
什么是魔法方法？
在Python中，所有以 __ 双下划线包起来的方法，都统称为 Magic Method ，中文称 魔法方法
格式：__方法名__

注意：
1）魔法方法是系统提供好的方法名字（【名称固定的】），用户需重新实现它
2）魔法方法一般情况下无需手动调用，在合适时候【自动会调用】
"""

"""
类的 __init__ 方法：
1）__init__ 方法叫做 对象的初始化方法，在 创建一个对象后会被自动调用，不需要手动调用
2）__init__ 方法的作用：给创建的对象添加属性
"""


class Dog(object):
    """狗类"""
    def __init__(self):
        """
        调用：每创建一个这个类的实例对象，这个类的 __init__ 魔法方法就会被自动调用一次，并且 self 就是创建出来的对象
        作用：__init__ 魔法方法的作用就是给创建的每个实例对象添加一些初始的默认属性，所以它也叫对象的初始化方法
        """
        print('Dog类的__init__魔法方法被调用')
        self.name = '旺财'
        self.age = 2
#
    def show_info(self):
        print(f'我的名字：{self.name}, 年龄：{self.age}')
#
#

print('================= 华丽的分割线 ===============')

# # 创建一个 dog1 对象
dog1 = Dog()

dog1.show_info()

print(dog1.name, dog1.age)

# # 通过 dog1 对象调用 show_info 方法
# dog1.show_info()
#
# print('================= 华丽的分割线 ===============')
# # 再创建一个 dog2 对象
# dog2 = Dog()
# print(dog2.name, dog2.age)
#
# # 结论：上面的 __init__ 代码，会导致创建出来的每个狗的实例对象两个属性的值都一样！


"""
__init__ 自定义参数：

1）__init__(self)除了默认参数self，还可以设置任意个数的自定义参数，例如：__init__(self,x,y,z)
2）__init__ 方法 设置的自定义参数必须和创建对象时传递的参数保持一致，例如：对象变量名 = 类名(x,y,z)

开发者可以 设置自定义参数，为对象的默认属性提供 不同的初始值
"""

# 需求：在创建每一个狗的实例对象时，可以动态指定每只狗的姓名和年龄属性的值


class Dog(object):
    """狗类"""
    # c++/java 构造函数
    def __init__(self, _name, _age):
        """
        调用：每创建一个这个类的实例对象，这个类的 __init__ 魔法方法就会被自动调用一次，并且 self 就是创建出来的对象
        作用：__init__ 魔法方法的作用就是给创建的每个实例对象添加一些初始的默认属性，所以它也叫对象的初始化方法
        形参：
        * _name：接收创建的狗的实例对象的姓名
        * _age：接收创建的狗的实例对象的年龄
        """
        print('Dog类的__init__魔法方法被调用')
        self.name = _name
        self.age = _age

    def show_info(self):
        print(f'我的名字：{self.name}, 年龄：{self.age}')


# 创建一个 dog1 对象
dog1 = Dog('小黑', 2)
print(dog1.name, dog1.age)

print('================= 华丽的分割线 ===============')
# 再创建一个 dog2 对象
dog2 = Dog('旺财', 1)
print(dog2.name, dog2.age)


class Cat(object): # 定义一个Cat类
    def __init__(self, _name, _age):
        print('Cat类的__init__魔法方法被调用')
        self.name = _name
        self.age = _age


    def show_info(self):
        print(f'我的名字:{self.name}, 年龄:{self.age}')

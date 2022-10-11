"""
魔法方法：__str__
学习目标：知道 print 打印对象时，输出 __str__ 方法的返回值
"""

"""
类的 __str__ 方法：
1）如果直接 print 打印对象，会看到创建出来的对象在内存中的地址
2）当使用 print(对象变量名) 输出对象的时候，只要类中定义了 __str__ 方法，就会打印 __str__ 方法返回值

__str__ 方法作用：
1）主要返回对象属性信息，print(对象变量名) 输出对象时直接输出 __str__ 方法返回的描述信息
2）注意：__str__ 方法的返回值必须是 字符串类型
"""


class Dog(object):
    """狗类"""
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    def show_info(self):
        print(f'我的名字：{self.name}, 年龄：{self.age}')

    #__str__方法实现
    def __str__(self):
        return f'我的名字:{self.name}, 年龄:{self.age}'


# 创建 dog1 对象
dog1 = Dog('小黑', 1)

res = str(dog1)
print(res)

print(dog1)


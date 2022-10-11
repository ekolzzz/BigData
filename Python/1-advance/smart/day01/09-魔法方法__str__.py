"""
魔法方法：__str__
学习目标：知道 print 打印对象时，输出 __str__ 方法的返回值
"""

"""
将一个实例对象转换为字符串：str(对象)
* 如果类中未定义__str__()方法，会看到转换的结果是对象在内存中的地址
* 如果类中定义了__str__()方法，则转换的结果是该类中__str__()方法的返回值
* 注意：__str__()方法的返回值必须是 字符串类型

print函数打印实例对象：print(对象)
* 如果类中未定义__str__()方法，会看到打印的结果是对象在内存中的地址
* 如果类中定义了__str__()方法，会看到打印结果是该类中__str__()方法的返回值
* 注意：print(对象)打印对象时，隐含着将对象转换为字符串的过程，print最终打印的就是转换后的结果
"""


class Dog(object):
    """狗类"""
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    def show_info(self):
        print(f'我的名字：{self.name}, 年龄：{self.age}')

    # __str__方法实现
    def __str__(self):
        """
        必须有返回值，而且必须为字符串
        作用：返回一个字符串，包含实例对象的一些属性的信息，方便 print(对象) 来查看对象的属性信息
        """
        # return 'hello world'
        return f'我的名字：{self.name}，年龄：{self.age}'


# 创建 dog1 对象
dog1 = Dog('小黑', 1)
# 使用 str 内置函数把实例对象 dog1 转换为字符串
# Dog 类中未定义 __str__ 魔法方法，结果为：'<__main__.Dog object at 0x000001B1B31E94C0>'
# Dog 类中定义了 __str__ 魔法方法，结果为：__str__ 方法的返回值
res = str(dog1)
print(res)


# 直接使用 print 打印一个对象
# 注意：当我们直接通过 print 打印一个对象时，其实会自动把这个对象转换为字符串，然后print打印的是转换的结果
print(dog1)

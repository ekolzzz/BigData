"""
单继承和多继承
学习目标：知道单继承和多继承的概念
"""

"""
单继承：子类定义时只继承一个父类
多继承：子类定义时同时继承多个父类
"""

"""
单继承：子类定义时只继承一个父类
"""


class Animal(object):
    """动物类"""
    def eat(self):
        print('吃东西')


# Dog 类定义时只继承了 Animal 类
class Dog(Animal):
    """狗类"""
    pass


# 创建一个 Dog 对象
dog1 = Dog()
dog1.eat()


"""
多继承：子类定义时同时继承多个父类

class 子类名(父类1, 父类2, ……)：
    pass
"""


class SmallDog(object):
    def eat(self):
        print('小口吃东西')

    def sleep(self):
        print('小憩一会')


class BigDog(object):
    def drink(self):
        print('大口喝水')

    def sleep(self):
        print('呼呼大睡')


# SuperDog 类定义时同时继承了 SmallDog 和 BigDog
class SuperDog(SmallDog, BigDog):
    pass


# 创建一个 SuperDog 对象
sd1 = SuperDog()
# SuperDog 从 SmallDog 继承了 eat 方法
sd1.eat()
# SuperDog 从 BigDog 继承了 drink 方法
sd1.drink()

"""
问题：子类继承的多个父类中有多个同名方法，`子类对象.同名方法(...)`调用哪个？
答：默认调用先继承的那个父类中的同名方法。
"""


"""
多层继承
学习目标：知道类的继承具有多层传递效果
"""

"""
代代相传
多层继承：继承关系为多层传递，如生活中的爷爷、父亲、儿子
"""


# 爷爷类
class Animal(object):
    """动物类"""
    def eat(self):
        print('吃东西')


# 爸爸类
class Dog(Animal):
    """狗类"""
    def drink(self):
        print('喝水')


# 儿子类
class SuperDog(Dog):
    pass


# 创建一个 SuperDog 对象
sd1 = SuperDog()
sd1.eat()
sd1.drink()

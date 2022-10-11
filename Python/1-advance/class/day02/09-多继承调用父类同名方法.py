"""
多继承调用父类同名方法
学习目标：多继承中，能够在子类重写父类方法之后，在子类中调用父类中的同名方法
"""

"""
子类调用父类同名方法

可以使用如下方式：

1）父类名.同名方法(self, 形参1, ……)
2）super(当前子类名, self).同名方法(形参1, ……)
3）super().同名方法(形参1, ……)：是方法 2 的简写，推荐的写法
"""

"""
示例1：
"""

class SmallDog(object):
    def eat(self):
        print('吃小东西')


class BigDog(object):
    def eat(self):
        print('啃大骨头')


class SuperDog(SmallDog, BigDog):
    def eat(self):
        print('吃蟠桃')

        # 需求1：调用 SmallDog 父类的 eat 方法

        # 需求2：调用 BigDog 父类的 eat 方法


# 创建一个 SuperDog 对象
sd1 = SuperDog()
sd1.eat()


"""
示例2：支付类
"""

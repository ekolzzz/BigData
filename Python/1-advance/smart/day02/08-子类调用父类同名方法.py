"""
子类调用父类同名方法
学习目标：能够在子类重写父类方法之后，在子类中调用父类中的同名方法
"""

"""
子类重写了父类的方法之后，若在子类方法中还想调用父类的同名方法。

可以使用如下方式：

1）父类名.同名方法(self, 形参1, ……)
2）super(子类名, self).同名方法(形参1, ……)
3）super().同名方法(形参1, ……)：是方法 2 的简写，推荐的写法
"""


class Animal(object):
    """动物类"""
    def __init__(self):
        print('Animal类中的__init__方法')
        self.type = '动物'

    def show_info(self):
        print(f'Animal类中的show_info方法，类型：{self.type}')


class Dog(Animal):
    def __init__(self):
        print('Dog类中的__init__方法')
        self.type = '狗'

    def show_info(self):
        print(f'Dog类中的show_info方法，类型：{self.type}')

        # 需求：如果在子类的方法中能够调用到父类中的同名 show_info 方法
        # 方式1：父类名.同名方法(self, ...)：【容易理解，不够灵活】
        Animal.show_info(self)
        # 方式2：super(子类名, self).同名方法(...)：【不容易理解，但灵活一点】
        super(Dog, self).show_info()
        # 方式3：super().同名方法(...)：方式2的简写：【不容易理解，但更灵活，推荐】
        super().show_info()


# 创建一个 Dog 对象
dog1 = Dog()
dog1.show_info()

"""
类的继承
学习目标：能够定义子类继承父类
"""

"""
类的继承：
    在面向对象编程中，子类可以直接继承父类，从而使子类直接具备父类的能力(属性和方法)

继承作用：  
    解决代码重用问题，提高开发效率

注：
1）站在父类的角度来看，父类派生出子类
2）站在子类的角度来看，子类继承于父类
3）父类也叫基类，子类也叫派生类

语法格式：

class 类名(父类名):
    pass
    
注：object 是 python 中所有类的父类
"""


class Father(object):
    """父类或基类"""
    def __init__(self):
        self.money = 99999999

    def show_money(self):
        print(f'身价：{self.money}')


class Son(Father):
    """子类或派生类"""
    pass


# 创建一个 Son 这个类的实例对象
son1 = Son()
print(son1.money)
son1.show_money()

"""
私有和继承
学习目标：知道父类中的私有属性和私有方法不能被子类继承
"""

"""
私有和继承：
    父类中的私有属性和方法不能被子类继承
    
如果子类想访问到父类中的私有属性和方法怎么办？

答：在父类中提供一个公有方法，在父类的公有方法中进行访问私有属性和方法，以此来达到子类能够间接
访问到父类中的私有属性和方法的效果。
"""


class Animal(object):
    """动物类"""
    def __init__(self, _name, _age):
        self.name = _name
        self.__age = _age

    def __pee(self):
        """pee：撒尿"""
        print('上厕所嘘嘘')

    def show_info(self):
        print(f'名字：{self.name}，年龄：{self.__age}')

    def sleep(self):
        # 睡觉撒尿
        self.__pee()
        print('睡觉了💤')


class Dog(Animal):
    """狗类"""
    def test(self):
        # Animal 中的私有属性和方法不能被 Dog 类继承
        # print(self.__age)
        # self.__pee()
        pass


# 创建一个 Dog 对象
dog1 = Dog('旺财', 20)
dog1.test()

"""
重写父类方法
学习目标：能够在子类中重写从父类继承的方法
"""

"""
重写父类(包括爷爷类及以上)方法：
1）父类(包括爷爷类及以上)的方法不能满足子类的需要，可以对父类(包括爷爷类及以上)的方法重写

重写的目的：从父类继承的方法不能满足子类的需要，为了拓展功能而重写

重写形式：
1）在子类中定义了一个和父类(包括爷爷类及以上)同名的方法(参数也一样)，即为对父类(包括爷爷类
及以上)的方法重写

注意：重写之后子类调用同名方法，默认只会调用子类的
"""


"""
案例1：
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
        """重写父类中的__init__"""
        # 先调用一下父类的__init__ 方法
        super().__init__()
        print('Dog类中的__init__方法')
        self.type = '狗'
        self.name = '翔翔'

    def show_info(self):
        """重写父类的 show_info"""
        print(f'Dog类中的show_info方法，类型：{self.type}')



# 创建一个 Dog 对象
dog1 = Dog()
dog1.show_info()


"""
案例2：支付类
"""



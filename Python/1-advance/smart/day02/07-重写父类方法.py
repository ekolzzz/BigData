"""
重写父类方法
学习目标：能够在子类中重写从父类继承的方法
"""

"""
重写父类(包括爷爷类及以上)方法：
1）父类(包括爷爷类及以上)的方法不能满足子类的需要，可以对父类(包括爷爷类及以上)的方法重写

重写的目的：从父类继承的方法不能满足子类的需要，为了拓展功能而重写

重写形式：
1）在子类中定义了一个和父类(包括爷爷类及以上)同名的方法，即为对父类(包括爷爷类及以上)的方法重写

注意：重写之后子类对象调用同名方法，默认只会调用子类的
"""


"""
案例1：
"""


class Animal(object):
    """动物类"""
    def __init__(self):
        print('Animal类中的__init__方法')
        self.type = '动物'
        self.age = 0

    def show_info(self):
        print(f'Animal类中的show_info方法，类型：{self.type}')


class Dog(Animal):
    def __init__(self):
        """重写父类中的 __init__"""
        # 先调用一下父类的 __init__ 方法
        super().__init__()
        print('Dog类中的__init__方法')
        self.type = '狗'
        self.name = '翔翔'

    def show_info(self):
        """重写父类的 show_info"""
        print(f'Dog类中的show_info方法，类型：{self.type}')


# 创建一个 Dog 对象
dog1 = Dog()
# dog1.show_info()
print(dog1.type)
print(dog1.age)
print(dog1.name)

"""
案例2：支付类
"""


# 标准：预留了需要子类重写的方法
# 在 java 中，类似于 java 中的一个概念：interface（接口）
# class PayClass(object):
#     """支付类"""
#     def pay(self):
#         """付款方法"""
#         pass
#
#     def refund(self):
#         """退款方法"""
#         pass
#
#
# class Alipay(PayClass):
#     """支付宝支付类"""
#     def pay(self):
#         """重写父类的pay方法，实现支付宝的付款逻辑"""
#         print('支付宝付款')
#
#     def refund(self):
#         """重写父类的refund方法，实现支付宝的退款逻辑"""
#         print('支付宝退款')
#
#
# class WeChat(PayClass):
#     """微信支付类"""
#     def pay(self):
#         """重写父类的pay方法，实现微信的付款逻辑"""
#         print('微信付款')
#
#     def refund(self):
#         """重写父类的refund方法，实现微信的退款逻辑"""
#         print('微信退款')


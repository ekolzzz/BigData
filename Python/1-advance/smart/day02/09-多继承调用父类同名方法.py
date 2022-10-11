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
        """重写了从父类继承的 eat 方法"""
        print('吃蟠桃')
        # 方式1：父类名.同名方法(self, ...)：【容易理解，不够灵活】
        # 需求1：调用 SmallDog 父类的 eat 方法
        SmallDog.eat(self)
        # 需求2：调用 BigDog 父类的 eat 方法
        BigDog.eat(self)
        # 方式2：super(指定类名, self).同名方法(...)
        # 原理：方式2的本质其实是调用原始那个类的继承顺序链上，你指定的那个类的下一个类中的同名方法。
        # 需求1：调用 SmallDog 父类的 eat 方法
        super(SuperDog, self).eat()
        # 需求2：调用 BigDog 父类的 eat 方法
        super(SmallDog, self).eat()
        # 方式3：super().同名方法(...)：其实是super(当前类名, self).同名方法(...)
        # 需求1：调用 SmallDog 父类的 eat 方法
        super().eat() # 等价于：super(SuperDog, self).eat()
        # 需求2：调用 BigDog 父类的 eat 方法
        # 方式3实现不了，只能使用方式1或方式2

# 类的继承顺序链
# 如果查看一个类的继承顺序链：类名.__mro__
# (<class '__main__.SuperDog'>, <class '__main__.SmallDog'>, <class '__main__.BigDog'>, <class 'object'>)
# print(SuperDog.__mro__)
#
# # 创建一个 SuperDog 对象
# sd1 = SuperDog()
# sd1.eat()


"""
示例2：支付类
"""

class PayClass(object):
    """支付类"""
    def pay(self):
        """付款方法"""
        pass

    def refund(self):
        """退款方法"""
        pass


class Alipay(PayClass):
    """支付宝支付类"""
    def pay(self):
        """重写父类的pay方法，实现支付宝的付款逻辑"""
        print('支付宝付款')

    def refund(self):
        """重写父类的refund方法，实现支付宝的退款逻辑"""
        print('支付宝退款')


class WeChat(PayClass):
    """微信支付类"""
    def pay(self):
        """重写父类的pay方法，实现微信的付款逻辑"""
        print('微信付款')

    def refund(self):
        """重写父类的refund方法，实现微信的退款逻辑"""
        print('微信退款')


class PayMax(Alipay, WeChat):
    """聚合支付类"""
    def pay_max(self, type):
        """
        如果 type 为 0，使用支付宝付款
        如果 type 为 1，使用微信付款
        """
        if type == 0:
            # 需求：调用 Alipay 类中的 pay 方法
            # 方式1：父类名.同名方法(self)
            # Alipay.pay(self)
            # 方式2：super(指定类名, self).同名方法()
            # super(PayMax, self).pay()
            # 方式3：super().同名方法()：是super(当前类名, self).同名方法()的简写
            super().pay() # super(PayMax, self).pay()
        elif type == 1:
            # 需求：调用 WeChat 类中的 pay 方法
            # 方式1：父类名.同名方法(self)
            # WeChat.pay(self)
            # 方式2：super(指定类名, self).同名方法()
            super(Alipay, self).pay()
        else:
            print('支付方式非法！不支持！')


# (<class '__main__.PayMax'>, <class '__main__.Alipay'>, <class '__main__.WeChat'>,
# <class '__main__.PayClass'>, <class 'object'>)
print(PayMax.__mro__)
obj = PayMax()
obj.pay_max(0)

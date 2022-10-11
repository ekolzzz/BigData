"""
多态：
学习目标：理解多态调用同一个方法，不同表现的特性
"""

"""
多态：多种形态，调用同一个函数，不同表现

因为Python是动态语言，站在用户的角度，本身就是多态，不存在非多态的情况

实现多态的步骤:
1）实现继承关系
2）子类重写父类方法
3）通过对象调用该方法
"""

class PayClass(object):
    """支付类"""
    def pay(self):
        """付款"""
        pass

    def refund(self):
        """退款"""
        pass


class Alipay(PayClass):
    """支付宝类"""
    def pay(self):
        print('支付宝付款')

    def refund(self):
        print('支付宝退款')


class WeChat(PayClass):
    """微信支付类"""
    def pay(self):
        print('微信付款')

    def refund(self):
        print('微信退款')

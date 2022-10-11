"""
多态：
学习目标：理解多态调用同一个方法，不同表现的特性
"""

"""
多态：多种形态，调用同一个函数，不同表现。【同一行代码，由于传递的实例对象的不同，最终代码调用有不同的表现】

因为Python是动态语言，站在用户的角度，本身就是多态，不存在非多态的情况。
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


def func(obj):
    """
    注意：给 obj 形参传递的实参必须有 pay 方法，否则 obj.pay() 会报错！！！
    """
    # ap1.pay()
    # wc1.pay()
    # 【同一行代码，由于传递的实例对象的不同，最终代码调用有不同的表现】
    obj.pay()


# 创建一个 Alipay 这个类的实例对象
ap1 = Alipay()
func(ap1)

# 再创建一个 WeChat 这个类的实例对象
wc1 = WeChat()
func(wc1)
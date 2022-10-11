class A(object):
    def func(self):
        print('A类中的func函数')


class C(A):
    def func(self):
        super().func() # 完整写法：super(C, self).func()
        print('C类中的func函数')


class B(object):
    def func(self):
        super().func() # 完整写法：super(B, self).func()
        print('B类中的func函数')


# class D(A, B, C):
#     def func(self):
#         super().func() # 完整写法：super(D, self).func()
#         print('D类中的func函数')

class D(B, C):
    def func(self):
        super().func() # 完整写法：super(D, self).func()
        print('D类中的func函数')

# 多继承的继承顺序链：画图
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(D.__mro__)

# 创建一个 D 这个类的对象
obj = D()
# 思考：代码执行的结果是什么？？？
obj.func()


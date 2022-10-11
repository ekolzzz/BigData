class A(object):
    def func(self):
        print('A类中的func函数')


class C(A):
    def func(self):
        super().func()
        print('C类中的func函数')


class B(A):
    def func(self):
        super().func()
        print('B类中的func函数')


class D(B, C):
    def func(self):
        super().func()
        print('D类中的func函数')


# 创建一个 D 这个类的对象
obj = D()
# 思考：代码执行的结果是什么？？？
obj.func()


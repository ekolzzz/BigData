class A(object):
    def func(self):
        print('A类中的func函数')


class B(A):
    def func(self):
        super().func()
        print('B类中的func函数')


class C(B):
    def func(self):
        super().func()
        print('C类中的func函数')


# 创建一个C这个类的对象
obj = C()
# 思考：代码的执行结果是什么？？？
obj.func()
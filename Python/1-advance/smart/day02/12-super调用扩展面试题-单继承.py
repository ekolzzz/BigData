class A(object):
    def func(self):
        print('A类中的func函数')


class B(A):
    def func(self):
        super().func() # 完整写法：super(B, self).func()
        print('B类中的func函数')


class C(B):
    def func(self):
        super().func() # 完整写法：super(C, self).func()
        print('C类中的func函数')


# 单继承的继承顺序链：其实就是一层一层往上找
# C的继承顺序链：C -> B -> A -> object
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
print(C.__mro__)

# 创建一个C这个类的对象
obj = C()
# 思考：代码的执行结果是什么？？？
obj.func()
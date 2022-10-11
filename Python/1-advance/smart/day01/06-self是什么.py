"""
self是什么？
学习目标：知道通过对象调用实例方法时，self形参就是对象本身
"""

"""
在 Python 类中规定，实例方法的第一个参数是实例对象本身，并且约定俗成，把其名字写为self。

某个对象调用其某个方法时，Python 解释器会自动把这个对象作为第一个参数传递给对应方法

通俗理解：通过哪个对象调用方法，方法中 self 就是这个对象
"""


class Dog(object):
    """狗类"""
    def show_info(self):
        print('测试self：', id(self))


# 创建一个 Dog 类的实例对象
dog1 = Dog()
print('测试dog1：', id(dog1))
# 我们在通过实例对象调用实例方法时，python解释器会自动将实例对象作为实参传递给形参self
# 本质：show_info(dog1)
dog1.show_info()

print('================= 华丽的分割线 ===============')

# 再创建一个 Dog 类的实例对象
dog2 = Dog()
print('测试dog2：', id(dog2))
# 本质：show_info(dog2)
dog2.show_info()


# 结论：通过哪个实例对象调用实例方法，实例方法的 self 形参就是哪个对象！！！

print('================= 华丽的分割线 ===============')

class Cat(object):
    def show_info(self):
        print('测试self：', id(self))


cat1 = Cat()
print('测试cat1：', id(cat1))
cat1.show_info()


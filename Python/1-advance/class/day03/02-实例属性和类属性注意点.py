"""
实例属性和类属性注意点
学习目标：知道实例属性和类属性使用的注意点
"""

"""
注意点1：如果类属性和实例属性同名，实例对象名只能操作实例属性

结论：操作类属性建议使用类名，避免不必要的麻烦
"""


class Dog(object):
    """狗类"""
    count = 0

    def __init__(self):
        self.count = 1


# 访问类属性 count
print(Dog.count)

# 创建一个 Dog 对象
dog1 = Dog()
# 注意：此处通过 dog1 对象只能访问到实例属性 count
print(dog1.count)

print('=' * 50)

"""
注意点2：类属性只能通过类对象修改，不能通过实例对象修改
"""


# class Dog(object):
#     """狗类"""
#     # 这是一个类属性
#     count = 0
#
#     def __init__(self, _name, _age):
#         self.name = _name
#         self.age = _age


# # 注意：只能通过`类名.类属性名`修改类属性
# Dog.count = 1
# print(Dog.count)
#
# # 注意：不能通过`对象名.类属性名`修改类属性
# dog1 = Dog('小黄', 2)
# # 此处是给 dog1 对象添加了一个实例属性：count，和类属性同名
# dog1.count = 3
# # 提示：此处访问的是 dog1 对象的实例属性：count，不是类属性：count
# print(dog1.count) # 结果为：
# print(Dog.count) # 结果为：
#
# print('=' * 50)

"""
注意点3：类属性也可以设置为私有，前边添加两个下划线__
"""


class Dog(object):
    """狗类"""
    __count = 0
#
#
# # 注意：类私有属性在类外部不能通过`类名.类属性名`访问
# # AttributeError: type object 'Dog' has no attribute '__count'
# print(Dog.__count)

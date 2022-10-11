"""
self的作用？
学习目标：知道通过 self 形参区分不同对象
"""

"""
在方法中使用 self，可以获取到调用当前方法的对象，进而获取到该对象的属性和方法

self作用：为了区分不同对象的属性和方法
"""


class Dog(object):
    """狗类"""
    pass


# 创建 dog1 实例对象
dog1 = Dog()
# 给 dog1 对象添加 name 和 age 两个属性
dog1.name = '小黑'
dog1.age = 2

# 需求：在 Dog 类中实现 show_info 方法，调用时打印：`我的名字：XXX，年龄：XXX`

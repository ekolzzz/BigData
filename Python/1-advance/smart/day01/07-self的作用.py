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
    def show_info(self):
        # 下面这句代码的问题：
        # 无论通过哪个实例对象调用，打印出来的都是 dog1 的信息
        # print(f'我的名字：{dog1.name}，年龄：{dog1.age}')

        # 需求：通过哪个对象调用的该方法，就打印出哪个对象的信息
        print(f'我的名字：{self.name}，年龄：{self.age}')


# 创建 dog1 实例对象
dog1 = Dog()
# 给 dog1 对象添加 name 和 age 两个属性
dog1.name = '小黑'
dog1.age = 2

# 需求：在 Dog 类中实现 show_info 方法，调用时打印：`我的名字：XXX，年龄：XXX`
dog1.show_info()

print('================= 华丽的分割线 ===============')
# 再创建 dog2 实例对象
dog2 = Dog()
dog2.name = '旺财'
dog2.age = 1
dog2.show_info()
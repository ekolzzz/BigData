"""
对象属性添加和使用
学习目标：能够给对象添加属性
"""

"""
对象既然有实例方法，也有自己的属性

对象添加/修改属性格式：
    对象变量名.属性名 = 数据
    第一次是添加

对象属性的访问格式：
    对象变量名.属性名

注：属性和变量类似，首次赋值时会定义属性，再次赋值改变属性
"""


# 需求：定义一个狗类
class Dog(object):
    """狗类"""
    # 定义在类的函数，叫方法
    # 注意：self参数是必填的，具体作用后面会进行讲解
    def eat(self):
        print('吃东西')

    def drink(self):
        print('喝东西')


# 创建一个 Dog 类对象
dog1 = Dog()
# 给 dog1 对象添加一个 name 属性，值为`小黑`
dog1.name = '小黑'
# 给 dog1 对象添加一个 age 属性，值为 2
dog1.age = 2
# 获取 dog1 对象的 name 和 age 属性的值
print(dog1.name)
print(dog1.age)
# 修改 dog1 对象的 age 属性的值，改为：3
dog1.age = 3
print(dog1.age)

print('================= 华丽的分割线 ===============')

dog1.name = '大黑'
print(dog1.name)


# 再创建一个 Dog 类的对象
dog2 = Dog()
dog2.name = '旺财'
dog2.age = 1
print(dog2.name)
print(dog2.age)

# 注意：一个类可以创建很多个实例对象，每个实例对象是独立的，它们都有自己的内存存储空间，
# 每个实例对象的属性数据保存在自己的内存存储空间中，互不影响！！！

print('================= 华丽的分割线 ===============')

dog3 = Dog()
dog3.name = 'ttt'
dog3.age = 3
print(dog3.name)
print(dog2.age)

"""
实例属性和类属性
学习目标：能够区分实例属性和类属性
"""

"""
在Python中 "万物皆对象"
1）通过类创建的对象 又称为 实例对象，对象属性 又称为 实例属性
1）类本身也是一个对象，执行class语句时会被创建，称为 类对象，为了和实例对象区分开来，我们习惯叫类

class Dog(object):
    pass
"""

"""
实例属性：属于单个实例对象的属性，不同实例对象互相独立，互不相干

实例属性添加：
1）通过在__init__方法里面给实例对象添加的属性
2）在类的外面，直接通过实例对象添加的属性

注意：实例属性只能通过`实例对象.实例属性名`进行访问

class 类名(object):
    def __init__(self):
        self.实例属性1 = 值1
        self.实例属性2 = 值2

# 创建实例对象
实例对象名 = 类名()

# 添加属性
实例对象名.实例属性3 = 值3
"""


class Dog(object):
    """狗类"""
    def __init__(self, _name, _age):
        # 在 __init__ 中给创建的实例对象添加初始的实例属性
        self.name = _name
        self.age = _age


dog1 = Dog('旺财', 1)
print(dog1.name, dog1.age)
# 注意：这里也是给实例对象添加了一个 color 实例属性
dog1.color = '黑色'
print(dog1.color)

print('================== 华丽的分割线 =================')

"""
类属性：类属性就是 类对象（也就是类） 所拥有的属性，它被 该类的所有实例对象 所共有

类属性添加：
1）定义在类定义内部，但在类方法外面的变量就是类属性

注意：类属性可以使用 `类名.类属性名` 或 `实例对象.类属性名` 访问【推荐使用类名访问】

class 类名(object):
    类属性名 = 值1

    def __init__(self):
        pass
"""
# 需求：保存 Dog 类一共创建了多少只狗


class Dog(object):
    """狗类"""
    # 类属性
    count = 0

    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age


# 访问类属性：`类名.类属性名`【推荐】
print(Dog.count)

# 修改类属性：`类名.类属性名 = 值`
Dog.count = 1
print(Dog.count)

# 区分实例属性和类属性
# 1）实例属性：每个实例对象都有一份，互相独立，会由各自的内存来保存
# 2）类属性：在这个类中只有一份，被这个类所有实例对象所共有

print('================== 华丽的分割线 =================')
"""
类属性有什么用？记录一类事物共同需要保存的内容
需求：记录一共创建了多少只狗的实例对象？
"""


class Dog(object):
    """狗类"""
    # 类属性
    count = 0

    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age
        # 注意：只要 __init__ 被调用一次，就说明创建了一只狗的实例对象
        Dog.count += 1


print(Dog.count)

dog1 = Dog('旺财', 1)
print(Dog.count)

dog2 = Dog('大白', 3)
print(Dog.count)



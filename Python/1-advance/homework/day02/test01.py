import msg.sl as sl

"""
3. 请写出一个Car作为基类,BMW类继承于Car类,基类中有`__init__`方法(包含name,color).

   创建Car和BMW的实例对象, 并分别打印对象的2个属性值
"""

# class Car(object):
#     def __init__(self, _name, _color):
#         self.name = _name
#         self.color = _color
#
#     # def __str__(self):
#     #     return  f'{self.name}是{self.color}'
#
# class BMW(Car):
#     pass
#
# new_car = Car('汽车', '黑色')
# new_BMW = BMW('宝马', '蓝色')
#
# print(new_car.name)
# print(new_BMW.name)
#
# print(new_car.color)
# print(new_BMW.color)
import cProfile

"""
4. 利用继承编写下面一段代码

   **要求：**

   1. 动物:吃,喝,跑,叫
   2. 猫的叫声是"喵喵"
   3. 狗的叫声是"旺旺"
   4. 猫狗继承于动物,并且有猫、狗有自己的属性.

   **运行结果：**

   ~~~
   喵喵
   花猫drink
   旺旺
   ~~~
"""

"""
面向对象思维分析：
1) 分解对象: 根据要解决的问题, 分析问题中涉及到哪些对象
    父类：动物
    子类：猫、狗
2) 抽象出类: 分解出每个对象抽象成一个类，分析类的对象有哪些属性和方法
    属性：叫声(sound)
    方法：吃(eat),喝(drink),跑(run)
3) 定义类: 根据2) 来定义类

4) 通过类创建对象, 实现功能
"""

# class Animals(object):
#
#     def eat(self):
#         print(f'{self.name}eat')
#
#     def drink(self):
#         print(f'{self.name}drink')
#
#     def run(self):
#         print(f'{self.name}run')
#
#     # def cry(self): # 每个动物都有自己的叫声，此处可以省略
#     #     pass
#
# class Cat(Animals):
#     def __init__(self, name):
#         self.name = name
#
#     def cry(self): # 重写父类方法
#         print('喵喵')
#
# class Dog(Animals):
#     def __init__(self, name):
#         self.name = name
#
#     def cry(self):  # 重写父类方法
#         print('旺旺')
#
# cat1 = Cat('大黄猫')
# cat1.eat()
#
# cat2 = Cat('花猫')
# cat2.drink()
#
# cat2 = Cat('黑猫')
# cat2.run()
#
# cat1 = Cat('大黄猫')
# cat1.cry()
#
# dog1 = Dog('八公')
# dog1.cry()

"""
4.创建一个动物类,其中有一个run方法

创建一个Cat类继承于动物类，Cat类中重写run方法，增加打印"迈着猫步跑起来"，同时实现eat方法

**运行结果：**

~~~
跑起来
迈着猫步跑起来
吃东西
~~~

**训练提示**

* 继承父类

* 重写父类方法
* 使用super方法调用父类方法
"""

# class Animals(object):
#
#     def run(self):
#         print('跑起来')
#
# class Cat(Animals):
#     def run(self): # 重写Cat类run方法
#         super(Cat, self).run()
#         super().run() # 简介
#         print('迈着猫步跑起来')
#
#     def eat(self):
#         print('吃东西')
#
# cat1 = Cat()
# cat1.run()
# cat1.eat()

"""
2.定义一个类，提供可以重新设置私有属性name的方法，限制条件为字符串长度小于10,才可以修改.

**训练提示**

* 定义私有属性
* 私有属性修改需要在本类中定义对应的方法修改属性

"""
# class Person(object):
#     def __init__(self, name):
#         self.__name = name
#         print(f'__init__里的{self.__name}')
#
#     def set_name(self, name):
#         if len(name) < 10:
#             self.__name = name
#             print(self.__name)
#         else:
#             print('字符过长错误')
#
# p1 = Person('ttt')
# p1.set_name('ttttttttttttttttttttttttttt')

"""
3.编写一段代码以完成下面的要求

**要求：**

1. 定义一个人的基类,类中要有初始化方法,方法中要有人的姓名,年龄.
2. 将类中的姓名和年龄私有化.
3. 提供获取用户信息的函数.
4. 提供获取私有属性的方法. # 私有属性只能在类中访问，可以通过公有方法间接调用
5. 提供可以设置私有属性的函数.
6. 设置年龄的范围(0-100).若设置的范围有误，则打印“输入的年龄错误！”

**运行结果：**
"""
# 如果子类想访问到父类中的私有属性和方法怎么办？
#
# 在父类中提供一个公有方法，在父类的公有方法中进行访问私有属性和方法，以此来达到子类能够间接 访问到父类中的私有属性和方法的效果。
# class Person(object):
#     """一个人类"""
#     def __init__(self, name, age):
#         # 姓名和年龄私有化
#         self.__name = name
#         self.__age = age
#
#     # 获取用户信息的函数
#     def get_info(self):
#         print(f'姓名：{self.__name},年龄：{self.__age}')
#
#     # 添加获取私有属性的方法，私有属性只能在类中访问，可以通过公有方法间接调用
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     # 设置姓名的函数
#     def set_name(self, name):
#         self.__name = name
#
#     # 设置年龄的函数
#     def set_age(self, age):
#         # 设置年龄的范围(0-100).若设置的范围有误，则打印“输入的年龄错误！”
#         if 0<= age <= 100 :
#             self.__age = age
#         else:
#             print('输入的年龄错误！')
#
# p1 = Person('张三', 20)
# p1.get_info()
#
# p1.set_age(30)
# p1.get_info()
#
# p2 = Person('李四', 30)
# p2.get_info()

# p1 = Person('ttt', 18)
# p1.get_info()
# p1.get_name()
#
# p1.set_name('tdp')
# p1.get_info()
#
# p1.set_age(81)
# p1.get_info()

"""
1.写出一个简单的多继承案例，并使用子类对象调用所有的父类方法。比如 LuoZi 类同时继承 Ma类、Lv类。
"""

# class Ma:
#     def run(self, name):
#         self.name = name
#         print(f'{self.name}跑得快')
#
# class Lv():
#     def send(self, name):
#         self.name = name
#         print(f'{self.name}拉的多')
#
# class Luozi(Ma, Lv):
#      pass
#
# luozi = Luozi()
# luozi.run('骡子')
# luozi.send('骡子')


"""
2.按如下要求实现代码：

- 创建一个动物的基类,其中有一个run方法
- 创建一个Cat类继承于动物类，具有私有属性__name = "波斯猫"
- 创建一个Dog类继承于动物类,具有私有属性__name = "京巴狗"
- Cat类中不仅有run方法还有eat方法
- Dog类中方法同上
- 创建一个letRun函数，可以接收动物及其子类对象，并调用run方法 class Cat(Animal):
- 编写测试代码以验证功能正常
- 运行结果：

```
跑起来
波斯猫在跑
波斯猫在吃
京巴狗在跑
京巴狗在吃
```

"""
class Animals(object):
    """动物类"""

    # run方法
    def run(self):
        print('跑起来')

class Cat(Animals): # 继承动物类
    """猫类"""
    def __init__(self):
        # 私有属性__name = "波斯猫"
        self.__name = '波斯猫'

    def run(self):
        print(f'{self.__name}在跑')

    def eat(self):
        print(f'{self.__name}在吃')

class Dog(Animals): # 继承动物类
    """狗类"""
    def __init__(self):
        # 私有属性__name = "京巴狗"
        self.__name = '京巴狗'

    def run(self):
        print(f'{self.__name}在跑')

    def eat(self):
        print(f'{self.__name}在吃')

# 创建一个letRun函数，可以接收动物及其子类对象，并调用run方法 class Cat(Animal):
def letRun(obj): # obj形参
    obj.run() # 实例对象.run()实现调用run方法

animal = Animals()
letRun(animal)

sl.sl()

cat = Cat()
letRun(cat) # 和cat.run()效果相同
cat.run()
cat.eat()

sl.sl()

dog = Dog()
letRun(dog) # 和cat.run()效果相同
dog.run()
dog.eat()

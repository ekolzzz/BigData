"""
- 定义动物类，

  1. 使用`__init__`方法，在创建对象时接收参数，为其添加name、age、color、food等属性，如"熊猫"，5, "黑白"，"竹子"
  2. 为动物类定义一个run方法，调用run方法时打印相关信息。如打印出“熊猫正在奔跑”
  3. 为动物类定义一个get_age方法，调用get_age方法时打印相关信息。如打印出“这只熊猫今年5岁了"
  4. 为动物类定义一个eat方法，调用eat方法时打印相关信息。如打印出“熊猫正在吃竹子”
  5. 通过动物类分别创建出2只不同的动物，分别调用它们的方法，让他们跑起来，吃起来
  6. 直接打印对象的时候，返回动物的所有信息

"""

"""
面向对象思维分析：
1) 分解对象: 根据要解决的问题,分析问题中涉及到哪些对象

2) 抽象出类: 分解出每个对象抽象成一个类，分析类的对象有哪些属性和方法

3) 定义类: 根据2) 来定义类

4) 通过类创建对象,实现功能

动物类：
1）属性
    _name：哪个明星
    _age：哪部电影
    _color：评价【好看】【非常好看】【难看】【非常难看】
    _food：食物

2）方法
    __init__：属性初始化、、、在创建对象时接收参数，为其添加name、age、color、food等属性，如"熊猫"，5, "黑白"，"竹子"
    run：打印相关信息。如打印出“熊猫正在奔跑”
    get_age：打印相关信息。如打印出“这只熊猫今年5岁了"
    eat：打印相关信息。如打印出“熊猫正在吃竹子”

"""
class Animals(object): # 类名要用大驼峰命名
    def __init__(self, _name, _age, _color, _food):
        self.name = _name
        self.age = _age
        self.color = _color
        self.food = _food

    def __str__(self):
        return f'你好呀！我是一只{self.name}，今年{self.age}岁了，我的颜色是{self.color}，我喜欢吃{self.food}'

    def run(self):
        print(f'{self.name}正在奔跑')

    def get_age(self):
        print(f'这只{self.name}今年{self.age}了')

    def eat(self):
        print(f'{self.name}正在吃{self.food}')

animal1 = Animals('熊猫', '5', '黑白', '竹子')
animal1.run()
animal1.get_age()
animal1.eat()
print(animal1)
# animal2 = Animals()
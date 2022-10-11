"""
- 定义一个汽车类Car

  - 在类中定义一个move方法打印'汽车在移动'
  - 分别创建BMW_X9、AUDI_A9两个对象

  - 并添加颜色、型号等属性，然后打印出属性值
  - 使用\_\_init\_\_方法, 以达到在创建对象的同时，就为对象添加对应的属性的目的
  - 添加\_\_str\_\_方法，以实现当直接打印对象时，能打印出可读性较高的信息。例如：我的颜色是 红色，型号是 X9

"""

"""
面向对象思维分析：
1) 分解对象: 根据要解决的问题,分析问题中涉及到哪些对象

2) 抽象出类: 分解出每个对象抽象成一个类，分析类的对象有哪些属性和方法
    
3) 定义类: 

4) 通过类创建对象,实现功能

汽车类：
1）属性
    color: 颜色
    model: 型号

2）方法
    __init__: 为实例对象添加初始化属性
    __str__: 打印出可读性较高的信息。例如：我的颜色是 红色，型号是 X9
    move: 打印'汽车在移动'
"""

class Car(object):
    def __init__(self, _color, _model):
        self.color = _color
        self.model = _model

    def __str__(self):
        # 例如：我的颜色是 红色，型号是 X9
        return f'我的颜色是{self.color}，型号是{self.model}'

    def move(self):
        print('汽车在移动')

BMW_X9 = Car('红色', 'X9')
AUDI_A9 = Car('蓝色', 'A9')

print(BMW_X9)
print(AUDI_A9)

# Python进阶01-面向对象

[TOC]

## 能力目标

- [ ] 知道类是由方法(函数)和属性(变量)构成
- [ ] 知道使用class关键字定义一个类
- [ ] 能够说出调用对象中的方法的语法格式
- [ ] 能够给对象添加属性
- [ ] 知道方法的self参数的作用
- [ ] 知道\__init__方法的作用
- [ ] 知道如何定义带参数和不带参数的\__init__方法
- [ ] 知道\__str__方法的作用
- [ ] 知道烤地瓜案例的需求和实现思路



## 关卡一：概念题

### 1. 简述类和对象的关系

**参考答案**：

```python
类是一个抽象的概念，对象是由类所创造出的实体，一个类可以创建多个对象；
类相当于图纸，对象相当于由图纸造出的实物；
```



### 2. 实例方法的 self 形参是什么？self有什么作用？

**参考答案**：

```python
通过哪个对象调用实例方法，实例方法的self形参就是哪个对象；
作用：self形参的作用就是区分不同的实例对象，访问不同实例对象的属性和方法；
```



### 3. \__init__魔法方法什么时候调用？它有什么作用？

**参考答案**：

```python
每通过类创建一个实例对象，该类的__init__魔法方法就会被调用一次；
作用：__init__魔法方法也被称为对象的初始化方法，用于给创建的实例对象添加一些初始的属性。
```

## 关卡二：综合题

### 1. 设计一个程序:

- 定义一个Star类(明星类)， 通过明星类创建一个zhou_xing_chi对象

  使用\__init__方法给对象添加属性 

  定义方法playing()，打印“xxx出演了yyy，非常好看”

**参考答案**

```python
class Star(object):
    def __init__(self,name,movie):
        self.name = name
        self.movie = movie
        
    def playing(self):
        print("%s出演了%s，非常好看"%(self.name,self.movie))
        
zhou_xing_chi = Star('周星驰', "功夫")
zhou_xing_chi.playing()
```



### 2. 设计一个程序:

- 定义一个Star类(明星类)， 通过明星类创建一个zhou_xing_chi对象

  使用init方法给对象添加属性 

  print输出对象时打印"xxx是我的偶像，我非常喜欢他的电影yyy"

  xxx为明星姓名，yyy是电影的名字

**参考答案**

```python
class Star(object):
    def __init__(self, name, movie):
        self.name = name
        self.movie = movie

    def __str__(self):
        return "%s是我的偶像，我非常喜欢他的电影%s" % (self.name, self.movie)


zhou_xing_chi = Star('周星驰', "功夫")
print(zhou_xing_chi)
```



### 3. 设计一个程序:

- 定义一个汽车类Car

  - 在类中定义一个move方法打印'汽车在移动'
  - 分别创建BMW_X9、AUDI_A9两个对象
  - 并添加颜色、型号等属性，然后打印出属性值
  - 使用\_\_init\_\_方法, 以达到在创建对象的同时，就为对象添加对应的属性的目的
  - 添加\_\_str\_\_方法，以实现当直接打印对象时，能打印出可读性较高的信息。例如：我的颜色是 红色，型号是 X9

**参考答案**

```python
class Car(object):

    def __init__(self, color, model):
        self.color = color
        self.model = model

    def move(self):
        print('汽车在移动')

    def __str__(self):
        return '我的颜色是 %s，型号是 %s' % (self.color, self.model)

BMW_X9 = Car('白色','X9')
AUDI_A9 = Car('黑色', 'A9')

print(BMW_X9)
print(AUDI_A9)
```



### 4. 设计一个程序

- 定义动物类，

  1. 使用`__init__`方法，在创建对象时接收参数，为其添加name、age、color、food等属性，如"熊猫"，5, "黑白"，"竹子"
  2. 为动物类定义一个run方法，调用run方法时打印相关信息。如打印出“熊猫正在奔跑”
  3. 为动物类定义一个get_age方法，调用get_age方法时打印相关信息。如打印出“这只熊猫今年5岁了"
  4. 为动物类定义一个eat方法，调用eat方法时打印相关信息。如打印出“熊猫正在吃竹子”
  5. 通过动物类分别创建出2只不同的动物，分别调用它们的方法，让他们跑起来，吃起来
  6. 直接打印对象的时候，返回动物的所有信息

**参考答案**

```python
class Animal(object):
    def __init__(self, name, age, color, food):
        self.name = name
        self.age = age
        self.color = color
        self.food = food

    def run(self):
        print('%s 正在奔跑' % self.name)

    def get_age(self):
        print('这只 %s 今年 %d 岁了' % (self.name, self.age))

    def eat(self):
        print('%s 正在吃 %s' % (self.name, self.food))

    def __str__(self):
        return '你好呀，我是一只%s，今年%s岁了，我的颜色是%s，我喜欢吃%s' % (self.name, self.age, self.color, self.food)

animal = Animal('熊猫', 5, '黑白', '竹子')
animal.eat()
animal.get_age()
animal.run()
print(animal)
```



# Python进阶02-面向对象

[TOC]

## 能力目标

- [ ] 知道公有权限和私有权限的区别
- [ ] 知道继承的作用
- [ ] 知道单继承和多继承
- [ ] 知道类继承的多层传递效果
- [ ] 知道子类重写父类方法的原因
- [ ] 知道使用super()能够调用父类的同名方法
- [ ] 知道多态的好处


## 关卡一：综合题

### 1. 私有

按步骤实现如下需求:

1.定义一个人的基类,类中要有初始化方法,方法中初始化人的姓名,年龄.

**参考答案**

```python
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

2.提供\__str__方法，返回姓名和年龄信息

**参考答案**

```python
def __str__(self):
    return '%s 的年龄是 %d' % (self.name, self.age)
```

3.将类中的姓名和年龄私有化.

**参考答案**

```python
def __init__(self, name, age):
    self.__name = name
    self.__age = age
```

4.提供获取私有属性的方法.

**参考答案**

```python
def get_name(self):
    return self.__name

def get_age(self):
    return self.__age
```

5.提供可以设置私有属性的方法.

**参考答案**

```python
def set_name(self, new_name):
    self.__name = new_name

def set_age(self, new_age):
    self.__age = new_age
```

6.设置年龄时限制范围(0-100).

**参考答案**

```python
def set_age(self, new_age):
    if new_age > 0 and new_age <= 100:
        self.__age = new_age
    else:
        print('年龄设置失败，必须要在 0-100 之内')
```



### 2. 继承

1. 继承有什么好处？
   **参考答案**

   ```
   继承可以让子类直接使用父类的属性和方法，实现代码的复用，提高开发效率
   ```

2. 请写出继承的语法格式。
   **参考答案**

   ```python
   class 子类名(父类名):
       pass
   ```

3. 请写出一个Car作为基类,BMW类继承于Car类,基类中有\__init__方法(包含name,color).

   创建Car和BMW的实例对象, 并分别打印对象的2个属性值
   **参考答案**

   ```python
   class Car(object):
       def __init__(self, name, color):
           self.name = name
           self.color = color
           
   class BMW(Car):
       pass
   
     
   car = Car('A9', '白色')
   print(car.name)
   print(car.color)
   
   bmw = BMW('X8', '白色')
   print(bmw.name)
   print(bmw.color)
   
   ```


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

   **参考答案**

   ~~~python
   class Animal():
       def eat(self):
           print("--%seat" % self.name)
   
       def drink(self):
           print("%sdrink" % self.name)
   
       def run(self):
           print("%s running" % self.name)
   
       def cry(self):
           pass # 为什么
   
   
   class Cat(Animal):
       def __init__(self, name):
           self.name = name
   
       def cry(self):
           print("喵喵")
   
   
   class Dog(Animal):
       def __init__(self, name):
           self.name = name
   
       def cry(self):
           print("旺旺")
   
   
   cat1 = Cat('大黄猫')
   cat1.cry()
   
   cat2 = Cat('花猫')
   cat2.drink()
   
   dog1 = Dog('八公')
   dog1.cry()
   ~~~

   

### 3. 重写

1.如果子类中没有定义`__init__`方法,但是要实例化一个对象,那此时会调用父类的`__init__`方法吗?
**参考答案**

```
会，子类没有的功能会跟父类要，如果父类也没有则会导致报错
```

2.如果子类重写了`__init__`方法,那么在实例化对象的时候,你觉得会调用哪个`__init__`方法,是父类的还是子类的?
**参考答案**

```
子类的，当子类重写了父类方法，则默认调用子类的方法
```

3.当子类重写`__init__`方法,在实例化对象的时候,如果想要调用父类的`__init__`方法该怎么办?
**参考答案**

```python
子类需要手动调用父类方法
调用父类方法有三种方式
# 方式1 
父类名.方法名(self, 参数列表)
# 方式2,
super().方法名(参数列表)
# 方式3
super(子类名, self).方法名(参数列表)
```

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

**参考答案**

~~~python
class Animal(object):
    def run(self):
        print("跑起来")

class Cat(Animal):
    def run(self):
        super(Cat, self).run()
        # 简写形式
        # super().run()
        print("迈着猫步跑起来")
        
    def eat(self):
        print("吃东西")

c = Cat()
c.run()
c.eat()
~~~



### 4. 私有与继承

1.父类中的私有属性能被子类继承吗，子类能直接使用父类的私有属性吗?
**参考答案**

```python
父类中的 私有方法、属性，不会被子类继承;
不能，可以通过调用继承的父类的共有方法，间接的访问父类的私有方法、属性
```

2.定义一个类，提供可以重新设置私有属性name的方法，限制条件为字符串长度小于10,才可以修改.

**训练提示**

* 定义私有属性
* 私有属性修改需要在本类中定义对应的方法修改属性

**参考答案**

~~~python
class Person(object):
 def __init__(self, name):
     self.__name = name

 def set_name(self, name):
     if len(name) < 10:
         self.__name = name
~~~

3.编写一段代码以完成下面的要求

**要求：**

1. 定义一个人的基类,类中要有初始化方法,方法中要有人的姓名,年龄.
2. 将类中的姓名和年龄私有化.
3. 提供获取用户信息的函数.
4. 提供获取私有属性的方法.
5. 提供可以设置私有属性的函数.
6. 设置年龄的范围(0-100).若设置的范围有误，则打印“输入的年龄错误！”

**运行结果：**

~~~
张三:20
张三:30
李四:30
~~~

**参考答案**

~~~python
class Person():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 获取用户信息的函数
    def print_info(self):
        print("%s:%s" % (self.__name, self.__age))

    # 添加获取私有属性的方法
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # 添加设置姓名的函数
    def set_name(self, name):
        self.__name = name

    # 添加设置年龄的函数
    def set_age(self, age):
        if (0 < age <= 100):
            self.__age = age
        else:
            print("输入的年龄错误!")


p = Person("张三", 20)
p.print_info()

p.set_age(30)
p.print_info()

p.set_name('李四')
p.print_info()
~~~

### 5. 多继承

1.写出一个简单的多继承案例，并使用子类对象调用所有的父类方法。比如 LuoZi 类同时继承 Ma类、Lv类。
**参考答案**

```python
class Ma(object):
    
    def run(self):
        print('马跑的快')

class Lv(object):
    
    def walk(self):
        print('驴走得远')

class LuoZi(Ma, Lv):
    pass

luozi = LuoZi()
luozi.run()
luozi.walk()
```

### 6. 多态

1.面向对象开发的三个基本特征是什么？

**参考答案**

```python
面向对象三大特性: 封装\继承\多态

封装: 将事物抽象成一个类, 区分出属性和方法, 并提供权限控制
继承: 继承一个父类, 获得父类的公有的方法和属性. 作用是:可以提高代码的复用
多态: 传入不同的对象, 调用同名方法, 执行不同的效果 (核心是方法同名). 作用是:方便程序的功能扩展

Python的多态和其他语言不一样: 其他语言, 必须有继承\必须有重写, 才能实现多态.
因为其他语言对数据类型有严格的要求, 定义参数时, 会指明参数的类型. 如果不是同一个类或者子类, 那么无法传入.
Python只要不同的类方法同名即可实现
```



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

**参考答案**

```python
# 1.创建一个动物的基类,其中有一个run方法
class Animal(object):
    def run(self):
        print('跑起来')


# 2.创建一个Cat类继承于动物类
class Cat(Animal):
    # 4.Cat类中不仅有run方法还有eat方法
    def __init__(self):
        self.__name = "波斯猫"

    def run(self):
        print('%s在跑' % self.__name)

    def eat(self):
        print('%s在吃' % self.__name)


# 3.创建一个Dog类继承于动物类
class Dog(Animal):
    # 5.方法同上
    def __init__(self):
        self.__name = "京巴狗"

    def run(self):
        print('%s在跑' % self.__name)

    def eat(self):
        print('%s在吃' % self.__name)


# 6.创建一个letRun函数，可以接收动物及其子类对象，并调用run方法 class Cat(Animal):
# 需求给 animal 形参传递的是一个动物对象
def letRun(obj):
    # 同一行的代码，由于传入的实例对象的不同，最终有不同的调用效果
    obj.run()


# 7.编写测试代码以验证功能正常
# 动物测试
animal = Animal()
letRun(animal)

# 猫测试
cat = Cat()
letRun(cat)
cat.eat()

# 狗测试
dog = Dog()
letRun(dog)
dog.eat()
```

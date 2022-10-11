"""
面向对象应用-烤地瓜案例-升级版
学习目标：理解烤地瓜案例升级版代码的实现
"""

"""
烤地瓜需求拓展：
1）地瓜可以添加佐料：如 盐、孜然、辣酱等
2）输出地瓜信息时，可以显示地瓜的状态、烧烤总时间、以及添加过的所有佐料
"""

"""
面向对象编程的思维步骤：
① 根据需要解决的问题来分解对象（拆解对象）：地瓜对象
    实际面向对象编程时，对于对象的拆解很多时并没有那么细。
    比如说咱们这个烤地瓜的案例，由于案例比较简单，只拆解一个地瓜对象就可以了。

② 把对象抽象成类，分析类的属性（对象需要保存的数据）和方法（对象能够干什么）：地瓜类
    第①步拆解了几个对象，第②步就应该抽象出几个类，然后分析每个类应该有的属性和方法

③ 根据第②步的抽象，来把类定义出来
④ 通过类创建实例对象，通过实例对象来完成功能

面向对象类的属性和方法分析：
1）地瓜类(SweetPotato)
    属性：（对象需要保存的数据）
        state：保存地瓜对象的状态，默认为生的，状态可能是：生的、半生不熟、熟了、烤糊了
        cooked_time：保存地瓜烧烤的总时间，默认为0
        condiments：保存地瓜对象烧烤过程中添加的佐料，默认为：[]

    方法：（对象能够干什么）
        __init__(self)：地瓜对象的初始化方法，给创建的地瓜对象添加初始的属性：state、cooked_time
        cook(self, time)：地瓜烧烤的方法，形参time接收地瓜每次烧烤的时间
        add_condiment(self, item)：地瓜添加佐料的方法，形参item接收每次添加的佐料
        __str__(self)：返回一个字符串，包含地瓜对象的状态和烧烤的总时间，还有添加过的所有佐料
"""


class SweetPotato(object):
    """地瓜类"""
    def __init__(self):
        """
        地瓜对象的初始化方法，给创建的地瓜对象添加初始的属性：state、cooked_time
        """
        # 给创建的地瓜对象添加一个初始的属性：state，保存地瓜的状态
        self.state = '生的'
        # 给创建的地瓜对象添加一个初始的属性：cooked_time，保存地瓜烧烤的总时间
        self.cooked_time = 0
        # 给创建的地瓜对象添加一个初始的属性：condiments，保存地瓜烧烤过程中添加的所有佐料
        self.condiments = []

    def __str__(self):
        """
        返回一个字符串，包含地瓜对象的状态和烧烤的总时间
        """
        return f'地瓜的状态：{self.state}，烧烤总时间：{self.cooked_time}，添加的佐料：{self.condiments}'


    def cook(self, time):
        """
        地瓜烧烤的方法，形参time接收地瓜每次烧烤的时间
        """
        # 将地瓜烧烤的总时间进行累加
        self.cooked_time += time

        # 根据地瓜烧烤的总时间来改变地瓜的状态
        if 0 <= self.cooked_time < 3:
            self.state = '生的'
        elif 3 <= self.cooked_time < 6:
            self.state = '半生不熟'
        elif 6 <= self.cooked_time < 8:
            self.state = '熟了'
        else:
            self.state = '烤糊了'

    def add_condiment(self, item):
        """
        地瓜添加佐料的方法，形参item接收每次添加的佐料
        """
        self.condiments.append(item)


# 创建一个地瓜对象
sp1 = SweetPotato()
print(sp1)

# 烧烤一次地瓜，烤2分钟
sp1.cook(2)
# 添加一次佐料
sp1.add_condiment('辣椒面')
print(sp1)

# 再烧烤一次地瓜，再烤2分钟
sp1.cook(2)
# 再添加一次佐料
sp1.add_condiment('酱油')
print(sp1)

# 再烧烤一次地瓜，再烤2分钟
sp1.cook(2)
# 再添加一次佐料
sp1.add_condiment('芥末')
print(sp1)

# 再烧烤一次地瓜，再烤2分钟
sp1.cook(2)
# 再添加一次佐料
sp1.add_condiment('玛莎拉')
print(sp1)





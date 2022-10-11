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
面向对象思维分析：

地瓜类：
1）属性
    state：地瓜状态【生的、半生不熟、熟了、烤糊了】
    cooked_time：烧烤时间
    condiments：添加的佐料 列表[]

2）方法
    __init__：地瓜属性初始化
    __str__：输出地瓜信息
    cook：地瓜烧烤方法
    add_condiment(self, item)：添加烧烤佐料,形参item用于接收添加的佐料
"""

class SweetPotato(object):
    """地瓜类"""
    def __init__(self):
        # 地瓜对象的初始化方法,给创建的地瓜对象添加初始的属性,状态和烧烤总时间
        self.state = '生的'
        self.cooked_time = 0
        self.condiments = []

    def __str__(self):
        # 返回一个字符串, 包含地瓜对象的状态和烧烤总时间
        return f'地瓜的状态:{self.state}, 烧烤总时间: {self.cooked_time}, 添加的佐料：{self.condiments}'

    def cook(self, time):
        self.cooked_time += time
        if 0 <= self.cooked_time <3:
            self.state = '生的'
        elif 3 <= self.cooked_time <6:
            self.state = '半生不熟'
        elif 6<= self.cooked_time <8:
            self.state = '熟了'
        else:
            self.state = '烤糊了'

    def add_condiment(self,item):
        # add_condiment(self, item)：添加烧烤佐料,形参item用于接收添加的佐料
        self.condiments.append(item)
        pass


# 创建一个地瓜对象
sp1 = SweetPotato()
print(sp1)

# 烤了一次地瓜
sp1.cook(2)
sp1.add_condiment('盐')
print(sp1)

# 烤了一次地瓜
sp1.cook(2)
sp1.add_condiment('孜然')
print(sp1)

# 烤了一次地瓜
sp1.cook(2)
sp1.add_condiment('辣椒')
print(sp1)

# 烤了一次地瓜
sp1.cook(2)
sp1.add_condiment('玛莎拉')
print(sp1)

# 再创建一个地瓜对象
# sp2 = SweetPotato()
# print(sp2)



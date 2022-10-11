"""
面向对象应用-烤地瓜案例-基础版
学习目标：理解烤地瓜案例基础版代码的实现
"""

"""
烤地瓜规则：
1）地瓜有自己的状态，默认是生的，地瓜可以进行烧烤
2）地瓜有自己烧烤的总时间，由每次烧烤的时间累加得出
3）地瓜烧烤时，需要提供本次烧烤的时间
4）地瓜烧烤时，地瓜状态随着烧烤总时间的变化而改变：[0, 3) 生的、[3, 6) 半生不熟、[6, 8) 熟了、>=8 烤糊了
5）输出地瓜信息时，可以显示地瓜的状态和烧烤的总时间
"""

"""
面向对象思维分析：
1) 分解对象:根据要解决的问题,分析问题中涉及到哪些对象
    地瓜、烤箱、人
2) 抽象出类:
    分解出每个对象抽象成一个类，分析类的对象有哪些属性和方法
3) 定义类

4) 通过类创建对象,实现功能
地瓜类：
1）属性
    state：地瓜状态【生的、半生不熟、熟了、烤糊了】
    cooked_time：烧烤时间

2）方法
    __init__：地瓜属性初始化
    __str__：输出地瓜信息
    cook：地瓜烧烤方法
"""

class SweetPotato(object):
    """地瓜类"""
    def __init__(self):
        # 地瓜对象的初始化方法,给创建的地瓜对象添加初始的属性,状态和烧烤总时间
        self.state = '生的'
        self.cooked_time = 0

    def __str__(self):
        # 返回一个字符串, 包含地瓜对象的状态和烧烤总时间
        return f'地瓜的状态:{self.state}, 烧烤总时间: {self.cooked_time}'

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

# 创建一个地瓜对象
sp1 = SweetPotato()
print(sp1)

# 烤了一次地瓜
sp1.cook(2)
print(sp1)

# 烤了一次地瓜
sp1.cook(2)
print(sp1)

# 烤了一次地瓜
sp1.cook(2)
print(sp1)

# 烤了一次地瓜
sp1.cook(2)
print(sp1)

# 再创建一个地瓜对象
sp2 = SweetPotato()
print(sp2)




















"""
面向对象应用案例-搬家具-升级版
学习目标：理解搬家具案例升级版代码实现
"""

"""
搬家具规则：

1）家具分不同的类型，并占用不同的面积
2）输出家具信息时，显示家具的类型和家具占用的面积
3）房子有自己的地址和占用的面积
4）房子可以添加家具，如果房子的剩余面积可以容纳家具，则提示家具添加成功；否则提示添加失败
5）输出房子信息时，可以显示房子的地址、占地面积、剩余面积

扩展需求：输出房子时，显示包含的所有家具的类型，print(房子对象)
"""

"""
面向对象编程的思维步骤：
① 根据需要解决的问题来分解对象（拆解对象）：房子对象、家具对象
    实际面向对象编程时，对于对象的拆解很多时并没有那么细。

② 把对象抽象成类，分析类的属性（对象需要保存的数据）和方法（对象能够干什么）：房子类、家具类
    第①步拆解了几个对象，第②步就应该抽象出几个类，然后分析每个类应该有的属性和方法

③ 根据第②步的抽象，来把类定义出来
④ 通过类创建实例对象，通过实例对象来完成功能

面向对象类的属性和方法分析：
1）家具类（Item）
    属性：
        type：保存家具的类型
        area：保存家具的面积

    方法：
        __init__(self, _type, _area)：家具对象的初始方法，给创建的家具对象添加初始的属性：type、area
        __str__(self)：返回一个字符串，包含家具对象的类型和占用的面积

2）房子类（Home）
    属性：
        address：保存房子的地址
        area：保存房子的占地面积
        free_area：保存房子的剩余面积，默认等于房子的占地面积
        item_list：保存房子中添加过的家具类型，默认为：[]
    方法：
        __init__(self, _address, _area)：房子对象的初始化方法，给创建的房子对象添加初始的属性：address、area、free_area
        add_item(self, item)：向房子中添加家具的方法，形参item接收向房子中添加的【家具对象】
        __str__(self)：返回一个字符串，包含房子的地址、面积、剩余面积、房子中添加过的家具类型
"""


class Item(object):
    """家具类"""
    def __init__(self, _type, _area):
        """
        家具对象的初始方法，给创建的家具对象添加初始的属性：type、area
        """
        self.type = _type
        self.area = _area

    def __str__(self):
        """
        返回一个字符串，包含家具对象的类型和占用的面积
        """
        return f'家具类型：{self.type}，占用面积：{self.area}'


# 测试：创建一个家具对象
# item1 = Item('桌子', 10)
# print(item1)


class Home(object):
    """房子类"""

    def __init__(self, _address, _area):
        """
        房子对象的初始化方法，给创建的房子对象添加初始的属性：address、area、free_area
        """
        self.address = _address
        self.area = _area
        self.free_area = _area  # 默认剩余面积等于房子的面积
        self.item_list = [] # 保存房子中添加过的所有家具类型

    def __str__(self):
        """
        返回一个字符串，包含房子的地址、面积、剩余面积、房子中添加过的所有家具类型
        """
        return f'房子的地址：{self.address}，占地面积：{self.area}，剩余面积：{self.free_area}，添加的家具：{self.item_list}'

    def add_item(self, item):
        """
        作用：向房子中添加家具的方法
        形参：
        * item：接收向房子中添加的【家具对象】
        注意：对象也是一个变量，也可以作为实参传递给形参
        """
        # 判断房子的剩余面积是否能够容纳家具（判断房子的剩余面积是否大于等于家具的面积）
        # self.free_area：房子的剩余面积
        # item.area：添加家具的面积
        if self.free_area >= item.area:
            # 如果能够容纳家具，则提示：家具添加成功！
            print(f'家具{item.type}添加成功！')
            # 减少房子的剩余面积
            self.free_area -= item.area
            # 将添加的家具类型保存到房子对象的 item_list 属性中
            self.item_list.append(item.type)
        else:
            # 否则提示：家具添加失败！
            print(f'家具{item.type}添加失败！')


# 测试：创建一个房子对象
home1 = Home('北京昌平', 100)
print(home1)

# 向房子中添加一个家具
item1 = Item('椅子', 10)
home1.add_item(item1)
print(home1)

# 再向房子添加一个家具
item2 = Item('桌子', 20)
home1.add_item(item2)
print(home1)

# 再向房子添加一个家具
item3 = Item('大床', 70)
home1.add_item(item3)
print(home1)
"""
实例方法、类方法和静态方法
学习目标：能够区分实例方法、类方法和静态方法
"""


"""
实例方法：属于实例对象的方法，第一个形参是self，只能通过实例对象进行调用，self形参就是实例对象

实例对象.实例方法(...)：self就是那个实例对象
"""


class Dog(object):
    """狗类"""
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    # 实例方法：只能通过实例对象进行调用
    def show_info(self):
        print(f'我的名字：{self.name}, 年龄：{self.age}')


print('======================= 示例1 =======================')
# 创建一个 Dog 对象
dog1 = Dog('小黄', 1)
dog1.show_info()

dog2 = Dog('大黄', 2)
dog2.show_info()

"""
类方法：属于类对象(类)的方法，可以通过类名【推荐】或实例对象名进行调用

什么时候应该用类方法？你的这个方法只需要访问类属性的数据，不需访问实例对象的数据

作用：用于对一类事物进行操作，和具体的某个实例对象没有直接关联关系，若类中的方法方法在逻辑上采用
类本身来调用更合理，那么这个方法就可以定义为类方法

需求：在类中提供一个方法，展示一共有多少只狗

定义：
    class 类名(object):
        @classmethod
        def 类方法名(cls):
            pass

注意：类方法必须有一个形参，一般叫 cls，调用类方法是 cls 形参不用传递，python解释器会自动传递
"""


class Dog(object):
    # 类属性
    count = 0

    def __init__(self, _name, _age):
        # 实例属性
        self.name = _name
        self.age = _age

        # 只要__init__调用，就说明创建了一个对象，类属性 count 就加1
        Dog.count += 1

    # 实例方法：只能通过实例对象进行调用
    def show_info(self):
        print(f'我的名字：{self.name}, 年龄：{self.age}')

    # 需求：提供一个显示一共有多少只狗的方法
    @classmethod
    def show_dog_count(cls):
        # print('测试cls：', id(cls))
        # print(f'现在一个有{Dog.count}只狗')
        print(f'现在一个有{cls.count}只狗')


print('======================= 示例2 =======================')

print('测试Dog：', id(Dog))
# 调用类方法：`类名.类方法名(...)`【推荐】
# 本质：show_dog_count(Dog)
Dog.show_dog_count()

dog1 = Dog('小黑', 1)
Dog.show_dog_count()

dog2 = Dog('大黄', 3)
Dog.show_dog_count()


"""
静态方法：主要是用来存放逻辑性的代码，逻辑上属于类，但是和类本身没有关系，也就是说在静态方法中，
不会涉及到类中的属性和方法的操作。可以理解为，静态方法是个独立的、单纯的函数，它仅仅托管于某个
类中，便于使用和维护。


定义：
    class 类名(object):
        @staticmethod
        def 静态方法名():
            pass
            
注意：静态方法不需要有 self 或 cls 参数
"""


class SysManager(object):
    """管理系统类"""
    # 需求：提供一个显示菜单的方法
    @staticmethod
    def show_menu():
        print('====================')
        print('= 1. 新增一个学生')
        print('= 2. 查询所有学生')
        print('= 3. 查询某个学生')
        print('= 4. 修改某个学生')
        print('= 5. 删除某个学生')
        print('= ...')
        print('====================')


print('======================= 示例3 =======================')
# 调用静态方法：`类名.静态方法(...)`【推荐]
SysManager.show_menu()


# 区分实例方法、类方法、静态方法
# 1）实例方法：需要访问每个实例对象的数据
# 2）类方法：只需要访问类属性的数据，跟实例对象没关系
# 3）静态方法：没有使用类中的任何数据（实例属性和类属性都用不到）











"""
面向对象版-学生名片管理系统
学习目标：常握面向对象版学生名片管理系统的实现
"""

"""
面向对象分析：

学生类：Student
    属性：
        name：姓名
        age：年龄
        tel：电话
    方法：
        __init__(self, _name, _age, _tel)：初始化学生对象的属性
        __str__(self)：打印学生对象时，显示学生对象的信息

管理类：SysManager
    属性：
        str_list：保存所有学生的数据
    方法：
        show_menu(self)：显示菜单
        add_stu_info(self)：添加学生数据
        show_all_stu(self)：显示所有学生数据
        show_one_stu(self)：查询指定学生数据
        update_one_stu(self)：修改指定学生数据
        delete_one_stu(self)：删除指定学生数据
        load_info(self)：从文件中加载学生数据
        save_info(self)：将学生数据保存到文件中
        start(self)：学生管理系统主逻辑
        
数据存储分析：
1）存储一个学生数据：学生对象
2）存储所有学生学生：列表嵌套学生对象
"""
import os

class Student(object):
    """学生类：Student"""
    i = 0
    def __init__(self, _name, _age, _tel):
        # 初始化学生对象的属性
        self.name = _name
        self.age = _age
        self.tel = _tel
        self.i += 1

    def __str__(self):
        # 打印学生对象时，显示学生对象的信息
        # print('序号\t\t姓名\t\t年龄\t\t电话')
        # for i, stu in enumerate(SysManager.get_stu_list(self)) :
        #     print(f'{i + 1}\t\t{stu.name}\t\t{stu.age}\t\t{stu.tel}')
        return f'姓名：{self.name}，年龄：{self.age}，电话：{self.tel}'
        # print(f'姓名：{self.name}，年龄：{self.age}，电话：{self.tel}')
        # return  f'{self.i+1}\t\t{self.name}\t\t{self.age}\t\t{self.tel}'

    def to_dict(self):
        """将学生对象的数据转换为一个字典"""
        return {'name': self.name, 'age': self.age, 'tel': self.tel}

class SysManager(object):
    """管理类：SysManager"""

    def __init__(self):
        """管理系统类初始化方法"""
        # 给管理系统类实例对象添加一个初始的属性 stu_list，默认为：[]
        self.stu_list = []

    def get_stu_list(self):
        return  self.stu_list

    @staticmethod
    # 静态方法：
    # 主要是用来存放逻辑性的代码，逻辑上属于类，但是和类本身没有关系，也就是说在静态方法中，不会涉及到类中的属性和方法的操作。
    # 静态方法是个独立的、单纯的函数，它仅仅托管于某个类中，便于使用和维护。
    def show_menu(): # 静态方法不需要传递形参
        """开始菜单静态方法"""
        print('=' * 30)
        print('= 1. 添加学生')
        print('= 2. 查询所有学生')
        print('= 3. 查询某个学生')
        print('= 4. 修改某个学生')
        print('= 5. 删除某个学生')
        print('= 6. 保存信息')
        print('= 7. 退出系统')
        print('=' * 30)

    # 添加学生数据
    def add_stu_info(self):
        _name = input('请输入要添加的学生姓名：')

        # 判断输入的名字是否已经存在，若不存在则可以添加，若存在则提升已存在
        for stu in self.stu_list : # manager.stu_list.append(stu1) manager.stu_list.append(stu2) 已经将学生对象信息添加到列表中了
            # 遍历self.stu_list, stu就是学生对象 stu
            if stu.name == _name :
                print(f'该学生{_name}已存在，请勿重复添加！')
                break
            # 上面的逻辑：需要遍历完所有数据后确定没有重复的值才会执行下一步骤

            # 这段代码是只有当不是break结束的时候才会执行
        else:
            _age = int(input(f'请输入{_name}的年龄：'))
            _tel = input(f'请输入{_name}的电话：')

            # 创建一个 Student 实例对象，保存添加的学生数据
            stu = Student(_name, _age, _tel)

            # 将添加的学生对象存储到 user_list 中
            self.stu_list.append(stu)

        # print('添加学生数据')

    # 显示所有学生数据
    def show_all_stu(self):
        print('序号\t\t姓名\t\t年龄\t\t电话')

        for i, stu in enumerate(self.stu_list) : # stu是个实例对象
            print(f'{i+1}\t\t{stu.name}\t\t{stu.age}\t\t{stu.tel}')

        # for stu in self.stu_list:
        #     print(type(stu), str(stu))
        # print('显示所有学生数据')

    # 查询指定学生数据
    def show_one_stu(self):
        _name = input('请输入要查询的学生姓名：')

        for i, stu in enumerate(self.stu_list) : # stu是个实例对象

            if stu.name == _name:
                print('序号\t\t姓名\t\t年龄\t\t电话')
                print(f'{i + 1}\t\t{stu.name}\t\t{stu.age}\t\t{stu.tel}')
                break
        else:
            # 如果学生不存在，则提示：查无此人！该学生不存在！
            print(f'查无此人！该学生{_name}不存在！')

        # for stu in self.stu_list :
        #     # 遍历self.stu_list, stu就是学生对象 stu
        #     if stu.name == _name :
        #         print('姓名\t\t年龄\t\t电话')
        #         print(f'{stu.name}\t\t{stu.age}\t\t{stu.tel}')
        #         break
        #     # 上面的逻辑：需要遍历完所有数据后确定没有重复的值才会执行下一步骤
        #
        # # 这段代码是只有当不是break结束的时候才会执行
        # else:
        #     # 如果学生不存在，则提示：查无此人！该学生不存在！
        #     print(f'查无此人！该学生{_name}不存在！')

        # print('查询指定学生数据')

    # 修改指定学生数据
    def update_one_stu(self):
        _name = input('请输入要修改的学生姓名：')

        # 如果学生已存在，提示输入修改之后的姓名、年龄、电话，然后将对应的学生数据进行修改
        for stu in self.stu_list:  # stu是个实例对象

            if stu.name == _name:
                stu.name = input('请输入修改之后学生姓名：')
                # 这里应该要判断新输入要修改的名字是否已存在在对象中
                stu.age = int(input(f'请输入修改之后的年龄：'))
                stu.tel = int(input(f'请输入修改之后的电话：'))
                break

        else:
            # 如果学生不存在，则提示：查无此人！该学生不存在！
            print(f'查无此人！该学生{_name}不存在！')

        # print('修改指定学生数据')

    # 删除指定学生数据
    def delete_one_stu(self):
        _name = input('请输入要删除的学生姓名：')

        for i, stu in enumerate(self.stu_list):
            if stu.name == _name:
                del self.stu_list[i]
                break

        else:
            # 如果学生不存在，则提示：查无此人！该学生不存在！
            print(f'查无此人！该学生{_name}不存在！')
        # print('删除指定学生数据')

    # 将学生数据保存到文件中
    def save_info(self):
        """保存学生数据"""
        # 将 stu_list 中每个学生对象的数据转换为一个字典
        _list = []

        for stu in self.stu_list:
            stu_dict = stu.to_dict()
            # print(stu_dict)

            _list.append(stu_dict)

        with open('./A.txt', 'w', encoding= 'utf8') as f:
            content = str(_list)
            f.write(content)

        # print('将学生数据保存到文件中')

    # 从文件中加载学生数据
    def load_info(self):
        if not os.path.exists('./A.txt'):
            print('A.txt文件不存在！')
            return

        # 读取 A.txt 文件中的内容
        with open('./A.txt', 'r', encoding='utf8') as f:
            content = f.read() # 以str的形式读取数据
            # print(type(content), content) # <class 'str'> [{'name': 'ttt', 'age': 18, 'tel': 123}, {'name': 'tdp', 'age': 16, 'tel': 234}]
            stu_list = eval(content)
            # print(type(stu_list), stu_list) # <class 'list'> [{'name': 'ttt', 'age': 18, 'tel': 123}, {'name': 'tdp', 'age': 16, 'tel': 234}]

        for stu in stu_list: # stu是字典
            # print(stu)
            # 根据字典中数据创建学生对象
            stu = Student(stu['name'], stu['age'], stu['tel'])

            # 并将学生对象添加到 user_list 中
            self.stu_list.append(stu)

        # print('从文件中加载学生数据')

    # 开始
    def start(self):

        self.load_info()
        self.show_menu()

        while True :

            # print(manager.stu_list)
            # self.show_all_stu()

            in_num = int(input('请输入功能数字：'))

            if in_num == 1 :
                self.add_stu_info()

            elif in_num == 2 :
                self.show_all_stu()

            elif in_num == 3:
                self.show_one_stu()

            elif in_num == 4:
                self.update_one_stu()

            elif in_num == 5:
                self.delete_one_stu()

            elif in_num == 6:
                self.save_info()

            elif in_num == 7:
                print('学生管理系统已退出！')
                break

            else:
                print('输入错误，请重新输入！')

# 创建一个管理系统类的对象
manager = SysManager()

# stu1 = Student('ttt', 18, 123)
# print(str(stu1))
#
# stu2 = Student('tdp', 16, 234)
# print(str(stu2))

# 将学生对象添加到管理系统初始化方法列表中
# manager.stu_list.append(stu1)
# manager.stu_list.append(stu2)
#
# print(manager.stu_list)

manager.start()
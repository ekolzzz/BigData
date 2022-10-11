"""
面向对象版-学生名片管理系统
学习目标：常握面向对象版学生名片管理系统的实现
"""

"""
面向对象分析：
1）学生类(Student)
    属性：
        name：姓名
        age：年龄
        tel：电话fgr
    方法：
        __init__(self, _name, _age, _tel)：学生实例对象的初始化方法，用于给学生实例对象添加初始的属性
        __str__(self)：返回一个字符串，包含学生的信息：姓名、年龄、电话

2）管理系统类(SysManger)
    属性：
        user_list：保存所有学生的数据，默认为：[]
    方法：
        __init__(self)：管理系统类初始化
        show_menu()：静态方法，显示功能菜单
        add_stu_info(self)：添加一个学生
        show_all_stu(self)：查询所有学生
        show_one_stu(self)：查询某个学生
        update_one_stu(self)：修改某个学生
        delete_one_stu(self)：删除某个学生
        save_data(self)：保存学生数据，将学生的数据保存到文件中
        load_data(self)：加载学生数据，从文件中读取学生的数据
        start(self)：管理系统的主逻辑方法，通过这个启动管理系统
        
学生数据的存储：
1）如何保存一个学生的数据？
    之前：字典 {'name': 'smart', 'age': 18, 'tel': '138'}
    现在：实例对象 Student('smart', 18, '138')
    
2）如何保存多个学生的数据？   
    之前：列表套字典 [{'name': 'smart', 'age': 18, 'tel': '138'}, {'name': 'linda', 'age': 16, 'tel': '133'}, ...]
    现在：列表套对象 [Student('smart', 18, '138'), Student('linda', 16, '133'), ...]
"""
import os

class Student(object):
    """学生类"""
    def __init__(self, _name, _age, _tel):
        """学生实例对象的初始化方法"""
        self.name = _name
        self.age = _age
        self.tel = _tel

    def __str__(self):
        """必须返回一个字符串，包含学生的信息"""
        return f'姓名：{self.name}，年龄：{self.age}，电话：{self.tel}'

    def to_dict(self):
        """将学生对象的数据转换为一个字典"""
        return {'name': self.name, 'age': self.age, 'tel': self.tel}


# 测试创建一个学生对象
# stu1 = Student('smart', 18, '138')
# print(stu1)


class SysManager(object):
    """管理系统类"""
    def __init__(self):
        """管理系统类初始化方法"""
        # 给管理系统类实例对象添加一个初始的属性 stu_list，默认为：[]
        self.user_list = []

    @staticmethod
    def show_menu():
        """
        显示功能菜单
        """
        print('====================')
        print('= 1. 添加学生')
        print('= 2. 查询所有学生')
        print('= 3. 查询某个学生')
        print('= 4. 修改某个学生')
        print('= 5. 删除某个学生')
        print('= 6. 保存信息')
        print('= 7. 退出系统')
        print('====================')

    def add_stu_info(self):
        """添加一个学生数据"""
        # print('添加一个学生数据')
        # 提示用户输入要添加的学生姓名
        _name = input('请输入学生的姓名：')

        # 根据输入的姓名，判断学生是否存在
        for user in self.user_list:
            # 注意：这里的 user 是一个 Student 实例对象
            # 如果学生已存在，则提示：该学生已存在！不允许重复添加！
            if user.name == _name:
                print(f'该学生{_name}已存在！不允许重复添加！')
                break
        else:
            # 如果学生不存在，则提示输入学生的年龄和电话，并保存添加的学生的数据
            _age = int(input('请输入学生的年龄：'))
            _tel = input('请输入学生的电话：')

            # 创建一个 Student 实例对象，保存添加的学生数据
            stu = Student(_name, _age, _tel)

            # 将添加的学生对象存储到 user_list 中
            self.user_list.append(stu)

    def show_all_stu(self):
        """显示所有学生数据"""
        # print('显示所有学生数据')
        # 遍历 user_list，获取并显示所有学生的信息：序号、姓名、年龄、电话
        print('序号\t\t姓名\t\t年龄\t\t电话')

        for i, user in enumerate(self.user_list):
            print(f'{i+1}\t\t{user.name}\t\t{user.age}\t\t{user.tel}')

    def show_one_stu(self):
        """查询指定学生"""
        # print('查询指定学生数据')
        # 提示用户输入要查询的学生姓名
        _name = input('请输入学生的姓名：')

        # 根据输入的姓名，遍历查询对应的学生
        for i, user in enumerate(self.user_list):
            # 如果学生已存在，则显示对应学生的数据
            if user.name == _name:
                print('序号\t\t姓名\t\t年龄\t\t电话')
                print(f'{i + 1}\t\t{user.name}\t\t{user.age}\t\t{user.tel}')
                break
        else:
            # 如果学生不存在，则提示：查无此人！该学生不存在！
            print(f'查无此人！该学生{_name}不存在！')

    def update_one_stu(self):
        """更新指定学生数据"""
        # print('更新指定学生数据')
        # 提示用户输入要修改的学生姓名
        _name = input('请输入学生的姓名：')

        # 根据输入的姓名，遍历查找对应的学生
        for user in self.user_list:
            # 如果学生已存在，提示输入修改之后的姓名、年龄、电话，然后将对应的学生数据进行修改
            if user.name == _name:
                new_name = input('请输入修改之后的姓名：')
                new_age = int(input('请输入修改之后的年龄：'))
                new_tel = input('请输入修改之后的电话：')

                # 修改学生对象的name、age和tel这三个属性的值
                user.name = new_name
                user.age = new_age
                user.tel = new_tel
                break
        else:
            # 如果学生不存在，则提示：查无此人！该学生不存在！
            print(f'查无此人！该学生{_name}不存在！')

    def delete_one_stu(self):
        """删除指定学生数据"""
        # print('删除指定学生数据')
        # 提示用户输入要删除的学生姓名
        _name = input('请输入学生的姓名：')

        # 根据输入姓名，遍历查找对应的学生
        for i, user in enumerate(self.user_list):
            # 如果学生已存在，则删除对应的学生数据
            if user.name == _name:
                del self.user_list[i]
                break
        else:
            # 如果学生不存在，则提示：查无此人！该学生不存在！
            print(f'查无此人！该学生{_name}不存在！')

    def save_data(self):
        """保存学生数据"""
        # print('保存学生数据')
        # 将 user_list 中学生的数据保存到一个 stu.txt 文件
        # with open('./stu.txt', 'w', encoding='utf8') as f:
        #     content = str(self.user_list)
        #     f.write(content)

        # 将 user_list 中每个学生对象的数据转换为一个字典
        stu_list = []

        for user in self.user_list:
            # 将学生对象的数据保存到一个字典中
            # stu_dict = {'name': user.name, 'age': user.age, 'tel': user.tel}
            stu_dict = user.to_dict()
            # 将字典添加到 stu_list 列表中
            stu_list.append(stu_dict)

        # 再将转换的结果写入 stu.txt 文件中
        with open('./stu.txt', 'w', encoding='utf8') as f:
            content = str(stu_list)
            f.write(content)

    def load_data(self):
        """加载学生数据"""
        # print('加载学生数据')
        # 判断 stu.txt 文件是否存在
        # if not False
        if not os.path.exists('./stu.txt'):
            print('stu.txt文件不存在！')
            return

        # 读取 stu.txt 文件的内容
        with open('./stu.txt', 'r', encoding='utf8') as f:
            content = f.read() # str
            # [{'name': 'smart', 'age': 18, 'tel': '138'}, {'name': 'linda', 'age': 16, 'tel': '133'}]
            stu_list = eval(content) # list套字典

        # 遍历 stu_list，获取每个学生的字典数据，然后根据字典中数据创建学生对象，并将学生对象添加到 user_list 中
        for stu_dict in stu_list:
            # 根据字典中数据创建学生对象
            _name = stu_dict['name']
            _age = stu_dict['age']
            _tel = stu_dict['tel']
            stu = Student(_name, _age, _tel)

            # 并将学生对象添加到 user_list 中
            self.user_list.append(stu)

    def start(self):
        """管理系统的主逻辑方法"""
        # 从 stu.txt 文件中加载学生的数据
        self.load_data()

        while True:
            # 打印 user_list 数据
            print(self.user_list)

            # 显示功能菜单
            SysManager.show_menu()

            # 接收用户的输入
            cmd_num = input('请输入功能数字：')

            # 根据用户的输入，判断用户要进行操作
            if cmd_num == '1':
                self.add_stu_info()
            elif cmd_num == '2':
                self.show_all_stu()
            elif cmd_num == '3':
                self.show_one_stu()
            elif cmd_num == '4':
                self.update_one_stu()
            elif cmd_num == '5':
                self.delete_one_stu()
            elif cmd_num == '6':
                self.save_data()
            elif cmd_num == '7':
                print('退出系统！')
                self.save_data()
                break
            else:
                print('输入有误！请重新输入！')


# 创建一个管理系统类的对象
manager = SysManager()

# 假设已经存在了两个学生
stu1 = Student('smart', 18, '138')
stu2 = Student('linda', 16, '133')
manager.user_list.append(stu1)
manager.user_list.append(stu2)

print(manager.user_list)
manager.start()

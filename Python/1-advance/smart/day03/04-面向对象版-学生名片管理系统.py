"""
面向对象版-学生名片管理系统
学习目标：常握面向对象版学生名片管理系统的实现
"""
import os

"""
数据存储的分析：
1）如何保存一个学生的信息（姓名、年龄、电话）？
    之前：字典
        {'name': 'smart', 'age': 18, 'tel': '138'}
        {'name': 'linda', 'age': 16, 'tel': '135'}
    现在：对象
        Student('smart', 18, '138')
        Student('linda', 16, '135')
    
2）如果保存多个学生的信息？
    之前：列表套字典
        [{'name': 'smart', 'age': 18, 'tel': '138'}, {'name': 'linda', 'age': 16, 'tel': '135'}, ...]
    现在：列表套对象（列表中的每个元素都是一个对象）
        [Student('smart', 18, '138'), Student('linda', 16, '135'), ...]
        
面向对象编程过程分析：
1）分解对象：问题中涉及到哪些对象
    学生对象、管理系统对象
2）抽象出类：分析类的对象的属性和方法
    学生类（Student）、管理系统类（SysManager）
3）定义出类：根据第2）步的分析定义出类
4）创建对象，通过对象完成功能


分析类的属性和方法：
1）学生类（Student）
    属性：
        name：学生的姓名
        age：学生的年龄
        tel：学生的电话
    方法：
        __init__(self, _name, _age, _tel)：学生对象的初始化方法，给创建的学生对象添加初始的属性
        __str__(self)：返回一个字符串，包含学生对象的姓名、年龄、电话
2）管理系统类（SysManager）
    属性：
        stu_list：保存所有学生的数据，默认为[]
    方法：
        __init__(self)：管理系统对象初始化方法
        show_menu()：显示功能菜单，静态方法
        add_stu_info(self)：添加一个学生的数据
        show_all_stu(self)：查询所有学生的数据
        show_one_stu(self)：查询某个学生的数据
        update_one_stu(self)：修改某个学生的数据
        delete_one_stu(self)：删除某个学生的数据
        save_data(self)：将学生的数据保存到文件中
        load_data(self)：从文件中读取学生的数据
        start(self)：管理系统的主逻辑方法（框架代码）
"""


class Student(object):
    """学生类"""
    def __init__(self, _name, _age, _tel):
        """学生对象初始化方法，给创建的学生对象添加初始的属性"""
        self.name = _name
        self.age = _age
        self.tel = _tel

    def __str__(self):
        """返回一个字符串，包含学生对象的姓名、年龄、电话"""
        return f'姓名：{self.name}，' \
               f'年龄：{self.age}，' \
               f'电话：{self.tel}'


class SysManager(object):
    """管理系统类"""
    def __init__(self):
        """管理系统对象的初始化方法，添加初始的属性"""
        self.stu_list = [] # 保存所有学生的数据

    @staticmethod
    def show_menu():
        """显示功能菜单方法"""
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
        """添加一个学生的数据"""
        # print('添加一个学生的数据')
        # 提示用户输入要添加的学生的姓名
        _name = input('请输入学生的姓名：')

        # 判断添加学生的姓名和已经存在的学生的姓名是否存在重复
        for stu in self.stu_list:
            # stu：学生对象
            if stu.name == _name:
                # 如果存在重复，则提示：该学生已存在！不允许重复添加！
                print(f'该学生{_name}已存在！不允许重复添加！')
                break
        else:
            # 如果不存在重复，则提示输入要添加的学生的年龄和电话，然后进行数据保存
            _age = int(input('请输入学生的年龄：'))
            _tel = input('请输入学生的电话：')

            # 创建一个学生对象，保存新增学生的数据
            new_stu = Student(_name, _age, _tel)

            # 将添加的学生对象放入管理系统对象的 stu_list 中
            self.stu_list.append(new_stu)

    def show_all_stu(self):
        """查询所有学生的数据"""
        # print('查询所有学生的数据')
        print('序号\t\t姓名\t\t年龄\t\t电话')

        # 遍历 stu_list 列表，获取每个元素(对象)，打印显示每个学生的信息
        for i, stu in enumerate(self.stu_list):
            # i：下标
            # stu：元素（学生对象）
            print(f'{i+1}\t\t{stu.name}\t\t{stu.age}\t\t{stu.tel}')

    def show_one_stu(self):
        """查询某个学生的数据"""
        # ① 提示用户输入要查询的学生名称
        _name = input('请输入学生的姓名：')

        # ② 遍历 stu_list，获取其中的每个元素（对象），从字典中获取学生的姓名，和查询学生姓名进行比对
        for i, stu in enumerate(self.stu_list):
            # i：下标
            # stu：学生对象
            if stu.name == _name:
                # 如果存在相等，则打印显示出对应学生的信息
                print('序号\t\t姓名\t\t年龄\t\t电话')
                print(f'{i+1}\t\t{stu.name}\t\t{stu.age}\t\t{stu.tel}')
                # 结束 for 循环
                break
        else:
            # 只要 for 循环的 else 里面的代码执行了，就说明没有查询到学生
            # 如果不存在相等，则提示：查无此人！该学生不存在！
            print(f'查无此人！该学生{_name}不存在！')

    def update_one_stu(self):
        """修改某个学生的数据"""
        # print('修改某个学生的数据')
        # ① 提示用户输入要修改的学生姓名
        _name = input('请输入学生的姓名：')

        # ② 根据用户的输入，判断要修改的学生是否存在
        for stu in self.stu_list:
            # stu：学生对象
            if stu.name == _name:
                # 如果学生存在，则提示输入修改之后的姓名、年龄、电话，然后进行数据的修改保存
                new_name = input('请输入修改之后的学生姓名：')
                new_age = int(input('请输入修改之后的学生年龄：'))
                new_tel = input('请输入修改之后的学生电话：')

                # 进行数据的修改保存
                # 学生对象.属性名 = 值
                stu.name = new_name
                stu.age = new_age
                stu.tel = new_tel
                # 结束 for 循环
                break
        else:
            # 如果学生不存在，则最终提示：查无此人！该学生不存在！
            print(f'查无此人！该学生{_name}不存在！')

    def delete_one_stu(self):
        """删除某个学生的数据"""
        # print('删除某个学生的数据')
        # ① 提示用户输入要删除的学生姓名
        _name = input('请输入学生的姓名：')

        # ② 遍历查询要删除的学生，看学生是否存在
        for i, stu in enumerate(self.stu_list):
            # i：下标
            # stu：元素(对象)
            if stu.name == _name:
                # 如果学生存在，则将学生的数据从列表中删除
                del self.stu_list[i]
                # self.stu_list.remove(stu_dict)
                print('学生数据删除成功！')
                # 结束 for 循环
                break
        else:
            # 如果学生不存在，最终提示：操作失败！该学生不存在！
            print(f'操作失败！该学生{_name}不存在！')

    def save_data(self):
        """将学生的数据保存到文件中"""
        # print('将学生的数据保存到文件中')
        # ① 从 stu_list 列表中获取每个学生的对象，将学生的数据再保存一个字典
        temp_list = []
        for stu in self.stu_list:
            # stu：学生对象
            stu_dict = {'name': stu.name, 'age': stu.age, 'tel': stu.tel}
            temp_list.append(stu_dict)

        # ② 将 temp_list 转换为一个字符串，写入到文件
        with open('./stu.txt', 'w', encoding='utf8') as f:
            content = str(temp_list)
            f.write(content)

    def load_data(self):
        """从文件中读取学生的数据"""
        # print('从文件中读取学生的数据')
        # 判断 stu.txt 文件是否存在
        # not False -> True
        # 快速导入快捷：alt + enter
        if not os.path.isfile('./stu.txt'):
            print('stu.txt文件不存在')
            return

        # 从 stu.txt 文件中读取所有学生的数据
        with open('./stu.txt', 'r', encoding='utf8') as f:
            content = f.read() # str
            temp_list = eval(content) # temp_list：是一个列表套字典

        # 遍历 temp_list 中的每个字典，把每个字典学生数据再保存成一个对象
        for stu_dict in temp_list:
            # {'name': 'smart', 'age': 18, 'tel': '138'}
            _name = stu_dict['name']
            _age = stu_dict['age']
            _tel = stu_dict['tel']
            stu = Student(_name, _age, _tel)
            self.stu_list.append(stu)

    def start(self):
        """管理系统的主逻辑方法（框架代码）"""
        # 首先从文件中加载保存的学生的数据
        self.load_data()

        while True:
            print(self.stu_list)
            # 显示功能菜单
            SysManager.show_menu()
            # 提示用户输入功能数字
            cmd_num = input('请输入功能数字：')
            # 根据用户的输入，判断要进行什么操作
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


# 创建一个 SysManager 对象
manager = SysManager()

# 首先创建两个学生对象，添加到 manager 对象的 stu_list 属性中，表示已经存在两个学生了
# stu1 = Student('smart', 18, '138')
# stu2 = Student('linda', 16, '135')
# manager.stu_list.append(stu1)
# manager.stu_list.append(stu2)

manager.start()




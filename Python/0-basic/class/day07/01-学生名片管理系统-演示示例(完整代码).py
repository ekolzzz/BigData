"""
数据存储分析：
1）如何存储一个学生的数据？字典
    学生1：{'name': 'smart', 'age': 18, 'tel': '131'}
    学生2：{'name': 'linda', 'age': 16, 'tel': '133'}
2）如果存储多个学生的数据？列表套字典
    [{'name': 'smart', 'age': 18, 'tel': '131'},
    {'name': 'linda', 'age': 16, 'tel': '133'}]

业务功能分析：
1）提示功能菜单，接收输入
2）添加学生
3）查询所有学生
4）查询某个学生
5）修改某个学生
6）删除某个学生
7）退出系统
"""

# 保存学生数据
user_list = [{'name': 'smart', 'age': 18, 'tel': '131'},
             {'name': 'linda', 'age': 16, 'tel': '133'}]


def show_menu():
    """
    显示功能菜单
    """
    print('= 1. 添加学生')
    print('= 2. 查询所有学生')
    print('= 3. 查询某个学生')
    print('= 4. 修改某个学生')
    print('= 5. 删除某个学生')
    print('= 6. 退出系统')


def add_stu_info():
    """
    添加学生
    """
    # 1. 提示用户输入学生姓名、年龄、电话
    name = input('请输入学生姓名：')
    age = int(input('请输入学生年龄：'))
    tel = input('请输入学生电话：')

    # 2. 根据姓名判断用户是否存在，如果存在，则提示学生已存在，否则添加学生信息
    for user_dict in user_list:
        if user_dict['name'] == name:
            print('该学生已存在！不能重复添加！')
            break
    else:
        # 学生不存在，将学生的信息组装成字典数据
        user_dict = {'name': name, 'age': age, 'tel': tel}

        # 将学生信息添加到列表中
        user_list.append(user_dict)


def show_all_stu():
    """
    显示所有学生信息
    """
    print('序号\t\t姓名\t\t年龄\t\t电话')

    for i, user_dict in enumerate(user_list):
        print(f"{i}\t\t{user_dict['name']}\t\t{user_dict['age']}\t\t{user_dict['tel']}")


def show_one_stu():
    """
    显示单个学生信息
    """
    # 1. 提示输入要查询的学生姓名
    name = input('请输入学生姓名：')

    # 2. 查询指定的学生信息并显示
    for i, user_dict in enumerate(user_list):
        if user_dict['name'] == name:
            print('序号\t\t姓名\t\t年龄\t\t电话')
            print(f"{i}\t\t{user_dict['name']}\t\t{user_dict['age']}\t\t{user_dict['tel']}")
            break
    else:
        print('查无此人，没有学生信息！')


def update_one_stu():
    """
    修改指定学生数据
    """
    # 1. 提示输入要修改的学生姓名
    name = input('请输入学生姓名：')

    # 2. 根据姓名查询对应的学生信息，若存在，则提示输入修改的信息并进行修改，否则提示没有改学生
    for user_dict in user_list:
        if user_dict['name'] == name:
            # 查询到学生
            # 则提示输入修改的信息并进行修改
            _name = input('请输入修改之后的学生姓名：')
            _age = input('请输入修改之后的学生年龄：')
            _tel = input('请输入修改之后的学生电话：')

            user_dict['name'] = _name
            user_dict['age'] = _age
            user_dict['tel'] = _tel

            break
    else:
        # 没有查到该学生
        print('查无此人！没有该学生信息！')


def delete_one_stu():
    """
    删除指定学生数据
    """
    # 1. 提示用户输入要删除的学生姓名
    name = input('请输入学生姓名：')

    # 2. 根据输入的姓名查询指定的学生，若存在，则删除数据，否则提示学生不存在
    for i, user_dict in enumerate(user_list):
        if user_dict['name'] == name:
            del user_list[i]
            print('删除学生信息成功！')
            break
    else:
        print('操作失败！该学生不存在！')


def main():
    """
    主函数
    """
    while True:
        print(user_list)

        # 1. 显示功能菜单
        show_menu()

        # 2. 接收用户输入
        cmd_num = input('请输入功能数字：')

        # 3. 根据用户的输入执行相应的操作
        if cmd_num == '1':
            add_stu_info()
        elif cmd_num == '2':
            show_all_stu()
        elif cmd_num == '3':
            show_one_stu()
        elif cmd_num == '4':
            update_one_stu()
        elif cmd_num == '5':
            delete_one_stu()
        elif cmd_num == '6':
            print('退出系统')
            break
        else:
            print('输入有误！请重新输入！')


# 调用主函数
main()


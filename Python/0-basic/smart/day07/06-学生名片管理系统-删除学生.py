"""
数据存储的分析：
1）如何保存一个学生的信息(姓名、年龄、电话)？字典
    学生1：{'name': 'smart', 'age': 18, 'tel': '135'}
    学生2：{'name': 'linda', 'age': 16, 'tel': '138'}

2）如何保存多个学生的信息？列表套字典
    [{'name': 'smart', 'age': 18, 'tel': '135'}, {'name': 'linda', 'age': 16, 'tel': '138'}, ...]

案例功能分析：
1）添加学生
2）查询所有学生
3）查询某个学生
4）修改某个学生
5）删除某个学生
6）退出系统
"""
# 首先定义一个列表，假设已经存在两个学生了
stu_list = [{'name': 'smart', 'age': 18, 'tel': '135'},
            {'name': 'linda', 'age': 16, 'tel': '138'}]


# 定义一个函数：show_menu，功能就是显示功能菜单
def show_menu():
    """显示功能菜单"""
    print('= 1. 添加学生')
    print('= 2. 查询所有学生')
    print('= 3. 查询某个学生')
    print('= 4. 修改某个学生')
    print('= 5. 删除某个学生')
    print('= 6. 退出系统')


# 定义一个函数：add_stu_info，功能就是添加一个学生数据
def add_stu_info():
    """添加一个学生数据"""
    # ① 提示用户输入添加的学生姓名
    _name = input('请输入学生的姓名：')

    # ② 判断添加的学生姓名和已经存在的学生姓名是否存在相同
    # 遍历 stu_list，获取其中的每个元素(字典)，然后从字典中获取学生的姓名，和添加的学生姓名进行比较
    for stu_dict in stu_list:
        if stu_dict['name'] == _name:
            # 如果存在相同，则提示：该学生已存在！不允许重复添加！
            print(f'该学生{_name}已存在！不允许重复添加！')
            break
    else:
        # 只要 for 循环的 else 代码执行了，就说明不存在同名的学生
        # 如果不存在相同，则提示继续输入添加学生的年龄和电话，然后保存添加学生的数据
        _age = int(input('请输入学生的年龄：'))
        _tel = input('请输入学生的电话：')

        # 将添加学生的数据保存成一个字典
        new_stu = {'name': _name, 'age': _age, 'tel': _tel}

        # 然后将字典添加到 stu_list 列表中
        stu_list.append(new_stu)


# 定义一个函数：show_all_stu，功能就是显示所有学生的数据
def show_all_stu():
    """显示所有学生的数据"""
    print('序号\t\t姓名\t\t年龄\t\t电话')
    # 遍历 stu_list，获取每个学生的数据（姓名、年龄、电话），然后 print 打印显示
    for i, stu_dict in enumerate(stu_list):
        # i：数据的下标
        # stu_dict：遍历的每个数据（字典）
        # name = stu_dict['name']
        # age = stu_dict['age']
        # tel = stu_dict['tel']
        # print(f'{i}\t\t{name}\t\t{age}\t\t{tel}')

        print(f"{i}\t\t{stu_dict['name']}\t\t{stu_dict['age']}\t\t{stu_dict['tel']}")


# 定义一个函数：show_one_stu，功能就是查询某个学生的数据并显示
def show_one_stu():
    """查询某个学生的数据并显示"""
    # 提示用户输入要查询的学生姓名
    _name = input('请输入学生的姓名：')

    # 根据输入的姓名，查询学生是否存在
    # 遍历 stu_list，获取其中的每个元素（字典），然后取出学生的姓名和查询的学生姓名进行比较
    for i, stu_dict in enumerate(stu_list):
        # i：下标
        # stu_dict：遍历的数据（字典）
        if stu_dict['name'] == _name:
            # 如果学生存在，则显示对应学生的信息
            print('序号\t\t姓名\t\t年龄\t\t电话')
            print(f"{i}\t\t{stu_dict['name']}\t\t{stu_dict['age']}\t\t{stu_dict['tel']}")
            break
    else:
        # 如果学生不存在，则提示：查无此人！该学生不存在！
        print(f'查无此人！该学生{_name}不存在！')


# 定义一个函数：update_one_stu，功能就是修改某个学生的数据
def update_one_stu():
    """修改某个学生的数据"""
    # 提示用户输入要修改的学生姓名
    _name = input('请输入学生的姓名：')

    # 根据输入的姓名，查询要修改的这个学生
    # 遍历 stu_list，获取其中的每个元素（字典），然后从字典中获取学生的姓名，和输入的姓名进行比较
    for stu_dict in stu_list:
        if stu_dict['name'] == _name:
            # 如果学生存在，则提示输入修改之后的姓名、年龄、电话，然后进行修改数据的保存
            new_name = input('请输入修改之后的姓名：')
            new_age = int(input('请输入修改之后的年龄：'))
            new_tel = input('请输入修改之后的电话：')

            # 进行数据的修改（其实就是修改字典中键对应的值）
            stu_dict['name'] = new_name
            stu_dict['age'] = new_age
            stu_dict['tel'] = new_tel
            break
    else:
        # 如果学生不存在，则提示：查无此人！该学生不存在！
        print(f'查无此人！该学生{_name}不存在！')


# 定义一个函数：delete_one_stu，功能就是删除某个学生的数据
def delete_one_stu():
    """删除某个学生的数据"""
    # 提示用户输入要删除的学生姓名
    _name = input('请输入学生的姓名：')

    # 根据输入的姓名，查询对应的学生
    # 遍历 stu_list，获取其中的每个元素（字典），然后从字典中获取学生的姓名，和输入的姓名进行比较
    for i, stu_dict in enumerate(stu_list):
        if stu_dict['name'] == _name:
            # 如果学生存在，则将学生的数据删除
            # stu_list.remove(stu_dict)
            del stu_list[i]
            print('学生删除成功！')
            break
    else:
        # 如果学生不存在，则提示：操作失败！该学生不存在！
        print(f'操作失败！该学生{_name}不存在！')


# 实现案例的整体的框架代码
def main():
    """学生名片管理系统的主逻辑代码"""
    while True:
        print(stu_list)
        # ① 显示功能菜单
        show_menu()

        # ② 提示用户输入要进行的操作
        cmd_num = input('请输入要进行的操作：')

        # ③ 判断用户的输入，来执行对应的操作
        if cmd_num == '1':
            # print('添加学生')
            add_stu_info()
        elif cmd_num == '2':
            # print('查询所有学生')
            show_all_stu()
        elif cmd_num == '3':
            # print('查询某个学生')
            show_one_stu()
        elif cmd_num == '4':
            # print('修改某个学生')
            update_one_stu()
        elif cmd_num == '5':
            # print('删除某个学生')
            delete_one_stu()
        elif cmd_num == '6':
            print('退出系统')
            break
        else:
            print('输入有误！请重新输入！')


# 调用 main 函数启动程序
main()
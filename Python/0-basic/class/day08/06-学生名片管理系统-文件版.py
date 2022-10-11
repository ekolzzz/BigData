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

# 需求：编程代码，实现案例的整体的框架
# 先定义一个列表，假设已经存在两个学生了
stu_list = [{'name': 'smart', 'age': 18, 'tel': '135'},
            {'name': 'linda', 'age': 16, 'tel': '138'}]


# 需求：定义一个函数 show_menu，来打印功能菜单
def show_menu():
    """打印功能菜单"""
    print('= 1. 添加学生')
    print('= 2. 查询所有学生')
    print('= 3. 查询某个学生')
    print('= 4. 修改某个学生')
    print('= 5. 删除某个学生')
    print('= 6. 退出系统')


# 需求：定义一个函数 add_stu_info，负责学生数据的添加
def add_stu_info():
    """学生数据的添加"""
    # print('添加学生')
    # ① 提示用户输入要添加的学生姓名
    _name = input('请输入学生姓名：')

    # ② 判断新添加的学生姓名和已经存在的学生是否存在同名
    # 思路：遍历 stu_list 中每个元素(字典)，从字典中获取学生的姓名，然后和新添加的学生姓名进行比较
    for stu_dict in stu_list:
        if stu_dict['name'] == _name:
            # 如果存在同名，则提示：该学生已存在！不允许重复添加！
            print(f'该学生{_name}已存在！不允许重复添加！')
            # 结束 for 循环
            break
    else:
        # 只要 for 循环的 else 里面的代码执行了，就说明不存在同名学生！
        # 如果不存在同名，则提示用户输入要添加的学生的年龄和电话，然后进行添加学生数据的保存
        _age = int(input('请输入学生的年龄：'))
        _tel = input('请输入学生的电话：')

        # 将新添加的学生的数据保存为一个字典
        new_stu = {'name': _name, 'age': _age, 'tel': _tel}

        # 将字典添加到 stu_list 这个列表中
        stu_list.append(new_stu)


# 需求：定义一个函数 show_all_stu，负责显示所有学生的数据
def show_all_stu():
    """显示所有学生的数据"""
    # print('显示所有学生的数据')
    print('序号\t\t姓名\t\t年龄\t\t电话')

    # 遍历 stu_list 列表，获取每个元素(字典)，打印显示每个学生的信息
    for i, stu_dict in enumerate(stu_list):
        # i：下标
        # stu_dict：元素
        print(f'{i}\t\t{stu_dict["name"]}\t\t{stu_dict["age"]}\t\t{stu_dict["tel"]}')


# 需求：定义一个函数 show_one_stu，负责显示查询某个学生的数据
def show_one_stu():
    """查询某个学生"""
    # print('查询某个学生')
    # ① 提示用户输入要查询的学生名称
    _name = input('请输入学生的姓名：')

    # ② 遍历 stu_list，获取其中的每个元素（字典），从字典中获取学生的姓名，和查询学生姓名进行比对
    for i, stu_dict in enumerate(stu_list):
        # i：下标
        # stu_dict：字典
        if stu_dict['name'] == _name:
            # 如果存在相等，则打印显示出对应学生的信息
            print('序号\t\t姓名\t\t年龄\t\t电话')
            print(f'{i}\t\t{stu_dict["name"]}\t\t{stu_dict["age"]}\t\t{stu_dict["tel"]}')
            # 结束 for 循环
            break
    else:
        # 只要 for 循环的 else 里面的代码执行了，就说明没有查询到学生
        # 如果不存在相等，则提示：查无此人！该学生不存在！
        print(f'查无此人！该学生{_name}不存在！')


# 需求：定义一个函数 update_one_stu，负责指定某个学生数据的修改
def update_one_stu():
    """修改指定的某个学生"""
    # ① 提示用户输入要修改的学生姓名
    _name = input('请输入学生的姓名：')

    # ② 根据用户的输入，判断要修改的学生是否存在
    for stu_dict in stu_list:
        if stu_dict['name'] == _name:
            # 如果学生存在，则提示输入修改之后的姓名、年龄、电话，然后进行数据的修改保存
            new_name = input('请输入修改之后的学生姓名：')
            new_age = int(input('请输入修改之后的学生年龄：'))
            new_tel = input('请输入修改之后的学生电话：')

            # 进行数据的修改保存
            stu_dict['name'] = new_name
            stu_dict['age'] = new_age
            stu_dict['tel'] = new_tel
            # 结束 for 循环
            break
    else:
        # 如果学生不存在，则最终提示：查无此人！该学生不存在！
        print(f'查无此人！该学生{_name}不存在！')


# 需求：定义一个函数 delete_one_stu，负责指定某个学生数据的删除
def delete_one_stu():
    """删除某个学生数据"""
    # ① 提示用户输入要删除的学生姓名
    _name = input('请输入学生的姓名：')

    # ② 遍历查询要删除的学生，看学生是否存在
    for i, stu_dict in enumerate(stu_list):
        # i：下标
        # stu_dict：元素(字典)
        if stu_dict['name'] == _name:
            # 如果学生存在，则将学生的数据从列表中删除
            del stu_list[i]
            # stu_list.remove(stu_dict)
            print('学生数据删除成功！')
            # 结束 for 循环
            break
    else:
        # 如果学生不存在，最终提示：操作失败！该学生不存在！
        print(f'操作失败！该学生{_name}不存在！')


# 需求：定义一个函数 main，来实现学生名称管理系统的整体框架代码
def main():
    """学生名称管理系统的整体框架代码"""
    while True:
        print(stu_list)
        # 首先打印显示功能菜单
        show_menu()

        # 提示用户输入功能数字
        cmd_num = input('请输入功能数字：') # str

        # 判断用户输入的数字，执行对应的操作
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
            # 结束循环
            break
        else:
            print('输入有误！请重新输入！')


# 调用 main 函数
main()
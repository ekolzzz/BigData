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
            print('查询所有学生')
        elif cmd_num == '3':
            print('查询某个学生')
        elif cmd_num == '4':
            print('修改某个学生')
        elif cmd_num == '5':
            print('删除某个学生')
        elif cmd_num == '6':
            print('退出系统')
            break
        else:
            print('输入有误！请重新输入！')


# 调用 main 函数启动程序
main()
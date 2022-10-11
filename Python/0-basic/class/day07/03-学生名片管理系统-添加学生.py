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


# 需求：定义一个函数：show_menu，功能就是打印显示菜单
def show_menu():
    """打印显示菜单"""
    print('= 1. 添加学生')
    print('= 2. 查询所有学生')
    print('= 3. 查询某个学生')
    print('= 4. 修改某个学生')
    print('= 5. 删除某个学生')
    print('= 6. 退出系统')


# 需求：定一个函数：main，功能就是学生名片管理系统的框架逻辑
def main():
    """学生名片管理系统的主逻辑"""
    while True:
        # ① 首先给用户显示功能菜单
        show_menu()

        # ② 提示用户输入要进行的操作
        cmd_num = input('请输入功能数字：') # str

        # ③ 根据用户输入的数字，判断要进行什么操作
        if cmd_num == '1':
            print('添加学生')
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


# 调用 main 函数
main()

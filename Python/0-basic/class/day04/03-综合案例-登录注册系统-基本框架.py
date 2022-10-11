"""
登录注册系统
"""
"""
数据存储的分析：
1）如何保存单个注册用户的信息？
user1 = {'name': 'smart', 'pwd': '123456abc'}
user2 = {'name': 'linda', 'pwd': '123*abc'}

2）如果保存多个注册用户的信息？
user_list = [{'name': 'smart', 'pwd': '123456abc'}, {'name': 'linda', 'pwd': '123*abc'}]

案例功能的分析：
"""
# 先定义出一个嵌套字典的列表
user_list = [{'name': 'smart', 'pwd': '123456abc'}, {'name': 'linda', 'pwd': '123*abc'}]
#
# for user_dict in user_list :
#     print(user_dict['name'])

while True :
    print(user_list)
    cmd_num = input('请输入操作:1.用户注册/ 2.用户登录/ 3.忘记密码/ 4.退出程序 :') # 获取的数据类型为 str
    if cmd_num == '1' :
        new_name = input('请输入用户名：')

        # 判断新输入的用户名是否已存在嵌套字典的列表中
        for user_dict in user_list : # for循环遍历user_list列表中的每个元素，并将元素赋值给user_dict
            # 判断新用户名是否和字典user_dict中'name'键的值相等
            if user_dict['name'] == new_name :
                print('用户名已存在，请重新输入！')
                break # 如果用户名已存在，则跳出for循环

        # for循环会遍历所有数据，如果没有找到相同的用户名，则会执行else中的语句
        else: # 当循环中没有遇到break，循环结束时会执行else部分的代码
            new_pwd = input('请输入密码：')
            # 将新用户的用户名和密码存到user_dict里
            user_dict = {'name': new_name, 'pwd': new_pwd} # 定义字典user_dict
            # user_list列表里添加字典
            user_list.append(user_dict) # 在末尾追加值if cmd_num == '1' :

    elif cmd_num == '2' :
        login_name = input('请输入用户名：')
        login_pwd = input('请输入登录密码：')

        # 判断新输入的用户名是否已存在嵌套字典的列表中
        for user_dict in user_list : # for循环遍历user_list列表中的每个元素，并将元素赋值给user_dict
            # 判断新用户名是否和字典user_dict中'name'键的值相等
            if user_dict['name'] == login_name and user_dict['pwd'] == login_pwd :
                print('登录成功！')
                break # 如果用户名已存在，则跳出for循环

        # for循环会遍历所有数据，如果没有找到相同的用户名，则会执行else中的语句
        else: # 当循环中没有遇到break，循环结束时会执行else部分的代码
            print('用户名或者密码错误，请重新输入!')
    # 忘记密码，
    # 1. 输入忘记密码的用户名，如果存在则让用户输入要修改的密码
    # 2. 如果用户名不存在则输出用户名不存在
    elif cmd_num == '3' :
        _name = input('请输入用户名：')

        for user_dict in user_list : # for循环遍历user_list列表中的每个元素，并将元素赋值给user_dict
            if user_dict['name'] == _name:
                _pwd = input('请输入新密码：')
                user_dict['pwd'] = _pwd
                break
        else:
            print('用户名不存在')
            break

    elif cmd_num == '4' :
        print('退出程序')
        break

    else:
        print('输入错误，请重新输入')
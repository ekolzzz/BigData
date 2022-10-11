# """
# 字典定义格式：
#     字典变量 = {k1:v1, k2:v2,……}
#
# 取出元素的值：
#     字典变量[键值]
# """
# # 字典的定义
# info = {'name': 'mike', 'age': 34, 'city': 'sz'}
# print(info)  # {'name': 'mike', 'age': 34, 'city': 'sz'}
#
# # 取出元素的值：字典变量[键值]
# print(info['city'])

# 0. 定义一个列表，用于存储用户字典
user_list = [{'name': 'mike', 'pwd': '123456'}, {'name': 'yoyo', 'pwd': '123456'}]

# 1. 死循环 while True:
while True:
    #  2. 输入数字指令
    cmd_num = input('请输入操作: 1.用户注册/ 2.用户登录/ 3.退出程序')

    # 3. 判断指令，选择分支
    # 4. 用户注册功能
    if cmd_num == '1':
        # print('用户注册')
        # 4.1 输入注册的用户名
        reg_name = input('请输入注册的名字：')
        # 4.2 通过for遍历列表，取出的每个元素是字典
        for user_dict in user_list:
            # 4.3 字典['name']和输入注册的用户名比较是否相等
            if user_dict['name'] == reg_name:
                # 4.4 如果相等，打印提示：名字在列表中，不允许注册
                print(reg_name, '名字在列表中，不允许注册')
                # 4.5 跳出循环
                break
        # 4.6 for循环的else，循环里面没有执行到break，则会执行else
        else:
            # 4.7 输入注册的密码
            reg_pwd = input('请输入注册的密码：')
            # 4.8 创建一个字典
            user_dict = {'name': reg_name, 'pwd': reg_pwd}
            # 4.9 字典追加到列表中
            user_list.append(user_dict)
            # 4.10 打印：注册成功
            print('注册成功')
    # 5. 用户登陆功能
    elif cmd_num == '2':
        # print('用户登录')
        # 5.1 输入登陆的用户名和密码
        login_name = input('请输入登录用户名:')
        login_pwd = input('请输入登录密码:')
        # 5.2 通过for遍历列表，取出的每个元素是字典
        for user_dict in user_list:
            # 5.3 字典['name']和登陆用户名比较 and 字典['pwd']和登陆密码比较
            if user_dict['name'] == login_name and user_dict['pwd'] == login_pwd:
                # 5.4 如果都相等，打印提示：登陆成功
                print('登陆成功')
                # 5.5 跳出循环
                break
        # 5.6 for循环的else，循环里面没有执行到break，则会执行else
        else:
            # 5.7 打印：用户名或密码错误，请重新登陆
            print('用户名或密码错误，请重新登陆')
    elif cmd_num == '3':
        print('退出程序')
        break
    else:
        print("输入错误，重新输入")
"""
登录注册系统
"""
"""
数据存储的分析：
1）如何保存单个注册用户的信息？字典
    用户1：{'name': 'smart', 'pwd': '123456abc'}
    用户2：{'name': 'linda', 'pwd': '123*abc'}

2）如果保存多个注册用户的信息？列表套字典（列表中的每个元素都是一个字典）
    [{'name': 'smart', 'pwd': '123456abc'}, {'name': 'linda', 'pwd': '123*abc'}, ...]

案例功能的分析：
1）用户注册
2）用户登录
3）退出程序
"""
# 先定义一个列表套字典的结构，假设已经有两个注册用户了
user_list = [{'name': 'smart', 'pwd': '123456abc'}, {'name': 'linda', 'pwd': '123*abc'}]

# 需求：遍历打印每个注册用户的用户名，该怎么办？
# 思路：先遍历 user_list，获取其中的每个元素（字典），然后从字典中根据 key 获取对应的 value
# for user_dict in user_list:
#     # print(type(user_dict), user_dict)
#     print(user_dict['name'])

# 登录注册案例基本框架代码实现
while True:
    # 每次循环开始，打印一下 user_list，方便查看其中数据的变化
    print(user_list)
    # ① 提示用户输入要进行的操作
    cmd_num = input('请输入操作: 1.用户注册/ 2.用户登录/ 3.退出程序：') # str

    # ② 根据用户的输入，判断用户要进行什么操作
    if cmd_num == '1':
        # print('用户注册')
        # 基本用户注册的代码逻辑
        # # ① 提示用户输入注册的用户名和密码
        # _name = input('请输入注册的用户名：')
        # _pwd = input('请输入注册的密码：')
        #
        # # ② 保存注册用户的信息（先将注册的用户名和密码保存成一个字典，再将字典添加到列表中）
        # user_dict = {'name': _name, 'pwd': _pwd}
        # user_list.append(user_dict)

        # 解决用户名注册不能重复的问题
        # ① 提示用户输入注册的用户名
        _name = input('请输入注册的用户名：')

        # ② 判断注册的用户名和已经注册的用户名是否存在相同的
        # 遍历 user_list，获取其中的每个元素（字典），然后从字典中获取注册的用户名，和新注册的用户名进行比对
        for user_dict in user_list:
            if user_dict['name'] == _name:
                # 如果存在相同的用户名，则提示：用户已存在！不允许重复注册！
                print('用户已存在！不允许重复注册！')
                # 如果存在相同用户名，则 for 循环不需要继续，结束 for 循环
                break
        else:
            # 只要 for 循环的 else 代码执行了，就说明不存在相同的用户名
            # 如果不存在相同的用户名，再提示用户输入注册的密码，然后保存注册用户的信息（先将注册的用户名和密码保存成一个字典，再将字典添加到列表中）
            _pwd = input('请输入注册的密码：')

            new_user = {'name': _name, 'pwd': _pwd}
            user_list.append(new_user)
    elif cmd_num == '2':
        print('用户登录')
    elif cmd_num == '3':
        print('退出程序')
        # 终止循环
        break
    else:
        print('输入有误！请重新输入！')
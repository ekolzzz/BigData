"""
假设有一个文件 register.txt，里面保存了注册用户的用户名和密码，信息如下：

smart,123456abc
linda,123*abc
david,123#abc


编写一个python程序，从上面的文件中读取注册用户的信息，并存储成python中的列表套字典的格式：
[
    {"name": "smart", "pwd": "123456abc"},
    {"name": "linda", "pwd": "123*abc"},
    {"name": "david", "pwd": "123#abc"}
]
"""

# 定义一个空列表
result_list = []

# 读取文件中的内容，并进行处理
with open('./register.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    # print(lines)

    # 遍历文件中的每一行数据
    for line in lines:
        # 去掉每一行的 \n
        line = line.strip('\n')
        # 对每一行的数据使用,进行分割
        result = line.split(',')
        # 将每一行的用户名和密码保存成一个字典
        user = {'name': result[0], 'pwd': result[1]}
        # 将字典添加到列表中
        result_list.append(user)

    print(result_list)
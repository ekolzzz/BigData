# smart,123456abc
# linda,123*abc
# david,123#abc

# with open ('register.txt', 'w') as f:
#     f.write('smart,123456abc\n')
#     f.write('linda,123*abc\n')
#     f.write('david,123#abc\n')
"""
[
    {"name": "smart", "pwd": "123456abc"},
    {"name": "linda", "pwd": "123*abc"},
    {"name": "david", "pwd": "123#abc"}
]
"""
# 定义一个空列表
user_list = []

# 读取register.txt
with open ('register.txt', 'r', encoding= 'utf8') as f:
    lines = f.readlines()
    # print(type(lines), lines)
    #lines = ['smart,123456abc\n', 'linda,123*abc\n', 'david,123#abc\n']

    # 遍历列表lines里的每一个元素
    for line in lines:
        # 字符串.strip(目标字符串): 返回新字符串，去除 字符串 左右两边的目标字符串, 不设置目标字符串则去除空格
        line = line.strip('\n')
        # print(type(line), line)

        # 字符串.split(分割符): 以分割符拆分字符串, 返回列表
        user = line.split(',')
        # print(type(user), user)

        user_dict = {'name': user[0], 'pwd': user[1]}
        # print(type(user_dict), user_dict)

        # 将字典添加到列表中
        user_list.append(user_dict)
        # print(user_list)

    print(user_list)



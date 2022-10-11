"""
假设有一个 python 字典如下：

user_dict = {'name': 'smart', 'age': 18, 'tel': '13888888888'}

编写一个 python 程序，将字典的数据写入一个 user.txt 文件中，写入格式如下：
name: smart
age: 18
tel: 13888888888
"""

user_dict = {'name': 'smart', 'age': 18, 'tel': '13888888888'}

with open('./user.txt', 'w', encoding='utf8') as f:
    # 遍历字典的 key 和 value
    for key, value in user_dict.items():
        # 生成一个字符串
        content = f'{key}: {value}\n'
        # 写入到文件中
        f.write(content)
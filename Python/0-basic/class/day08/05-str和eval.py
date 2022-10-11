"""
str和eval
学习目标：常握 str 和 eval 两个函数的用法
"""

"""
str函数：将传入的数据转换为字符串类型，如果传入容器类型数据，则将容器数据转换为字符串
"""
user_list = [{'name': 'mike', 'age': 34, 'tel': 110},
             {'name': 'yoyo', 'age': 30, 'tel': 120}]

print(type(user_list), user_list)


"""
eval函数：返回传入字符串内容的结果，字符串里面看到像是什么，就转换成什么
"""
# my_str = "[{'name': 'mike', 'age': 34, 'tel': 110}, {'name': 'yoyo', 'age': 30, 'tel': 120}]"

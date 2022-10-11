"""
enumerate：通过 for 配合 enumerate 遍历容器同时获取元素索引位置(下标)、元素
"""

user_list = [{'name': 'mike', 'age': 34, 'tel': '110'},
             {'name': 'yoyo', 'age': 18, 'tel': '120'}]

"""
需求：遍历 user_list 数据时，同时打印出每个元素及元素的下标
"""
for user in user_list:
    print(type(user), user)

for i, user in enumerate(user_list):
    # i：元素的下标
    # user：元素
    print(i, user)


"""
del：通过del根据下标删除列表元素
格式：del 列表[索引]
"""

user_list = [{'name': 'mike', 'age': 34, 'tel': '110'},
             {'name': 'yoyo', 'age': 18, 'tel': '120'}]

# 需求：将 user_list 中下标为 0 的数据删除
# del user_list[0]
# print(user_list)

# # del 变量名：表示把这个变量销毁，后面不能再使用销毁的变量了
# del user_list
# # NameError: name 'user_list' is not defined
# print(user_list)

res = user_list.pop(0)
print(res)
print(user_list)
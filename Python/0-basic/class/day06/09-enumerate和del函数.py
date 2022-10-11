"""
enumerate：通过 for 配合 enumerate 遍历容器同时获取元素索引位置(下标)、元素
"""

user_list = [{'name': 'mike', 'age': 34, 'tel': '110'},
             {'name': 'yoyo', 'age': 18, 'tel': '120'}]

"""
需求：遍历 user_list 数据时，同时打印出每个元素及元素的下标
"""
i = 0
for user_dict in user_list:
    print(i, user_dict)
    i += 1

print('=='*20)

for i, user_dict in enumerate(user_list):
    print(i, user_dict)


"""
del：通过del根据下标删除列表元素
格式：del 列表[索引]
"""

user_list = [{'name': 'mike', 'age': 34, 'tel': '110'},
             {'name': 'yoyo', 'age': 18, 'tel': '120'}]


del user_list[0]
print(user_list)

print('=='*20)

user_list = [{'name': 'mike', 'age': 34, 'tel': '110'},
             {'name': 'yoyo', 'age': 18, 'tel': '120'}]

ret = user_list.pop(1) # pop可以返回被删除的数据
print('被删除的列表元素是：', ret)
print('=='*20)
print(user_list)
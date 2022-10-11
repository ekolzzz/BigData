"""
遍历：从前到后依次取出列表中的每个元素
"""


# 需求：遍历打印name_list中的每个元素

"""
while循环实现
"""

# name_list = ['smart', 'yoyo', 'rock', 'lily']
#
# # print(name_list[0])
# # print(name_list[1])
# # print(name_list[2])
# # print(name_list[3])
#
# i = 0
#
# while i < len(name_list):
#     print(name_list[i])
#     i += 1


"""
for循环实现：依次从列表中取出每个元素，赋值给前面的变量
语法：
    for 变量 in 列表(可迭代数据):
        ...
"""

name_list = ['smart', 'yoyo', 'rock', 'lily', 'jack']

for i in name_list:
    print(i)

# 注意区分
# 1）if 变量名 in 列表：判断变量的值是否在列表中，存在为True，不存在为False
# 2）for 变量名 in 列表：对列表中的数据进行遍历，从列表中依次取出每个元素，赋值给前面的变量

# name = 'yoyo'
#
# if name in name_list:
#     print('%s在列表中' % name)
# else:
#     print('%s不在列表中' % name)


"""
for循环中的else: 和while的else一样，当循环中没有遇到break，循环结束时会执行else部分的代码
"""

name_list = ['smart', 'yoyo', 'rock', 'lily']

for name in name_list:
    print(name)

    if name == 'yoyo':
        # 终止循环
        break
else:
    print('for循环的else部分的代码')

print('for循环结束')

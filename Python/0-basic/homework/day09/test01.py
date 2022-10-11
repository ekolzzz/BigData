# import keyword
#
# print(keyword.kwlist)

# sum = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         sum += i
# print(sum)

# list = []
#
# for i in range(1, 101):
#     if i % 2 == 0 :
#         list.append(i)
# print(list)
# print(sum(list))

# my_str = "abc"
#
# new_str = my_str[::-1]
# print(new_str)

# my_str = "abc"
# str_list = list(my_str)
# print(str_list)
# # 把列表中元素翻转
# str_list.reverse()
# print(str_list)
# # 将列表中的字符串连接到一起
# result = ''.join(str_list) # # my_str = "abc": 以字符串来连接字符串列表中每个元素，合并为一个新的字符串
# print(result)

# list = []
#
# for i in range(100, 200):
#     if i % 2 != 0 :
#       list.append(i)
# print(list)

# for i in range(100, 200):
#     if i % 2 != 0 :
#       print(i, end=',')

# i = 1
# j = 1
# while i <= 5:
#     while j <= i:
#       print('*' * j)
#       j += 1
#     i += 1

# list = []
# for i in range(1, 100):
#     if i % 7 != 0 :
#         print(i, end='\n')

import random
print('*' * 20, '猜数字', '*' * 20)

count = 5

j = random.randint(1,100)

# 玩家有5次机会，每猜一次系统就会提示玩家该数字是偏大还是偏小，如果猜中了，
# 则告知玩家并提前结束游戏，如果5次都没猜中，结束游戏并告知正确答案。
while count:
    i = int(input('请输入一个数:'))
    if i == j :
        print('恭喜你，猜中了!')
        break

    elif i > j :
        print('偏大')

    elif i < j :
        print('偏小')

    count -= 1

else:
    print('5次都用完了还没才出来，你也太菜了！')


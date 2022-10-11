# num = 1
# age = 18
# name = '小明'
# height = 1.78
#
# # 传统格式化
# print('我叫%s，学号%03d，年龄为%d，身高为%.2f米' % (name, num, age, height))
#
# # fstring格式化
# print(f'我叫{name}，学号{num:03d}，年龄为{age}，身高为{height}米')

# name_list = ['mike', 'yoyo', 'rock', 'lily']
#
# for name in name_list:
#     if name == 'yoyo':
#         print(name)
#         break


alpha_list = ['A', 'B', 'C', 'A', 'B', 'B', 'D', 'E', 'D']

# 对列表中的数据进行去重
my_list = list(set(alpha_list))

# 对列表进行排序
my_list.sort()

# 遍历统计每个字符出现的次数
for c in my_list:
    count = alpha_list.count(c)
    print(f'字母：{c}，频次：{count}')













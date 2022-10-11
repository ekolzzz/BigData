# num = 1
# age = 18
# name = '小明'
# height = 1.78

# '我叫小明，学号001，年龄为18，身高为1.78米'
# print(f'我叫{name}，学号{num}，年龄为{18}，身高为{height}米')
# print('我叫%s，学号%03d，年龄为%d，身高为%.2f' % (name, num, age, height))

# name_list = ['mike', 'yoyo', 'rock', 'lily']

# for name in name_list:
#     if name == 'yoyo' :
#         print(name)

# alpha_list = ['A', 'B', 'C', 'A', 'B', 'B']
#
# data = {}
#
# for character in alpha_list:
#     # print(character)
#     data[character] = alpha_list.count(character) # 牛逼
#
# for key, vaule in data.items():
#     print(f'字母：{key} 频次：{vaule}')

def new_num():
    global num
    num = 10
    return num

num = 100

new_num()
print(num)
"""
num.txt:
10
18
30
11
12
15
"""

# num_list = [10, 18, 30, 11, 12, 15]
# with open('num.txt', 'w', encoding='utf8') as f:
#     for num in num_list:
#         # print(num)
#         f.write(str(num)+'\n')

# 定义一个空列表
num_list = []
sum = 0
# 打开num.txt文件
with open('num.txt', 'r', encoding='utf8') as f:
    # 读取所有内容
    res = f.readlines()
    # print(type(res), res)

    # 遍历列表res里的每个元素
    for num_str in res:
        # print(type(num_str), num_str)

        # 字符串.strip(目标字符串): 返回新字符串，去除 字符串 左右两边的目标字符串, 不设置目标字符串则去除空格
        # 将str转换成int类型
        num = int(num_str.strip('\n'))
        # print(type(num), num)

        # 列表添加元素
        num_list.append(num)
    print(num_list)

    for num in num_list:
        sum += num
    print(sum)


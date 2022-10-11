"""
查找	字符串.find(目标字符串, 开始索引, 结束索引)	在指定范围内, 查询目标字符串的索引, 不存在返回-1
替换	字符串.replace(原内容, 新内容, 替换次数)	返回一个替换了原内容的新字符串，可以指定替换次数
分割	字符串.split(分割符)	以分割符拆分字符串, 返回列表
拼接	字符串 + 字符串	拼接两个字符串
字符串.join(字符串列表)	以字符串来连接字符串列表中每个元素，合并为一个新的字符串
"""

"""
查找	字符串.find(目标字符串, 开始索引, 结束索引)	在指定范围内, 查询目标字符串的索引, 不存在返回-1
"""
#         0123456
# my_str = 'hello python! life is short, you need python!'

# 需求：从 my_str 字符串中查找 python
# res = my_str.find('python')
# print(res)
#
# res = my_str.find('python',14) # 14是开始范围
# print(res)
#
# # 需求：从 my_str 字符串中查找 itheima
# res = my_str.find('itheima') # 查不到返回值-1
# print(res)

"""
替换	字符串.replace(原内容, 新内容, 替换次数)	返回一个替换了原内容的新字符串，可以指定替换次数
"""
# my_str = 'hello python! life is short, you need python!'
# # 需求：将 my_str 字符串中的 python 替换为 itheima
#
# new_str = my_str.replace('python','itheima') #不写替换次数就会全部替换
#
# print(new_str)

"""
分割	字符串.split(分割符)	以分割符拆分字符串, 返回列表
"""
my_str = 'hello python! life is short, you need python!'
# 需求：将 my_str 字符串按照空格分隔成列表数据

new_str = my_str.split(' ')
print(new_str)

new_str = my_str.split('e')
print(new_str)

"""
拼接	字符串 + 字符串	拼接两个字符串
字符串.join(字符串列表)	以字符串来连接字符串列表中每个元素，合并为一个新的字符串
"""
# str1 = 'hello '
# str2 = 'python'
#
# # 需求：将 str1 和 str2 拼接成 'hello python'
# new_str = str1 + str2
# print(new_str)

# 需求：将 str_list 使用空格连接成一个字符串
# str_list = ['hello', 'python!', 'life', 'is', 'short,', 'you', 'need', 'python!']
#
# list = ' '.join(str_list)
# print(list)
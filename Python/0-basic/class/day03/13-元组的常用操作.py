"""
元组[索引]	根据索引取值，索引不存在会报错
len(元组)	元组长度(元素个数)
值 in 元组	判断元组中是否包含某个值
值 not in 元祖 判断元组中不包含某个值
"""

name_tuple = ('smart', 'yoyo', 'rock', 'lily')

print(len(name_tuple))

if 'rock' in name_tuple:
    print('rock在元组中')
else:
    print('rock不在元组中')

print('====================================')

for i in name_tuple :
    print(i)

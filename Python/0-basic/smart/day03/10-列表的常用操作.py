"""
增加	列表.append(值)	在末尾追加数据
删除	列表.remove(值)	删除第一个出现的指定数据
修改	列表[索引] = 值	修改指定索引的数据，数据不存在会报错
查询	列表[索引]	根据索引取值，索引不存在会报错
len(列表)	列表长度(元素个数)
值 in 列表	判断列表中是否包含某个元素，结果是 True 或 False
排序	列表.sort()	升序排序
"""

name_list = ['smart', 'yoyo', 'rock', 'yoyo', 'lily']
print(name_list)

"""
增加	列表.append(值)	在末尾追加数据
"""
name_list.append('jack')
print(name_list)

"""
删除	列表.remove(值)	删除第一个出现的指定数据
"""
name_list.remove('yoyo')
print(name_list)

"""
修改	列表[索引] = 值	修改指定索引的数据，数据不存在会报错
查询	列表[索引]	根据索引取值，索引不存在会报错
"""

# 把列表中的 'rock' 改成 'rose'
name_list[1] = 'rose'
print(name_list)

"""
len(列表)	列表长度(元素个数)
"""

print(len(name_list))

"""
值 in 列表	判断列表中是否包含某个元素，结果是 True 或 False
值 not in 列表 判断列表中是否不包含某个元素，结果是 True 或 False
"""

print('rose' in name_list) # True
print('rose' not in name_list) # False

# in 和 not in 经常配合分支结构来使用
if 'rose' in name_list:
    print('rose在列表中')
else:
    print('rose不在列表中')

"""
排序	列表.sort()	升序排序
"""

num_list = [1, 3, 2, 8, 7, 6, 10]

num_list.sort()
print(num_list) # 从小到大：升序

# reverse=True：作用就是让sort排序的时候，使用降序（从大到小）
num_list.sort(reverse=True)
print(num_list)

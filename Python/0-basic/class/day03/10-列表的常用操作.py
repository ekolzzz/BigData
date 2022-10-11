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

"""
增加	列表.append(值)	在末尾追加数据
"""
name_list.append('ekol')
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
name_list[1] = '卢本伟牛逼！'
print(name_list)

print(name_list)
"""
len(列表)	列表长度(元素个数)
"""

print(len(name_list))

"""
值 in 列表	判断列表中是否包含某个元素，结果是 True 或 False
值 not in 列表 判断列表中是否不包含某个元素，结果是 True 或 False
"""
# 配合条件分支使用

print('rock' in name_list)
print('rock' not in name_list)
print('ekol' not in name_list)
print('ekol' in name_list)

"""
排序	列表.sort()	升序排序
"""

num_list = [1, 3, 2, 8, 7, 6, 10]
num_list.sort()
print(num_list)
print(num_list.sort()) #没有返回值，None

# reverse = True: 作用就是让sort排序的时候，使用降序（从大到小排列）
num_list.sort(reverse=True)
print(num_list)
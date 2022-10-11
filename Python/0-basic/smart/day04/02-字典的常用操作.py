"""
增加	字典[键] = 值	键不存在，会添加键值对
修改	字典[键] = 值	键存在，会修改键值对的值
删除	字典.pop(键)	删除指定键值对,返回被删除的值,如果键不存在,会报错
查询	字典[键]	根据键取值，键值对不存在会报错
字典.get(键)	根据键取值，键值对不存在返回None, 不会报错
遍历	
    for key in 字典                  遍历字典，获取所有的键
    for value in 字典.values()       遍历字典，获取所有的值
    for key, value in 字典.items()	遍历字典, 获取所有的键值对 (键, 值)
"""

my_dict = {'name': 'smart', 'age': 18, 'city': '上海'}
print(my_dict)
"""
增加	字典[键] = 值	键不存在，会添加键值对
修改	字典[键] = 值	键存在，会修改键值对的值
"""

# 向字典中添加一个键值对，键叫 'gender', 值是：True
my_dict['gender'] = True
print(my_dict)

# 将字典中 'age' 这个键对应值修改为：20
my_dict['age'] = 20
print(my_dict)

"""
删除	字典.pop(键)	删除指定键值对,返回被删除的值,如果键不存在,会报错
"""
# 删除字典中的 'gender' 这个键值对
res = my_dict.pop('gender')
print(res)
print(my_dict)


"""
查询	字典[键]	根据键取值，键值对不存在会报错
字典.get(键)	根据键取值，键值对不存在返回None, 不会报错
"""
print(my_dict['name'])
print(my_dict.get('name'))

# KeyError: 'gender'
# print(my_dict['gender'])
# None：是 python 中的一个关键字，代表什么都没有
print(my_dict.get('gender'))

print('=============================================')
"""
遍历	
    for key in 字典                  遍历字典，获取字典中所有的键
    for value in 字典.values()       遍历字典，获取字典中所有的值
    for key, value in 字典.items()	遍历字典, 获取字典中所有的键值对 (键, 值)
"""

my_dict = {'name': 'smart', 'age': 18, 'city': '上海'}

# 只遍历字典中的key
for key in my_dict:
    print(key)

print('--------------------')
# 只遍历字典中的value
for value in my_dict.values():
    print(value)

print('--------------------')
# 同时遍历字典中的key和value
for key, value in my_dict.items():
    print(key, value)
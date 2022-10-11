"""
字典(dict)：也可以用来存储多个数据，其中存储的每个数据都包括key(名字)和value(值)，可以通过key取到对应的值
定义：
    字典变量 = {key1: value1, key2: value2, key3: value3}
访问：
    字典变量[key]
"""

# 定义一个字典数据：存储 name 为 'smart', age 为 18, city 为 '上海'
# 我们在定义字典时，key一般都是字符串类型，但是value可以是任何数据类型
my_dict = {'name': 'smart', 'age': 18, 'city': '上海'}
# <class 'dict'>
print(type(my_dict), my_dict)

# 定义空字典
dict1 = {}
dict2 = dict()
print(type(dict1), dict1)
print(type(dict2), dict2)

print(my_dict['name'])
print(my_dict['age'])
print(my_dict['city'])

# KeyError: 'gender'
# 键错误：这个键在字典中不存在
# 注意：从字典中根据键取值时，键必须存在，否则就会出现 KeyError 错误
print(my_dict['gender'])


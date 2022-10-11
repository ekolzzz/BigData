"""
字典(dict)：也可以用来存储多个数据，其中存储的每个数据都包括key(名字)和value(值)，可以通过key取到对应的值
定义：
    字典变量 = {key1: value1, key2: value2, key3: value3}
访问：
    字典变量[key]
"""

# 定义一个字典数据：存储 name 为 'smart', age 为 18, city 为 '上海'

# 我们在定义字典时,key一般都是字符串类型,但是value可以是任意数据类型
my_dict = {'name': 'ekol', 'age': 18, 'city': 'Wuxi'}
print(my_dict['name'])

# KeyError: 'gender'
# 键错误
# 注意:从字典中根据键取值时,键必须存在,否则会出现KeyError 错误
print(my_dict['gender'])

# 定义空字典

dict1 = {}
dict2 = dict()

print(dict1,type(dict1))
print(dict2,type(dict2))



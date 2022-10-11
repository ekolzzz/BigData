"""
学习目标：能够利用 zip 函数组合疫情地图数据
"""

import json

# ① 读取 `疫情.txt` 文件的内容，将读取的数据转换为 python 中的字典
with open('./疫情.txt', 'r', encoding='utf8') as f:
    content = f.read() # str
    data_dict = json.loads(content)
    # print(type(data_dict), data_dict)

# ② 从数据中提取每个省份名称和对应的确诊人数
# print(type(data_dict['areaTree']), data_dict['areaTree'])
# print(type(data_dict['areaTree'][0]), data_dict['areaTree'][0])
# print(type(data_dict['areaTree'][0]['children']), data_dict['areaTree'][0]['children'])

provinces_data = data_dict['areaTree'][0]['children']
# print(type(provinces_data), provinces_data)

# 遍历 provinces_data，获取每个省的名称和对应的确诊人数
# 定义一个空字典
# 语法：字典[键] = 值，键在字典中不存在，就是添加键值对；键在字典中存在，就是修改键对应的值；
# result_dict['台湾'] = 15880
# result_dict['江苏'] = 1576
result_dict = {}

for province_data in provinces_data:
    # 获取省的名称
    province_name = province_data['name']
    # 获取省的确诊人数
    confirm_count = province_data['total']['confirm']
    # print(province_name, confirm_count)
    # 向字典中添加键值对，省的名称作为 key，对应的确诊人数作为 value
    result_dict[province_name] = confirm_count

    # result_dict[province_data['name']] = province_data['total']['confirm']

print(result_dict)

# 处理 result_dict 这个字典，得到一个列表套元祖的形式
# {'台湾': 15880, '江苏': 1576, '云南': 982, ...}
# [('台湾', 15880), ('江苏', 1576), ('云南', 982), ...]

# 字典.keys()：获取字典中的所有 key 组成的一个容器数据
# 字典.values()：获取字典中的所有 value 组成的一个容器

# print(result_dict.keys())
# print(result_dict.values())

result = zip(result_dict.keys(), result_dict.values())
data = list(result)
print(data)
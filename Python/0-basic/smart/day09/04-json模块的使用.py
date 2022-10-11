"""
学习目标：掌握 json 模块中 dumps 和 loads 函数的使用

json.dumps(列表或字典)：将 python 中的列表或字典转换为 json 字符串
json.loads(json字符串)：将 json 字符串转换为 python 中的列表或字典
"""
import json

data = [{'name': '老王', 'age': 16}, {'name': '张三', 'age': 20}]
print(type(data), data)

res = json.dumps(data)
print(type(res), res)

# 注意：将列表或字典转换成 json 字符串时，不要用 str 转换！！！
res = str(data)
print(type(res), res)

print('======================================================')

json_str = '[{"name": "老王", "age": 16}, {"name": "张三", "age": 20}]'

res = json.loads(json_str)
print(type(res), res)

# 注意：给 loads 函数传递的内容一定要符合 json 字符串格式，否则 loads 会出错！！！
# my_str = "[{'name': '老王', 'age': 16}, {'name': '张三', 'age': 20}]"
# res = json.loads(my_str)
# print(type(res), res)

"""
学习目标：掌握 json 模块中 dumps 和 loads 函数的使用
"""
import json

data = [{'name': '老王', 'age': 16}, {'name': '张三', 'age': 20}]
print(type(data), data)

res = json.dumps(data)
print(type(res), res)

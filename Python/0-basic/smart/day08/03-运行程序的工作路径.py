"""
运行程序的工作路径
"""
import os

"""
获取当前工作的路径：默认就是当前程序文件所在的目录
语法格式：路径变量 = os.getcwd() # cwd：current working directory
"""

# 注意：一个 python 程序的默认工作目录，就是这个 py 文件所在的目录
res = os.getcwd()
print(res)

"""
改变运行程序的工作目录，切换指定的路径
语法格式：os.chdir(改变的路径) # ch：change 改变
"""

# 需求：将当前程序的工作路径改成 python
os.chdir('python')
res = os.getcwd()
print(res)

"""
运行程序工作路径意义：程序中使用的相对路径都是基于工作路径而言的

.：代表当前工作目录
..：代表当前工作目录的上一层目录
"""

with open('./4.txt', 'w', encoding='utf8') as f:
    f.write('111111')
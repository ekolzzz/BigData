"""
os模块：python中进行文件、目录相关操作的模块(工具包)
"""
# 导入 os
import os

"""
os模块中的rename()可以完成对文件的重命名操作
语法格式：os.rename(旧的文件名，新的文件名)
"""

# os.rename('1.txt', '1-最终版.txt')


"""
os模块中的remove()可以完成对文件的删除操作，不能删除文件夹
语法格式：os.remove(待删除的文件名)
"""

# os.remove('1-最终版.txt')


"""
创建文件夹，只能创建文件夹，不能创建普通文件
语法格式：os.mkdir(文件夹的名字) # mk：make  dir：directory
"""

# os.mkdir('a')


"""
删除文件夹，只能删除空的文件夹
语法格式：os.rmdir(待删除文件夹的名字) # rm：remove
"""

# os.rmdir('a')



"""
获取某个目录的文件信息，获取文件夹或文件的名字
语法格式：目录列表变量 = os.listdir(指定某个目录)
如果不指定目录，默认当前路径
"""

# res = os.listdir('python')
# print(res)


"""
语法格式：os.path.exists(路径)
判断路径是否存在，存在返回True，如果文件不存在返回False
注意：路径可能是一个文件夹路径，也可能是一个文件路径
"""

# res = os.path.exists('./python/1.txt')
# print(res)
#
# res = os.path.exists('./python/a')
# print(res)
#
# res = os.path.exists('./python/4.txt')
# print(res)

"""
语法格式：os.path.isfile(文件路径)
判断一个文件是否存在，存在返回True，如果文件不存在返回False
"""

res = os.path.isfile('./python/1.txt')
print(res)

res = os.path.isfile('./python/a')
print(res)

"""
案例：批量修改 python 目录下的文件名
1.txt -> 黑马出品-1.txt
2.txt -> 黑马出品-2.txt
3.txt -> 黑马出品-3.txt
"""
import os

"""
实现思路：
1、 首先获取python目录下有哪些内容：listdir
2、 遍历获取的每个内容，然后进行重命名：rename

"""
# 1、 首先获取python目录下有哪些内容：listdir
res_list = os.listdir('python')

os.chdir('python')

for old_name in res_list:
    os.rename(old_name, '黑马出品-' + old_name)
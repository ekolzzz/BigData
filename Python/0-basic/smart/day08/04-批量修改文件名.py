"""
案例：批量修改 python 目录下的文件名
1.txt -> 黑马出品-1.txt
2.txt -> 黑马出品-2.txt
3.txt -> 黑马出品-3.txt
"""
import os

"""
实现思路：
① 首先获取 python 目录下有哪些内容：listdir
② 遍历获取的每个内容，然后进行重命名：rename
"""

# ① 首先获取 python 目录下有哪些内容：listdir
res_list = os.listdir('python')
# print(res_list)

# 将当前程序的工作路径切换成 python
os.chdir('python')

# ② 遍历获取的每个内容，然后进行重命名：rename
for old_name in res_list:
    # os.rename('1.txt', '黑马出品-1.txt') -> os.rename('./1.txt', './黑马出品-1.txt')
    # os.rename('2.txt', '黑马出品-2.txt')
    # ...
    os.rename(old_name, '黑马出品-' + old_name)

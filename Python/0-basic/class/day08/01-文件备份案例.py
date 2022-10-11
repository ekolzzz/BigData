"""
文件备份案例需求：
    比如有当前目录下有一个文件 abc.abc.txt，备份之后的文件名为：abc.abc[备份].txt
    1.txt -> 1[备份].txt
    2.txt -> 2[备份].txt
    abc.abc.txt -> abc.abc[备份].txt
"""

"""
文件备份的思路分析：【读取旧文件的内容，写入到新文件中】
① 只读模式打开旧文件，只写模式打开新文件
② 读取旧文件的内容，写入到新文件中
③ 关闭旧文件和新文件
"""

# 需求1：可以动态让用户输入当前目录下要备份的文件名
# 需求2：新文件的名称根据旧文件的名称自动生成
# 需求3：改写程序，让程序可以备份任何类型的文件（文本文件、图片、音频、视频等）
# 需求4：大文件如何备份？？？假设你要备份的文件有8G，但是你的电脑内存只有4G

# 提示用户输入要备份的文件名
old_name = input('请输入要备份的文件名：')

# 根据旧文件名生成备份的新文件名
index = old_name.rfind('.')
new_name = old_name[:index] + '[备份]' + old_name[index:]
print(f'新的文件名为：{new_name}')

# ① 只读模式打开旧文件，只写模式打开新文件
old_file = open(old_name, 'rb')
new_file = open(new_name, 'wb')

# ② 读取旧文件的内容，写入到新文件中
content = old_file.read()
new_file.write(content)

# ③ 关闭旧文件和新文件
old_file.close()
new_file.close()

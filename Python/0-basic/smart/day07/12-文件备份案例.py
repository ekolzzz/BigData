"""
文件备份案例需求：
    比如有一个文件 abc.abc.txt，备份之后的文件名为：abc.abc[备份].txt
"""

"""
文件备份的思路分析：【读取旧文件的内容，写入到新文件】

需求1：将当前目录下1.txt文件，进行备份，备份文件名叫：1[备份].txt
需求2：可以动态让用户输入当前目录下要备份的文件名
需求3：新文件的名称根据旧文件的名称自动生成
    1.txt -> 1[备份].txt
    2.txt -> 2[备份].txt
    abc.abc.txt -> abc.abc[备份].txt
需求4：改写程序，让程序可以备份任何类型的文件（文本文件、图片、视频、音频等）
需求5：大文件如何备份？（假设你要备份的文件有8G，你的内存只有4G)
    读一点，写一点，直到文件读取结束
"""
# 提示用户输入要备份的文件名
old_name = input('请输入要备份的文件名：')

# 根据旧文件的名称，生成新文件的名称
index = old_name.rfind('.')
new_name = old_name[:index] + '[备份]' + old_name[index:]
print('新文件名：', new_name)

# ① 打开旧文件和新文件
old_file = open(old_name, 'rb')
new_file = open(new_name, 'wb')

# ② 读取旧文件的内容，写入到新文件
content = old_file.read()
new_file.write(content)

# ③ 关闭旧文件和新文件
old_file.close()
new_file.close()
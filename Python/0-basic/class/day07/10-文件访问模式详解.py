"""
文件访问模式：
    文件变量 = open(打开文件路径, 访问模式)
"""

"""
# 只可读写文本文件，不可以读写其他类型的文件
访问模式                说明
r	    只用于文本文件读取，默认模式。文件不存在，会报错。
w	    只用于文本文件写入。文件存在则先清空内容，文件不存在，创建新文件。
a	    只用于文本文件写入。文件存在则追加内容，文件不存在，创建新文件。

r+	    用于文本文件读写。文件不存在，会报错。
w+	    用于文本文件读写。文件存在则先清空内容，文件不存在，创建新文件。
a+	    用于文本文件读写。文件存在则追加内容，文件不存在，创建新文件。

# 可以读写任意文件类型
rb	    二进制格式的只读操作。
wb	    二进制格式的只写操作。
ab	    二进制格式的追加操作。
"""

# w：write 会先将原有文件的内容清空，然后再写入新内容
with open('3.txt', 'r+', encoding='utf8') as f:
    f.write('使用(w)write写入新内容\n')
    f.write('hello hadoop\n')
    f.write('hello spark\n')
    res = f.read()
    print(res)

# r：read 文件不存在，会报错
with open('3.txt', 'r', encoding='utf8') as f:
    res = f.read()
    print(res)

# a：append 追加，在原有文件末尾追加写入新内容
with open('3.txt', 'a', encoding='utf8') as f:
    f.write('使用(a)append写入新内容')
    f.write('hello hadoop\n')
    f.write('hello spark\n')




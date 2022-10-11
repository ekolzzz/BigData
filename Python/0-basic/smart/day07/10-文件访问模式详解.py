"""
文件访问模式：
    文件变量 = open(打开文件路径, 访问模式)
"""

"""
访问模式                说明
r	    只用于文本文件读取，默认模式。文件不存在，会报错。
w	    只用于文本文件写入。文件存在则先清空内容，文件不存在，创建新文件。
a	    只用于文本文件写入。文件存在则追加内容，文件不存在，创建新文件。

r+	    用于文本文件读写。文件不存在，会报错。
w+	    用于文本文件读写。文件存在则先清空内容，文件不存在，创建新文件。
a+	    用于文本文件读写。文件存在则追加内容，文件不存在，创建新文件。

rb	    二进制格式的只读操作。
wb	    二进制格式的只写操作。
ab	    二进制格式的追加操作。
"""


# w：write 会先将原有文件的内容清空，然后再写入新内容
with open('1.txt', 'w', encoding='utf8') as f:
    f.write('hello hadoop\n')
    f.write('hello spark\n')

# a：append 追加，在原有文件末尾追加写入新内容
with open('1.txt', 'a', encoding='utf8') as f:
    f.write('hello hadoop\n')
    f.write('hello spark\n')

# # r：文本只读模式
with open('1.txt', 'r', encoding='utf8') as f:
    # 第一步：先读取文件中二进制内容
    # 第二步：将读取的二进制内容根据指定的编码方式转换成对应文本
    res = f.read()
    print(res)

# # rb：二进制只读模式
# # 注意：以二进行方式操作一个文件时，不需要指定编码方式
# with open('1.txt', 'rb') as f:
#     # 读取文件中二进制内容
#     res = f.read()
#     print(res)


# 演示：w+：文本文件读写（可读可写）
with open('2.txt', 'w+', encoding='utf8') as f:
    # 先写入内容
    # 注意：写入内容之后，文件指定已经移动了文件的末尾
    f.write('hello world')

    # 调整文件指针的位置
    # 第二个 0：表示文件的开头
    # 第一个 0：表示从文件的开头向后移动几个字符
    f.seek(0, 0)

    # 然后读取内容
    res = f.read()
    print(res)
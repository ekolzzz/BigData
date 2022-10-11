
"""
文件编码问题
"""

"""
【任何文件中的内容存储到磁盘上，都是以二进制数字的形式进行存储的】。

编码主要是针对文本文件中的文本内容，编码规定了每个文本内容在硬盘上存储时，用什么数字进行表示；
对于同一个文本内容，不同的编码，规定在磁盘上存储的对应数字往往是不一样的，常见的编码方式有：gbk，utf8。

比如"中"这个字：
1）utf8编码时，对应的数字为：'\xe4\xb8\xad'
2）gbk编码时，对应的数字为：'\xd6\xd0'

使用：
    文件变量 = open('操作文件', '访问模式', encoding='编码方式')

注意：
1）当通过程序读写文本文件时，需要指定编码方式
    如果是读取文本文件内容，读取文件中存储的二进制数字之后，会根据编码方式转换为对应的文本，方便用户查看
    如果是写入文本文件内容，则会根据编码方式将文本转换为对应的二进制数字，然后再写入到文件中进行存储

2）读写文本文件时，编码方式必须统一，否则会出现乱码或错误
    当我们通过程序读取文件内容时，如果文件本身是utf8编码，而我们用gbk编码解析，
    或者
    如果文件本身是gbk编码，而我们用utf8编码解析，那么文件操作就会出现乱码或错误。

注意：
1）windows操作系统下，open操作文件时，encoding参数默认为gbk
2）linux/mac操作系统下，open操作文件时，encoding参数默认为utf8

windows系统：
    文件变量 = open('操作文件', '访问模式', encoding='gbk')

Mac/Linux系统：
    文件变量 = open('操作文件', '访问模式', encoding='utf8')
"""

# 以UTF8编码方式写入一个文件
with open('1.txt', 'w', encoding ='utf8') as f:
    r = f.write('123abc你好呀！')

# 以GBK编码方式写入一个文件
with open('2.txt', 'w', encoding ='gbk') as f:
    r = f.write('456def你好呀！')

# 以UTF8编码方式读取一个文件
with open('1.txt', 'r', encoding='utf8') as f:
    res = f.read()
    print(res)

# 以GBK编码方式读取一个文件
with open('2.txt', 'r', encoding='gbk') as f:
    res = f.read()
    print(res)

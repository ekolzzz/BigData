"""
文件的读写：通过文件变量可以进行文件的读写操作
"""

"""
文件对象相关函数：
1）write：向文件中写入数据
    使用方式 => 文件变量.write(要写入的内容)
    
2）read：从文件中读取数据
    使用方式 => 文件变量.read(读取的字符数量)
    注意：如读取的字符数量不设置，则默认全部读取
    
3）readline：每次读取文件中的一行数据
    使用方式 => 文件变量.readline()

4）readlines：一次读取文件中的所有行数据
    使用方式 => 文件变量.readlines()
    注意：readlines函数返回的是列表，列表中的每个元素是每一行数据
"""

"""
write：向文件中写入数据
"""
with open('1.txt', 'w') as f:
    f.write('hello world\n')
    f.write('hello python\n')
    f.write('hello itcast')

    # 注意：只能写入字符串数据
    # TypeError: write() argument must be str, not int
    # f.write(20)


"""
read：从文件中读取数据
"""
# 文件指针：记录文件操作的位置，比如我们每一次读取文件内容，文件指针的位置
# 都会自动向后移动，下次的读取是接着上次的位置继续向后读取的。

# 问题：如何判断已经读取到了文件的末尾了？
# ①：如果使用的 read 或 readline，当读取的内容是空字符串''时，就说明已经读取到了文件的末尾
# ②：如果使用的 readlines，当读取的结果是空列表[]时，就说明已经读取到了文件的末尾

with open('1.txt', 'r') as f:
    res = f.read(5) # 'hello'
    print(res)

    res = f.read(5) # ' worl'
    print(res)

    res = f.read(5) # 'd\nhel'
    print(res)

    res = f.read() # 'lo python\nhello itcast'
    print(res)

    res = f.read() # ''
    print(res)



"""
readline：每次读取文件中的一行数据
"""
with open('1.txt', 'r') as f:
    res = f.readline()
    print(res)

    res = f.readline()
    print(res)

    res = f.readline()
    print(res)

    res = f.readline() # ''
    print(res)



"""
readlines：一次读取文件中的所有行数据
返回值是一个列表，列表中每个元素就是文件中的每一行数据
"""

with open('1.txt', 'r') as f:
    res = f.readlines()
    print(type(res), res)

    res = f.readlines() # []
    print(type(res), res)




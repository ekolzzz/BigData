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
    f.write('hello itcast\n')

"""
read：从文件中读取数据
"""
with open('1.txt', 'r') as f:
    res = f.read(5)
    print(res)

    res = f.read(5)
    print(res)

    res = f.read(5)
    print(res)

    print('*' * 30)

    res = f.readline()
    print(res)

    print('*' * 30)

    res = f.readlines()
    print(res)

print('*' * 30)
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

"""
readlines：一次读取文件中的所有行数据
"""
with open('1.txt', 'r') as f: # 列表
    res = f.readlines()
    print(res)



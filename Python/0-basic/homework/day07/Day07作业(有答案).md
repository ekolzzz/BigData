# Python基础07-文件操作

[TOC]

## 能力目标

- [ ] 理解学生名片管理系统代码的实现
- [ ] 知道使用open函数能够打开文件
- [ ] 知道使用close方法关闭一个打开的文件
- [ ] 知道使用文件对象的write方法向文件中写入数据
- [ ] 知道read方法能够实现读取所有、指定长度的文本数据
- [ ] 知道readline方法能够从文件中读取一行数据
- [ ] 知道readlines方法能够从文件中按行读取所有数据
- [ ] 知道文件备份案例的实现思路



## 关卡一：综合题

### 1. 设计一个程序

从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。

**参考答案**

```python
file_name = input('输入文件名:\n')
fp = open(file_name,"w", encoding='utf8')
ch = input('输入字符串:\n')
for i in ch:
    if i != '#':
        fp.write(i)
    else:
        break
fp.close()
```

### 2. 设计一个程序

从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件”test”中保存。

**参考答案**

```python
fp = open('test.txt', 'w', encoding='utf8')
string = input('请输入字符串:\n')
string = string.upper()
fp.write(string)
fp = open('test.txt', 'r')
print(fp.read())
fp.close()
```

### 3. 设计一个程序

将”python是我用过的最好用，最优雅的计算机语言，没有之一！！！“这句话从文件A中读取出来，然后以逗号为分割符分割成三部分，然后依次存入B、C、D文件中。

**参考答案**

```python
# 打开A 文件

f = open("A.txt", "r", encoding="utf8")

# 读取A 文件中的内容

my_str = f.read()

# 将读取出来的内容以 ， 为切割符， 切割开
f.close()
my_list = my_str.split('，')

# 分别写入 B C D 文件中
B = open("B.txt", "w", encoding='utf8')
B.write(my_list[0])
B.close()
C = open("C.txt", "w", encoding='utf8')
C.write(my_list[1])
C.close()
D = open("D.txt", "w", encoding='utf8')
D.write(my_list[2])
D.close()
```

### 4. 设计一个程序

- 在python用户目录下创建python基础班文件夹
- 在文件夹中创建gai_lun.txt文件
- 打开文件在gai_lun.txt中写入"德玛西亚！人在塔在！"
- 在文件夹中创建gai_lun副本.txt文件
- 将gai_lun.txt文件中的数据写入gai_lun副本.txt文件中
- 打开文件，查看文件中是否有内容

**参考答案**

```python

# 导入模块
import os

# 记录文件夹名称
file_name = "python基础班文件夹"
# 第一步
# 创建一个文件夹()
os.mkdir(file_name)


# 第二步
# 先打开gailun.txt文件
old_f = open("./python基础班文件夹/gai_lun.txt", "r", encoding="utf8")
# 读取数据
result = old_f.read()

# 创建gailun副本.txt文件
new_f = open("./python基础班文件夹/gai_lun副本.txt", "w", encoding="utf8")
# 写入数据
new_f.write(result)

# 关闭文件
old_f.close()
new_f.close()
```

"""
假设有一个文件 num.txt，里面存储了如下的一些数字，内容如下：
```
10
18
30
11
12
15
```
编写一个 python 程序，读取文件中的内容，存储成 python 中的列表形式：
[10, 18, 30, 11, 12, 15]

然后计算上面的一组数字的和，并打印最终的结果。
"""
# 定义一个空列表
my_list = []

# 读取 num.txt 文件中的每一行内容
with open('./num.txt', 'r', encoding='utf8') as f:
    # 读取文件中的所有行
    lines = f.readlines()
    print(lines)

    # 遍历出每一行的数据
    for line in lines:
        # 去除每一行的 \n
        line = line.strip('\n')
        # 把字符串转换为数字
        num = int(line)
        # 把数据添加到列表中
        my_list.append(num)

    print(lines)
    print(my_list)

    # 计算列表中所有数字的和
    # 内置函数：sum(列表)
    result = sum(my_list)
    print(result)
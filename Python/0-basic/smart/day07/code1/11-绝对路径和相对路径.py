"""
绝对路径：是指文件在硬盘上真正存在的路径(从磁盘根目录开始描述)，是电脑完整的路径
相对路径：目标文件相对于当前位置所处的位置(基于一个文件的位置去描述另一个文件的位置)

文件访问模式：
    文件变量 = open(打开文件路径, 访问模式, encoding='编码方式')
"""

# 绝对路径访问 test1.txt 和　test2.txt
# test1.txt绝对路径：C:\Users\smart\Desktop\pycode\day07\code1\test1.txt
# test2.txt绝对路径：C:\Users\smart\Desktop\pycode\day07\code2\test2.txt

# \：反斜杠，在 python 的字符串中具有特殊含义，就是把 \ 之后的一个字符进行转义，表示一个特殊的作用
# \n：换行符
# \t：制表符
# 怎么解决这个问题？
# ① 在字符串用两个\表示一个普通的\字符 【不推荐，比较麻烦】
# ② 把文件路径中的\（反斜杠）换成/（正斜杠）【推荐，除了windows系统，其他操作系统路径中的斜杆用的都是正斜杆】
with open('C:\\Users\\smart\\Desktop\\pycode\\day07\\code1\\test1.txt', 'r', encoding='utf8') as f:
    res = f.read()
    print(res)

with open('C:/Users/smart/Desktop/pycode/day07/code1/test1.txt', 'r', encoding='utf8') as f:
    res = f.read()
    print(res)


# 相对路径访问 test1.txt 和 test2.txt
# 思考1：假设我要在当前的py文件中，打开test2.txt文件，请问，相对于当前py文件，要打开的test2.txt文件在什么位置？
# 在当前文件的上一层目录（指的就是day07），下面有一个 code2 目录，test2.txt 就在 code2 目录下
# 相对路径：../code2/test2.txt
with open('../code2/test2.txt', 'r', encoding='utf8') as f:
    res = f.read()
    print(res)

# 思考2：假设我要在当前的py文件中，打开test1.txt文件，请问，相对于当前py文件，要打开的test1.txt文件在什么位置？
# 在当前文件所在目录下（指的就是code1），就有要打开的 test1.txt 文件
# 相对路径：./test1.txt
with open('./test1.txt', 'r', encoding='utf8') as f:
    res = f.read()
    print(res)

# 注意：如果我们要打开的是当前目录下的文件，相对路径前面的./可以省略，可以直接写文件名即可
with open('test1.txt', 'r', encoding='utf8') as f:
    res = f.read()
    print(res)

# 思考3：假设我要在当前的py文件中，打开1.txt文件，相对路径是什么？
# 相对路径：../1.txt
with open('../1.txt', 'r', encoding='utf8') as f:
    res = f.read()
    print(res)

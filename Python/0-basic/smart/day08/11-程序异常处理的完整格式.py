"""
程序异常处理
学习目标：知道程序进行异常处理的完整格式
"""

"""
try:
    可能发生异常的代码
except:
    处理异常的代码
else:
    没有发生异常，except不满足执行else
finally:
    不管有没有异常，最终都要执行
"""

try:
    print('===============')
    # f = open('xxx.txt', 'r')
    num = 3 / 2
    print('===============')
except:
    print('try里面发生了异常')
else:
    print('try里面没有发生异常')
finally:
    print('不管try里面有没有异常，finally代码都会执行')


# 推荐大家使用 with 打开文件：可以自动把文件关闭（而且当with里面的代码出现异常时，也可把文件关闭掉）
with open('xxx.txt', 'w', encoding='utf8') as f:
    # 操作文件
    # 操作文件
    # 操作文件
    # 操作文件
    pass
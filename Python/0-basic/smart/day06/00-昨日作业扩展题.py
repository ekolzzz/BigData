"""
定义一个函数，接受三个参数，分别为字符串s、数值a1、数值a2，将字符串s从下标a1开始的a2个字符删除，并把结果返回
"""


def cut_str(s, a1, a2):
    """
    功能：把字符串s中，下标a1开始的a2字符删除，返回剩下的内容
    """
    s1 = s[:a1]
    s2 = s[a1+a2:]
    return s1 + s2


res = cut_str('123456789', 2, 4)
print(res)

res = cut_str('123456789', 4, 2)
print(res)


"""
定义一个函数
- 接收参数 num 和 command
- command 为 True 则返回0-n(包含n)以内的偶数组成的列表
- command 为 False 则返回0-n(包含n)以内的奇数组成的列表
"""


def get_list(num, command):
    ret = []
    i = 0

    while i <= num:
        if command:
            # 生成0-num之间偶数组成的列表
            if i % 2 == 0:
                ret.append(i)
        else:
            # 生成0-num之间奇数组成的列表
            if i % 2 != 0:
                ret.append(i)

        i += 1

    return ret


res = get_list(10, True)
print(res)


res = get_list(10, False)
print(res)














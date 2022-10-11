"""
while 条件:
    # 需要重复执行的代码
else:
    # 写代码，当循环代码结束【但不是因为break结束时】，循环的else部分的代码才会执行
"""

i = 0

while i < 10:
    print('跑步%d圈' % (i+1))
    # i向上增加1
    i += 1

    if i ==5 :
        print('休息一下')
        break
else :
    print('休息一下')
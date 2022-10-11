"""
break：跳出循环（终止循环），结束循环代码的执行
continue：本次循环 continue 之后的代码不再执行，直接重新执行循环代码
        跳过本次循环后续代码的执行，继续从循环开始准备执行下一次循环
"""

"""
break案例：
    需求：跑步10圈，跑5圈后，不再跑了
"""

i = 0

while i < 10:
    print('跑步%d圈' % (i+1))

    if i == 4:
        # 终止循环（强制结束循环）
        break

    # i向上增加1
    i += 1

print('while循环之后的代码')


"""
continue案例：
    需求：跑步10圈，到第5圈休息一下，第6圈继续
    
跑步1圈
跑步2圈
跑步3圈
跑步4圈
休息1圈
跑步6圈
跑步7圈
跑步8圈
跑步9圈
跑步10圈
"""

i = 0

while i < 10:
    if i == 4:
        print('休息1圈')
        i += 1
        continue

    print('跑步%d圈' % (i + 1))
    # i向上增加1
    i += 1

print('while循环之后的代码')


# 注意1：break和continue这两个关键字只能在循环内部使用！！！
# 注意2：break和continue只对离它最近的一层循环有效！！！


i = 1

while i <= 5:
    print('跑步 %d 圈' % i)

    if i == 3:
        # 这里的 break 终止的是外层循环
        break

    j = 1

    while j <= 5:
        print('做 %d 个俯卧撑' % j)

        if j == 2:
            # 这里的 break 终止的是内层循环
            break

        j += 1

    i += 1












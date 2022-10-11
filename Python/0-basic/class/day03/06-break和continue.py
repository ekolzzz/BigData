"""
break：跳出循环，结束循环代码的执行
continue：本次循环 continue 之后的代码不再执行，直接重新执行循环代码
"""

"""
break案例：
    需求：跑步10圈，跑5圈后，不再跑了
"""
#
# i = 0
#
# while i < 10:
#     print('跑步%d圈' % (i+1))
#     # i向上增加1
#     i += 1
#     if i == 5 :
#         break
#
# print('while循环之后的代码')


"""
continue案例：
    需求：跑步10圈，到第5圈休息一下，第6圈继续
"""

i = 0

while i < 10:
    print('跑步%d圈' % (i + 1))
    # i向上增加1
    i += 1
    if i == 5 :
        print('休息一下吧！')
        continue

print('while循环之后的代码')



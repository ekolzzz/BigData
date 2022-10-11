"""
循环语句的作用：就是让指定的一些代码重复执行

while 条件(判断是否满足条件):
    条件满足时，做的事情1
    ...(省略)...

注意：while 语句中的缩进部分是一个 独立的代码块
while 每次循序时，会先判断条件是否成立，只有成立才会执行循环操作，否则循环不再继续
"""

"""
案例：不停的打印：老婆，我错了！。
"""

# 无限循环（也叫死循环）：循环的条件永远为真
# while True:
#     print('老婆，我错了！')
#
# # 注意：无限循环后面的代码永远执行不到
# print('while循环之后的代码')

"""
指定次数的循环：让循环中的代码重复执行一定的次数之后，循环代码就不再重复了
案例演练：循环跑步10圈

代码效果：
跑步1圈
跑步2圈
跑步3圈
...
跑步10圈
"""

i = 1

# i=1, i<=10结果True
# i=2, i<=10结果True
# i=3, i<=10结果True
# i=4, i<=10结果True
# i=5, i<=10结果True
# i=6, i<=10结果True
# i=7, i<=10结果True
# i=8, i<=10结果True
# i=9, i<=10结果True
# i=10, i<=10结果True
# i=11, i<=10结果False
while i <= 10:
    print('跑步%d圈' % i)
    # 将 i 的值加1
    i += 1

print('while循环之后的代码')











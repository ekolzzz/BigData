"""
- 在控制台输出 秒表(如`11:13`, 每隔一秒, 时间更新一次)
- 使用time模块的sleep(秒数)函数可以让代码休眠指定的时间, 可以用此模拟计时
"""
import time

m = 0
while m < 60:  # 每分钟,需要执行60次分针移动
    s = 0
    while s < 60:  # 每秒钟,需要执行60次秒针移动
        print("%02d:%02d" % (m, s))
        time.sleep(1)
        s += 1
    m += 1


"""
* * * * *
* * * *
* * *
* *
*
"""

i = 5

while i > 0:
    j = 0
    while j < i:
        print('* ', end='')
        j += 1
    print()

    i -= 1















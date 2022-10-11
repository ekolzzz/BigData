"""
多线程的基本使用
学习目标：能够使用多线程同时执行两个不同的函数
"""

import time
# 导入线程模块
import threading


# 跳舞任务函数
def dance():
    for i in range(5):
        print('正在跳舞...%d' % i)
        time.sleep(1)


# 唱歌任务函数
def sing():
    for i in range(5):
        print('正在唱歌...%d' % i)
        time.sleep(1)


if __name__ == '__main__':
    # 创建两个子线程，一个执行 dance 函数，一个执行 sing 函数
    dance_thread = threading.Thread(target=dance)
    sing_thread = threading.Thread(target=sing)

    # 启动子线程
    dance_thread.start()
    sing_thread.start()

# 注意：上面的代码执行之后，
# 一个进程中有3个线程，一个主线程（负责执行 main 里面的代码，将两个子线程创建出来），两个子线程

"""
进程执行带有参数的任务(函数)
学习目录：能够使用多进程执行带有参数的任务
"""

import multiprocessing
import time


# 带有参数的任务(函数)
def task(count):
    for i in range(count):
        print('任务执行中...')
        time.sleep(0.2)
    else:
        print('任务执行完成')


if __name__ == '__main__':
    # 创建一个子进程，让它执行 task 函数
    # 通过 args 以元祖的形式给进程执行的任务函数传参
    # sub_process = multiprocessing.Process(target=task, args=(3,))
    # 通过 kwargs 以字典的形式给进程执行的任务函数传参
    sub_process = multiprocessing.Process(target=task, kwargs={'count': 5})

    # 启动子进程
    sub_process.start()


"""
守护进程和终止子进程
学习目标：能够设置守护进程和终止子进程
"""

"""
如何让主进程执行结束时，子进程就结束执行？
方式1：将子进程设置为守护进程：皇帝（主进程）死了，臣子（子进程）不再苟活
方式2：主进程结束时直接终止子进程：君要臣死，臣不得不死
"""

import multiprocessing
import time


# 方式1：将子进程设置为守护进程

# 任务函数
def task():
    for i in range(10):
        print('任务执行中...')
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子进程并启动
    sub_process = multiprocessing.Process(target=task)
    # TODO：设置子进程为守护进程
    sub_process.daemon = True # 注意：设置必须在 start 之前
    sub_process.start()

    # 主进程延时 1s
    time.sleep(1)
    print('主进程结束！')


# 方式2：主进程结束时直接终止子进程

import multiprocessing
import time


# 任务函数
def task():
    for i in range(10):
        print('任务执行中...')
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子进程并启动
    sub_process = multiprocessing.Process(target=task)
    sub_process.start()

    # 主进程延时 1s
    time.sleep(1)
    print('主进程结束！')
    # TODO: 终止子进程
    sub_process.terminate()
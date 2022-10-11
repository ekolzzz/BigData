"""
多进程的基本使用
学习目标：能够使用多进程同时执行两个不同的任务函数
"""
import time
# 导入进程包
import multiprocessing #


# 跳舞函数
def dance():
    for i in range(5):
        print('跳舞中...')
        time.sleep(1)


# 唱歌函数
def sing():
    for i in range(5):
        print('唱歌中...')
        time.sleep(1)


if __name__ == '__main__':
    # 创建两个进程，分别执行 dance 和 sing 这俩函数
    # target参数：指定创建的进程要执行什么函数
    dance_process = multiprocessing.Process(target=dance)
    sing_process = multiprocessing.Process(target=sing)

    # 启动进程
    # 注意：这里的 start 启动进程只是说明进程的代码可以执行了，但是什么执行还是要看CPU
    dance_process.start()
    sing_process.start()

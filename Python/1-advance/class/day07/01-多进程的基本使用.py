"""
多进程的基本使用
学习目标：能够使用多进程同时执行两个不同的任务函数
"""
import time
# 导入进程包
import multiprocessing # 多处理


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

if __name__ == '__main__' : # 注意：这样做的目的是，其他模块导入该模块时，被导入模块中的测试代码不会被执行
    # 创建两个进程，分别执行 dance 和 sing 函数
    # target参数：指定创建的进程要执行什么函数
    dance_process = multiprocessing.Process(target=dance) # 指定进程执行 dance 函数
    sing_process = multiprocessing.Process(target=sing) # 指定进程执行 sing 函数

    # 启动进程
    # 注意：start 启动进程只是说明进程的代码可以执行了，具体执行由 CPU 调度
    dance_process.start()
    sing_process.start()



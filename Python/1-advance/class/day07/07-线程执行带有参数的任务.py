"""
线程执行带有参数的任务(函数)
学习目录：能够使用多线程执行带有参数的任务
"""
# 导入线程模块
import threading
import time


# 带有参数的任务(函数)
def task(count):
    for i in range(count):
        print('任务执行中...')
        time.sleep(0.2)
    else:
        print('任务执行完成')

if __name__ = '__main__':
    # 创建一个子进程，让它执行 task 函数
    # 通过 arg 参数以元组的形式给任务函数传递参数
    # sub_thread = threading.Thread(target=task, args=(5,))
    # 通过 kwarg 参数以字典的形式给任务函数传递参数
    sub_thread = threading.Thread(target=task, kwarg = {'count' : 5})
    sub_thread.start()
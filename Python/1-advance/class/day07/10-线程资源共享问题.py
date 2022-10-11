"""
线程资源共享问题
学习目标：能够使用线程等待vs互斥锁解决线程资源共享问题
"""

"""
多线程会共享全局变量，当多个线程同时操作同一个共享的全局变量时，可能会造成错误的结果！
"""

# import threading
#
# # 定义全局变量/***/
# g_num = 0
#
#
# def sum_num1():
#     global g_num
#     # 循环一次给全局变量加1
#     for i in range(1000000):
#         g_num += 1
#
#     print('sum1：', g_num)
#
#
# def sum_num2():
#     global g_num
#     # 循环一次给全局变量加1
#     for i in range(1000000):
#         g_num += 1
#
#     print('sum2：', g_num)
#
#
# if __name__ == '__main__':
#     # 创建两个线程
#     first_thread = threading.Thread(target=sum_num1)
#     second_thread = threading.Thread(target=sum_num2)
#
#     # 启动两个线程
#     first_thread.start()
#     second_thread.start()


"""
如何解决线程资源共享出现的错误问题？
答：线程同步：保证同一时刻只能有一个线程去操作全局变量

线程同步的方式：
1）线程等待(join) ： 强制等待一个线程执行结束以后，再去执行另外的线程
2）互斥锁：多个线程去抢同一把"锁"，抢到锁的线程执行，没抢到锁的线程会阻塞等待
"""

# 线程等待(join)：等待一个线程执行结束之后，代码再继续执行，同一时刻只有一个线程执行
# import threading
#
# # 定义全局变量
# g_num = 0
#
#
# def sum_num1():
#     global g_num
#     # 循环一次给全局变量加1
#     for i in range(1000000):
#         g_num += 1
#
#     print('sum1：', g_num)
#
#
# def sum_num2():
#     global g_num
#     # 循环一次给全局变量加1
#     for i in range(1000000):
#         g_num += 1
#
#     print('sum2：', g_num)
#
#
# if __name__ == '__main__':
#     # 创建两个线程
#     first_thread = threading.Thread(target=sum_num1)
#     second_thread = threading.Thread(target=sum_num2)
#
#     # 启动两个线程
#     first_thread.start()
#     # 线程等待：等待 first_thread 执行完成，主线程的代码再继续向下执行
#     first_thread.join()
#     second_thread.start()

# 互斥锁：多个线程去抢同一把"锁"，抢到锁的线程执行，没抢到锁的线程会阻塞等待
import threading

# 定义全局变量
g_num = 0

lock = threading.Lock()


def sum_num1():
    global g_num
    # 循环一次给全局变量加1
    for i in range(1000000):
        # 尝试抢锁：抢到锁可以继续执行，否则阻塞等待
        lock.acquire()
        g_num += 1
        # 释放锁
        lock.release()
    print('sum1：', g_num)


def sum_num2():
    global g_num

    # 循环一次给全局变量加1
    for i in range(1000000):
        # 尝试抢锁：抢到锁可以继续执行，否则阻塞等待
        lock.acquire()
        g_num += 1
        # 释放锁
        lock.release()
    print('sum2：', g_num)


if __name__ == '__main__':
    # 创建两个线程
    first_thread = threading.Thread(target=sum_num1)
    second_thread = threading.Thread(target=sum_num2)

    # 启动两个线程
    first_thread.start()
    second_thread.start()

# 注意：互斥锁可以保证线程代码同时执行的前提下解决资源共享问题，但是加锁、释放锁会浪费一下时间！！！

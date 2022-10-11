# list = ['a','b','c','d']
# for i in list :
#     print(i)

# ret = 1
# i = 1
# while i <= 100 :
#     ret *= i
#     i += 1
# print('1*2*……*100的乘积为:%d' % ret)

# i = 1
# sum = 0
#
# while i <= 100 :
#     print(i)
#
#     if i % 2 == 1 :
#         sum += i
#
#     i += 1
#
# print('1~100的奇数之和是:%d' % sum)

# i = 1
#
# while i <=100 :
#   if i % 7 != 0 :
#     print(i)
#   i += 1

# i = 1
#
# while i <= 100:
#   if i % 7 != 0:
#     print(i)
#   else:
#     print('哈~')
#   i += 1

# i = 0
# while i < 100:
#     i+=1
#     if i % 7 == 0:
#         print("哈~")
#         continue
#     print(i)

# i = 0
# while i < 100:
#   i += 1
#   if i % 7 == 0:
#     print('哈~')
#     continue # continue 某一条件满足时，不再执行本次循环体中后续重复的代码，但进入下一次循环判断
#   print(i)

# i = 0
# while i < 9:
#   i += 1
#   print('第%d次外循环' % i)
#   j = 0
#   while j < 9:
#     j += 1
#     if j == 4 :
#       print()
#       break
#     print('第%d次内循环' % j)

# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print("i=%d, j=%d  " % (i, j))
#         if j == 4:
#             break  # 内循环 break，外循环可以正常结束
#         j += 1
#     i += 1

# a = [11, 22, 33]
#
# # 获取列表的元素 22
# ret = a[1]
# print(ret)
#
# # 向列表中添加（增）新元素44
# # a.append(44)
# #
# # a.insert(3,44)
# #
# b = [44,11,11]
# a.extend(b)
#
# print(a)
#
# # 删除（删）列表中的元素 33
# a.remove(33)
#
# # del a[2]
#
# # a.pop(2)
#
# # a.clear() #清空列表
#
# print(a)
#
# # 修改（改）列表中的元素 22 为 55
# a[1] = 55
# print(a)
#
# # 查找（查）列表中的元素 55 的下标
# index = a.index(55)
# print(index)
#
# # 列表长度(元素个数)
# print(len(a))
#
# # 判断列表中是否包含某个值
# if 11 in a :
#     print('元祖a里有11')
#
# #	判断列表中是否包含某个值
# print(a.count(11))
#
# # 排序
# a.sort() #升序
# print(a)
#
# a.sort(reverse=True) #降序
# print(a)
#
# a.reverse() #降序
# print(a)

import time

h = 0

while h < 24 :
    m = 0
    while m < 60 :
        s = 0
        while s < 60 :
            print('现在时间是: %02d:%02d:%02d' % (h, m, s))
            time.sleep(1)  # 代表休眠1秒
            s += 1
        m += 1
    h += 1

# import time
#
# m = 0
# while m < 60:  # 每小时,需要执行60次分针移动
#     s = 0
#     while s < 60:  # 每分钟,需要执行60次秒针移动
#         print("%02d:%02d" % (m, s))
#         time.sleep(1)
#         s += 1
#     m += 1

# i = 5
#
# while i >= 1:
#   j = 1
#   while j <= i:
#     print('*', end='')
#     j += 1
#   print()
#   i -= 1
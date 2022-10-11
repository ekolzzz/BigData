# list1 = [11, 45, 34, 51, 90]
# list2 = [4, 16, 23, 0]
#
# list = list(set(list1 + list2))
#
# # 升序
# # list.sort()
#
# # 降序
# # list.sort(reverse= True)
# list.reverse()
#
# print(list)

# def max(a, b) :
#     if a > b :
#         max = a
#     else:
#         max = b
#     return max
#
# a = int(input('请输入一个数：'))
# b = int(input('请输入另一个数：'))
#
# print(max(a, b))

# while True :
#     print('============闰年查询器============')
#     year = int(input('请输入要查询的年份：'))
#
#     def leap_year(year) :
#         if year % 4 == 0 and year % 100 != 0 :
#             print(year, '是闰年')
#
#         else:
#             print(year, '不是闰年')
#
#     leap_year(year)

# def sum(num1, num2):
#   """计算两数之和"""
#   sum = num1 + num2
#   return sum
#
# num1 = int(input('请输入一个数：'))
# num2 = int(input('请输入另一个数：'))
#
# my_sum = sum(num1, num2)
#
# print()
# if my_sum <= 10:
#   print('%d+%d=%d' % (num1, num2, my_sum))
# else:
#   print('超过10的加法太难了')

# def my_fun(list, a, b, c):
#     if a+b > c:
#         print(list, '可以组成三角形')
#     else:
#         print(list, '不可以组成三角形')
#
# while True :
#     print('==============三角形判断器==============')
#
#     i = 1
#     list = []
#
#     while i <= 3 :
#         list.append(int(input('请输入第%d个数：' % i)))
#         i +=1
#
#     list.sort() # 升序，确定大小：list[0]<list[1]<list[2]
#
#     my_fun(list,list[0],list[1],list[2])

#      012345678
# s = "123456789", a1 = 2, a2 = 4 结果为: "12789"
# def my_task(str, a1, a2):
#     str1 = str[:a1+1]
#     str2 = str[a1+a2:]
#     my_str = str1 + str2
#     return (my_str)
#
# str = input('请输入一个字符串：')
# a1 = int(input('请输入数值1：'))
# a2 = int(input('请输入数值2：'))
#
# print(my_task(str, a1, a2))

def my_task(num, com):
    i = 0
    list = []

     #如果命令为True,则输出偶数
    while i <= num :
        if com:  # 返回偶数
            if i % 2 == 0:
                list.append(i)
        else:  # 返回奇数
            if i % 2 != 0:
                list.append(i)
        i += 1

    return list

while True :
    num= int(input('请输入num:'))
    com= input('请输入command:')

    print(my_task(num, com))

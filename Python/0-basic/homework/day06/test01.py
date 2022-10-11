# test = 'a', 'b', 'c'
# print(type(test), test)
#
# test_0 = 1, 2, 3
# print(type(test_0), test_0)

# a, b, c = (1, 2, "3") # 本质上是一个元组
# print(type(a), a, type(b), b, type(c), c)

# num = [1,1,2,3,4,4,5]
# print([i for i in list(set(num)) if i % 2 != 0])

# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)
#
# odd_list = [i for i in range(1, 101) if i % 2 != 0] # 脱裤子放屁了属于是
# print(odd_list)
#
# odd_sum = 0
#
# for j in odd_list:
#     odd_sum += j
# print(odd_sum)

# for i in range(1, 6):
#     print('*' * i)

# my_list = [i for i in range(1, 101) if i % 4 ==0]
# print(my_list)

for i in range(1, 10):
    for j in range (1, i+1):
        print(f'{i}*{j}={i*j}', end=" ")
    print()


# for i in range(1, 10):
#   for j in range(1, i+1):
#     print("%d*%d=%d  " % (i, j, i*j), end=" ")
#   print()

# import time
# sentence = "谭 妙, I love you forever!"
# for char in sentence.split():
#    allChar = []
#    for y in range(12, -12, -1):
#        lst = []
#        lst_con = ''
#        for x in range(-30, 30):
#             formula = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
#             if formula <= 0:
#                 lst_con += char[(x) % len(char)]
#             else:
#                 lst_con += ' '
#        lst.append(lst_con)
#        allChar += lst
#    print('\n'.join(allChar))
#    time.sleep(1)

# 在PyCharm中拷贝下面代码, 尝试读懂下面的写法

# 思考: 为什么使用do函数中的action(), 但是调用了eat函数

# 1. 函数名, 其实也是一个变量, 也会有id地址
def eat():
    print(id(eat), "吃东西")

def drink():
    print(id(drink), "喝东西")

# 2. 只要是变量, 就可以传参, 因此, 函数名可以当做参数传递
def do(action):
    # 3. 只要id相同, 就说明是同一个函数
    print(id(action))
    # 4. 函数名+()就是函数调用
    action()

# 5. 想调用哪个函数, 就传递函数名.
do(eat)  # 这样的写法有助于扩充程序功能. 增加了其他方法后, 调用方法不用变
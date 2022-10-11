# a = 2
# b = 1
#
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
#
#
# name = 'TOM'
# age = 18
# weight = 66.6
# print('用户姓名：%s，年龄：%d，体重：%0.1f' % (name, age, weight))

# name = input('请输入用户名：')
# password = input('请输入密码：')
# print('您输入的用户名是：%s' % name )
# print('您输入的密码是：%s' % password )

# num1 = float(input('请输入一个数：'))
# num2 = float(input('请输入另一个数：'))
# print('%.2f+%.2f=%.2f' % (num1, num2, (num1+num2)))

# name = input('请输入姓名：')
# sex = input('请输入性别：')
# age = int(input('请输入年龄：'))
# company = input('请输入单位：')
# tel = input('请输入联系方式：')
#
# print('**********************************************')
# print('*','姓名：%s ' % name )
# print('*','性别：%s' % sex )
# print('*','年龄：%d' % age )
# print('*','姓名：%s' % company )
# print('*','姓名：%s' % tel )
#
# print('**********************************************')


# age = int(input('请输入自己的年龄：'))
#
# if age >= 18:
#     print('允许上网')
#
# elif age >= 17:
#     print('过两天再来上网')
#
# elif age >= 12:
#     print('存两年钱再来上网')
#
# else:
#     print('小屁孩还敢来网吧,一会告诉你妈去')

# day = int(input('请输入日期(1-7):'))
#
# if day == 6 or day == 7:
#     print('周末')
#
# else:
#     print('工作日')


# age = int(input('请输入年龄:'))
#
# if age >= 60 and age <= 99 :
#     age = '老年'
#
# elif age >=36 :
#     age = '中年'
#
# elif age >= 18 :
#     age = '青年'
#
# else:
#     age = '青少年'
#
# print('您的年龄是%s' % age )

# num1, num2, num3 = input('输入三个数,空格隔开:').split()
#
# sum = int(num1) + int(num2) + int(num3)
#
# if sum > 100000:
#     print('**"您输入的三个数的和忒大了"**')
# elif sum > 10000:
#     print('**"您输入的三个数的和挺大"**')
# elif sum > 1000 :
#     print('**"您输入的三个数的和有点大"**')
# elif sum > 100 :
#     print('输出**"您输入的三个数的和不算大"**')
# else:
#     print('**"您输入的三个数的和忒小了"**')

# ticket取值为1表示有票，取值为0表示无票
# ticket = int(input('有无车票【1/0】：'))
# seat取值为1表示有座位，取值为0表示无座位


# if ticket == 1 :
#     print('有票请上车！')
#     seat = int(input('看车上有无车位【1/0】：'))
#     if seat == 1 :
#         print('有座位，请坐下！')
#     else :
#         print('没有座位，请站着！')
# else :
#     print('请先买票再上车！')

# print('***************BMI指数*****************')
# print('低于18.5：过轻')
# print('18.5 - 25：正常')
# print('25 - 28：过重')
# print('28 - 32：肥胖')
# print('高于32：严重肥胖')
# print('****************************************')
#
# height = float(input('请输入你的身高(m):'))
# weight = float(input('请输入你的体重(kg):'))
#
# BIM = weight / height**2
# if BIM >32 :
#     Health = '严重肥胖'
# elif BIM >=28 :
#     Health = '肥胖'
# elif BIM >= 25:
#     Health = '过重'
# elif BIM >= 18.5:
#     Health = '正常'
# else :
#     Health = '过轻'
# print('您的BIM指数是:%.1f,%s' % (BIM,Health))

# # 已知A用户注册的用户名为`aaa`，密码是`123456`
# A_name = 'aaa'
# A_password = '123456'
#
# # 固定验证码为`qwer`
# code = 'qwer'
#
# # 获取登录时用户名、密码、验证码
# login_name = input('请输入用户名:')
# login_password = input('请输入密码:')
# login_code = input('请输入验证码:')
#
# # 系统先验证验证码是否正确，正确后再验证用户名和密码
# while login_code != 'qwer' :
#         print('验证码错误,请重新输入!')
#         login_code = input('请输入验证码:')
#
# if login_name == A_name and login_password == A_password :
#     print('登录成功')
# else:
#     print('用户名或密码错误,请重新登录!')

# a =3
# b =40
# max = (a if a>b else b)
# print(max)

# yue = int(input('请输入银行卡的余额:'))
# jine = int(input('请输入要付款的金额:'))
#
# deal = '使用银行卡付款，付款成功！' if yue >= jine else '余额不足,付款失败！'
# print(deal)

# print('*************简易计算器*************')
# num1 = int(input('请输入第一个数字：'))
# symbol = input('请输入操作符[+、-、*、/]：')
# num2 = int(input('请输入第一个数字：'))
#
# if symbol == '+' :
#     result = num1 + num2
#     print('%d + %d = %d' % (num1, num2, result))
# elif symbol == '-' :
#     result = num1 - num2
#     print('%d - %d = %d' % (num1, num2, result))
#
# elif symbol == '*' :
#     result = num1 * num2
#     print('%d * %d = %d' % (num1, num2, result))
#
# elif symbol == '/' :
#     result = num1 / num2
#     print('%d / %d = %d' % (num1, num2, result))
# print('*************简易计算器  *************')

year = int(input('请输入年份：'))

if year % 4 == 0 and year % 100 != 0 :
    print('%d是闰年' % year)
else:
    print('%d不是闰年' % year)
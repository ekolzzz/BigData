"""20、接收用户输入的账号和密码，如果账号为'admin'，密码为'admin888'，则提示用户登录成功，
其他情况则提示用户名或密码输入错误，只有3次输入机会。"""

name = 'admin'
pwd = 'admin888'

i = 1

# 只有3次输入机会
while i <=3 :
    login_name = input('请输入用户名：') # 提示用户输入用户名
    login_pwd = input('请输入密码：') # 提示用户输入密码

    if name == login_name and pwd == login_pwd : # 只有当用户名和密码都相同时，提示登录成功
        print('登录成功！')
        break

    else: # 当用户名或密码不相同时，提示用户名或密码输入错误，请重新输入！
        print('用户名或密码输入错误，请重新输入！')

    i += 1 # 每判断一次i会加1次

else: # 只有当while不是被break终止循环的时候才会执行else的语句
    print('输入次数过多，请稍后尝试！')
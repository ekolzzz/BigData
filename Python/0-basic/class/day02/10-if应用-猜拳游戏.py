"""
需求：
① 从控制台输⼊要出的拳 —— ⽯头（1）／剪⼑（2）／布（3）
② 电脑 随机 出拳 —— 先假定电脑只会出⽯头，完成整体代码功能
③ ⽐较胜负
"""
# 从控制台输⼊要出的拳 —— ⽯头（1）／剪⼑（2）／布（3）
user = int(input('输⼊要出的拳 —— ⽯头（1）／剪⼑（2）／布（3）:'))
if user == 1 :
    user_out = '⽯头'
elif user == 2 :
    user_out = '剪刀'
else :
    user_out = '布'
print('用户出的是:%s' % user_out)

# ② 电脑 随机 出拳 —— 先假定电脑只会出⽯头，完成整体代码功能
import random
computer = random.randint(1,3)
if computer == 1 :
    computer_out = '⽯头'
elif computer == 2 :
    computer_out = '剪刀'
else :
    computer_out = '布'
print('电脑出的是:%s' % computer_out)

# ③ ⽐较胜负

# 玩家赢:
# 1----user ==1 and computer == 2
# 2----user ==2 and computer ==3
# 3----user ==3 and computer ==1
if (user ==1 and computer == 2) or (user ==2 and computer ==3) or (user ==3 and computer ==1) :
    print('电脑弱爆了!')
# 平局:
# user == computer

elif user == computer :
    print('心有灵犀一点通')

# 电脑赢
else:
    print('决战到天亮!')


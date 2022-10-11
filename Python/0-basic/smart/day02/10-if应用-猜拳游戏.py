"""
需求：
① 从控制台输⼊要出的拳 —— ⽯头（1）／剪⼑（2）／布（3）
② 电脑 随机 出拳 —— 先假定电脑只会出⽯头，完成整体代码功能
③ ⽐较胜负

假设用户输入的数字使用 user 变量保存，电脑出的数字使用 computer 变量保存。

比较胜负有几种情况：
1）用户赢（电脑输）
    情况1：user == 1 and computer == 2
    或
    情况2：user == 2 and computer == 3
    或
    情况3：user == 3 and computer == 1
2）平局
    user == computer
3）用户输（电脑赢）
    只要不是用户赢，也不是平局，那么一定是用户输
"""

# ① 从控制台输⼊要出的拳 —— ⽯头（1）／剪⼑（2）／布（3）
user = int(input('请输入⽯头（1）／剪⼑（2）／布（3）:'))
print('用户出：%d' % user)

# ② 电脑 随机 出拳 —— 先假定电脑只会出⽯头，完成整体代码功能
# computer = 1 # 后面再来改造这个代码，让电脑随机出1-3之间的一个数字
import random
computer = random.randint(1, 3)
print('电脑出：%d' % computer)

# ③ ⽐较胜负
if (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
    # 用户赢，打印：电脑弱爆了！
    print('电脑弱爆了！')
elif user == computer:
    # 平局，打印：心有灵犀，再来一局！
    print('心有灵犀，再来一局！')
else:
    # 用户输，打印：不要走，决战到天亮！
    print('不要走，决战到天亮！')




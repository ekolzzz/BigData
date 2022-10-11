"""19、定义一个字符串，如str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"。
编写一个程序，使用随机数从字符串中抽取4个字符，用于生成验证码。"""
import random # 导入random模块

str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = len(str1) # 获取字符串长度

i = 1
new_str1 = '' # 定义一个空字符串

while i <= 4:
    new_str1 += str1[random.randint(0, res-1)] # 通过下标，随机获取str1里的字符，并添加到new_str1里
    i += 1
    
print(f'验证码是：{new_str1}')
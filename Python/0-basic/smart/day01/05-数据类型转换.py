age = "18"
# TypeError: can only concatenate str (not "int") to str
# 原因：age是字符串类型，字符串不能和整数类型进行相加
# print(age + 1)
print(int(age) + 1)

"""
数据类型转换的函数：
* int(x)：把 x 转换为一个整数
* float(x)：把 x 转换为一个小数
* str(x)：把 x 转换为一个字符串

注意：我们在进行类型转换时，这个转换应该是合理的，否则会报错！！！
"""

"""
int(x)：把 x 转换为一个整数
"""
# 把字符串转换为整数
str1 = "10"
print(type(str1), str1)

num1 = int(str1)
print(type(num1), num1)

# 把小数转换为整数
# 注意：把小数转换为整数时，它是只取整数部分
num2 = 10.6
print(type(num2), num2)

num3 = int(num2)
print(type(num3), num3)

# 注意：不能把看起来像小数的字符串直接转换为整数
# str2 = "20.5"
# # ValueError: invalid literal for int() with base 10: '20.5'
# num4 = int(str2)

print('==============================================')

"""
float(x)：把 x 转换为一个小数
"""

# 将字符串转换成小数
str2 = "20.5"
print(type(str2), str2)

num5 = float(str2)
print(type(num5), num5)

# 将整数转换为小数
num6 = 10
print(type(num6), num6)

num7 = float(num6)
print(type(num7), num7)

print('==============================================')

"""
str(x)：把 x 转换为一个字符串
"""
# 将整数转换为字符串
num8 = 10
print(type(num8), num8)

str3 = str(num8)
print(type(str3), str3)

# 将小数转换为字符串
num9 = 10.3
print(type(num9), num9)
str4 = str(num9)
print(type(str4), str4)

# 演示不合理的类型转换
# str5 = "abc"
# num10 = int(str5)








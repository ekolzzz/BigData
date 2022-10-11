"""
需求：假如有两个数字：a 和 b，通过程序计算 a 和 b 中的最大值
"""

"""
三目运算符(也叫三元运算符)：if...else语句的简写

语法：表达式1 if 条件 else 表达式2
"""

# 思路
# 判断输入的两个数中较大的数
a = int (input('请输入一个数:'))
b = int (input('请输入另一个数:'))

max = (a if a > b else b)   #三目运算符(也叫三元运算符)
print(max)
"""
if a > b :
    max = a
else :
    max = b

print(max)
"""

max = (a if a > b else b)   #三目运算符(也叫三元运算符)
print(max)














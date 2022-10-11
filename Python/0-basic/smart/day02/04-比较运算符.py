"""
==	检查两个操作数的值是否相等，如果是则条件变为真。	如a=3,b=3，则（a == b) 为 True
!=	检查两个操作数的值是否相等，如果值不相等，则条件变为真。	如a=1,b=3，则(a != b) 为 True
>	检查左操作数的值是否大于右操作数的值，如果是，则条件成立。	如a=7,b=3，则(a > b) 为 True
<	检查左操作数的值是否小于右操作数的值，如果是，则条件成立。	如a=7,b=3，则(a < b) 为 False
>=	检查左操作数的值是否大于或等于右操作数的值，如果是，则条件成立。	如a=3,b=3，则(a >= b) 为 True
<=	检查左操作数的值是否小于或等于右操作数的值，如果是，则条件成立。	如a=3,b=3，则(a <= b) 为 True
"""

num1 = 15
num2 = 20

# == 等于：表示左右两个操作数是否相等
print(num1 == num2) # False

# != 不等于
print(num1 != num2) # True

# > 大于
print(num1 > num2) # False

# < 小于
print(num1 < num2) # True

# >= 大于等于: num1 大于 或者 等于 num2 ，条件都成立
print(num1 >= num2) # False

# <= 小于等于： num1 小于 或者 等于 num2 ，条件都成立
print(num1 <= num2) # True

# 注意：
# 一定要区别 = 和 ==
# =：赋值运算符，表示把=号右边的结果赋值给=号左边的变量
# ==：比较运算符，判断 == 两边的数据是否相等，结果是一个bool值


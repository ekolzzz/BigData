"""
变量：可变的量，在程序中存储数据的容器
语法：
    变量名 = 值
注意：首次是定义一个变量，再操作就是修改变量的值
"""

# # 定义一个变量，名字叫：num，存储的数据是数字：10
# num = 10
# # 打印一个变量的值
# # 注意：打印变量时，千万不要在变量名的两边添加引号
# # print('num')
# print(num)
#
# # 修改 num 变量存储的数据，改成：250
# num = 250
# print(num)



"""
数据类型：根据变量存储数据的不同，变量分为不同的类型
int：整型
float：浮点型（小数类型）
bool：布尔类型，只要两种值：True或False，如果存储的数据只要两种可能，可以使用bool类型
str：字符串类型（文本类型），数据两边必须添加引号（单引号或双引号都可以）

函数：
type(变量或数据)：获取变量或数据的类型
"""

# 需求：定义变量存储一个人的姓名、年龄、性别、身高。
# 姓名
name = "小明"
# <class 'str'>
print(type(name))
print(name)
# 年龄
age = 18
# <class 'int'>
print(type(age))
print(age)
# 性别
gender = True # True表示男，False表示女
# <class 'bool'>
print(type(gender))
print(gender)
# 身高
height = 1.83
# <class 'float'>
print(type(height))
print(height)

print("=========================================")


# 思考题：以下变量都是什么数据类型？
a = 3.14 # float
print(type(a))
b = 10 # int
print(type(b))
c = 'True' # str
print(type(c))
d = '20' # str
print(type(d))
e = True # bool
print(type(e))













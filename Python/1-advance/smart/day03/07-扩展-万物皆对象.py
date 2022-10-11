"""
万物皆对象：在 python 中，所有的东西其实都是"对象"
"""
print('=================================== 基础类型 ======================================')
# int、float、bool
# 其实这个 num1 就是一个 int 类的实例对象，int 是 python 一个内置的类
num1 = 10
# <class 'int'>
print(type(num1), num1)

# 其实这个 num2 就是一个 float 类的实例对象，float 是 python 一个内置的类
num2 = 10.5
# <class 'float'>
print(type(num2), num2)

# 其实这个 gender 就是一个 bool 类的实例对象，bool 是 python 一个内置的类
gender = True
# <class 'bool'>
print(type(gender), gender)

print('=================================== 容器类型 ======================================')
# list、dict、tuple、set、str

# 其实这个 my_list 就是一个 list 类的实例对象，list 是 python 一个内置的类
my_list = [1, 2, 3]
# <class 'list'>
print(type(my_list), my_list)

print('=================================== 函数类型 ======================================')


# 注意：函数名其实就是 function 这个类的实例对象
def my_sum(a, b):
    return a + b


# <class 'function'>
print(type(my_sum), my_sum)

print('=================================== 类 ======================================')


# 注意：类名其实一个 type 类的实例对象
class Dog(object):
    """狗类"""
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age


# <class 'type'>
print(type(Dog), Dog)

# <class '__main__.Dog'>
dog1 = Dog('大黄', 2)
print(type(dog1), dog1)











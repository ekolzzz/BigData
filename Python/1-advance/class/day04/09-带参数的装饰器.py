"""
带有参数的装饰器
学习目标：能够写出带有参数的装饰器
"""

"""
需求：定义一个装饰器 log，装饰下面的两个函数，实现调用上面两个函数时进行日志信息记录的功能，将调用信息记录到 record.log 文件中。
记录日志信息要求：xxx函数被调用了，比如：login函数被调用了
"""
def log(func):

    # 注意： wrapper 小括号里面的 *args 和 **kwargs  代表是两种不定长形参
    def wrapper(*args, **kwargs): # 形参

        # 注意：调用func 时，小括号里面的 *args 和 **kwargs 代表的是拆解传实参
        result = func(*args, **kwargs) # 传递实参
        with open('./record.log', 'a', encoding='utf8') as f:
            f.write(f'{func.__name__}函数被调用\n')

        return result

    return wrapper

@log
def login():
    print("用户登录逻辑")

@log
def register():
    print("用户注册逻辑")

login()
register()

"""
在上面代码的基础上，如果还想实现能够指定日志信息记录到哪个文件里，该怎么办？
比如：调用 login 函数时的信息记录到 login.log 中
比如：调用 register 函数时的信息记录到 register.log 中

答： 需要使用带有参数的装饰器；
1）带有参数的装饰器就是使用装饰器装饰函数的时候可以传入指定参数，语法格式: @装饰器(参数,...)

实现：在装饰器外面再包裹上一个函数，让最外面的函数接收参数，返回的是装饰器，因为@符号后面必须是装饰器实例。
"""
def logger(filename):
    def log(func):

        # 注意： wrapper 小括号里面的 *args 和 **kwargs  代表是两种不定长形参
        def wrapper(*args, **kwargs): # 形参

            # 注意：调用func 时，小括号里面的 *args 和 **kwargs 代表的是拆解传实参
            result = func(*args, **kwargs) # 传递实参
            with open(f'./{filename}', 'a', encoding='utf8') as f:
                f.write(f'{func.__name__}函数被调用\n')

            return result

        return wrapper
    return log

@logger('aaa.log')
def login():
    print("用户登录逻辑")

@logger('bbb.log')
def register():
    print("用户注册逻辑")

login()
register()




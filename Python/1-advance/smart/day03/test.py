"""
一个函数的返回值，可以是另一个函数
"""


def outer():
    # 调用外面这个函数时，只是把里面这个函数定义了出来，里面这个函数的代码并没有执行
    def inner():
        print('inner函数被调用')

    # 外面函数的返回值，是里面函数的名称
    return inner


func = outer()
func()

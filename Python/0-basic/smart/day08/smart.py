# 在 smart 模块中添加一个内置变量：__all__
__all__ = ['num', 'my_sum']


# 定义一个变量
num = 10


# 定义几个函数
def my_sum(a, b):
    """计算两个数字的和"""
    return a + b


def my_sub(a, b):
    """计算两个数字的差"""
    return a - b


# 直接运行这个模块的代码，__name__的值就是：'__main__'
# print('__name__内置变量的值为：', __name__)


# 给模块添加一下功能测试代码，来测试模块中代码是否正确，但是有一个需求：
# 添加的测试代码只在运行这个模块时执行；在其他地方导入这个模块时不执行。
if __name__ == '__main__':
    res = my_sum(1, 2)
    print(res)
    res = my_sub(3, 1)
    print(res)
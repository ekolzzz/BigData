
def make_average():
    nums = []

    def average(n): # 1. 函数嵌套(外部函数中定义了一个内部函数)
        # 只有对全局变量进行‘=’赋值才需要global
        nums.append(n) # 3. 内部函数使用了外部函数的变量(还包括外部函数的参数)
        return sum(nums)/len(nums)

    return average # 2. 外部函数返回了内部函数

func = make_average() # func = average

print(func(10)) # 结果：10.0
print(func(20)) # 结果：15.0
print(func(30)) # 结果：20.0


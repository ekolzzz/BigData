def make_average():
    nums = []

    def average(n):
        nums.append(n)
        return sum(nums)/len(nums)

    return average


func = make_average()

print(func(10)) # 结果：？？？
print(func(20)) # 结果：？？？
print(func(30)) # 结果：？？？


"""
引用：在 python 中，=号赋值的本质是引用，引用也可以理解一种指向，比如：a = 10，其实就是 a 引用(指向)了 10

id(数据)：可以使用 id 函数 查看变量的引用地址，如果引用地址相等，说明指向同一个内存空间：
注意：每一次运行程序，每次地址都可能不一样，因为每次运行程序时，数据在内存中的存储位置是不确定的
"""

# 如果引用地址相等，说明指向同一个内存空间
a = 10
print(id(a))

b =  a
print(id(b))


"""
python中函数传递参数都是引用传递
"""

num = 10000

def func(num1):
    print('func num1地址：', id(num1))

print('函数调用之前，num地址：', id(num))
func(num)
print('函数调用之后，num地址：', id(num))

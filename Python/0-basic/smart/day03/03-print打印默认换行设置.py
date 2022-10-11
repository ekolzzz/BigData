"""
print函数每一次打印了内容之后，会自动进行换行，涉及到print函数的一个参数end='\n'

可以自己设置 end 参数，这个参数的作用就是表示print每一次打印完成之后，紧接着要干什么，默认就是换行
"""

# \n：就表示换行符
print('hello world', end='\n')
print('你好！世界！', end='\n')
print('hello python', end='\n')

print('hello world', end='')
print('你好！世界！', end='')

print('hello world', end='$$$')
print('你好！世界！', end='999')
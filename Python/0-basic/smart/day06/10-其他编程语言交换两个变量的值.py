a = 10
b = 20

print(f'交换之前：a={a}, b={b}')
temp = a # temp = 10
a = b # a = 20
b = temp # b = 10
print(f'交换之后：a={a}, b={b}')

# 在不引人第三个变量的情况下，如何交换两个变量的值？
a = 10
b = 20

print(f'交换之前：a={a}, b={b}')
a = a + b # a = 30
b = a - b # b = 10
a = a - b # a = 20
print(f'交换之后：a={a}, b={b}')

for i
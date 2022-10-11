"""
str和bytes的互相转换
学习目标：知道str和bytes数据之间的互相转换
"""
# str -> bytes：str.encode('编码方式：默认utf8')
# bytes -> str：bytes.decode('解码方式：默认utf8')

my_str = '你好！中国！' # str
res = my_str.encode('utf-8')
print(type(res), res)

res1 = my_str.encode('gbk')
print(type(res1), res1)

str1 = res.decode('utf-8')
print(type(str1), str1)

str2 = res1.decode('gbk')
print(type(str2), str2)

str3 = res.decode('gbk')
print(type(str3), str3)

print('一条美丽的分割线'.center(50, '='))

str4 = res1.decode('utf-8')
print(type(str4), str4)




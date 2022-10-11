"""
str和bytes的互相转换
学习目标：知道str和bytes数据之间的互相转换
"""
# str -> bytes（编码）：str.encode('编码方式：默认utf8')
# bytes -> str（解码）：bytes.decode('解码方式：默认utf8')

my_str = '你好！中国！' # str
print(type(my_str), my_str)

print('================== 华丽的分割线 =================')
res1 = my_str.encode('utf8')
print(type(res1), res1)

res2 = my_str.encode('gbk')
print(type(res2), res2)

print('================== 华丽的分割线 =================')

bytes1 = b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x81\xe4\xb8\xad\xe5\x9b\xbd\xef\xbc\x81'
res3 = bytes1.decode('utf8')
print(type(res3), res3)

bytes2 = b'\xc4\xe3\xba\xc3\xa3\xa1\xd6\xd0\xb9\xfa\xa3\xa1'
res4 = bytes2.decode('gbk')
print(type(res4), res4)

# 注意：编码、解码的方式必须统一，否则可能会出现乱码或错误！！！
res5 = bytes1.decode('gbk')
print(type(res5), res5)

res6 = bytes2.decode('utf8')
print(type(res6), res6)
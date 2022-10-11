import copy
a = [[1, 2, 3], [4, 5, 6]]
b = a # b = [[1, 2, 3], [4, 5, 6]]
c = copy.copy(a) # 浅拷贝 c = [[1, 2, 3], [4, 5, 6]] c的一层地址是变了，即c[0],c[1] 改变了，但是c[0][0]
d = copy.deepcopy(a) # 深拷贝
a.append(7)
a[1][2] = 0

print('原列表：', a)
print('引用赋值：', b)
print('浅拷贝：', c) # 只修改第一层
print('深拷贝：', d)
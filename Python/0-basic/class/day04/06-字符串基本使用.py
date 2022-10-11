"""
字符串：python中用来存储一段文本数据的类型，可以用单引号，双引号和三引号进行定义
"""

# 单引号字符串
name1 = 'smart'
print(type(name1), name1)


# 双引号字符串
name2 = "smart"
print(type(name2), name2)


# 打印出：I'm a smart boy

print('I\'m a smart boy')

# 打印出：鲁迅说:"学IT，来黑马程序员"
print('鲁迅说:"学IT，来黑马程序员"')

# 三引号用来定义多行字符串
"""
春有百花秋有月，
夏有凉风冬有雪，
若无闲事挂心头，
便是人间好时节。
"""

print("""
春有百花秋有月，
夏有凉风冬有雪，
若无闲事挂心头，
便是人间好时节。
""")

print('春有百花秋有月，\n夏有凉风冬有雪，\n若无闲事挂心头，\n便是人间好时节。')


"""
字符串可以通过下标获取指定位置的字符
字符串可以遍历获取其中的每个字符
"""

#         01234
my_str = 'hello'

# 字符串不能被修改
print(my_str[2])


# 字符串的遍历
for c in my_str :
    print(c)

# 判断某个字符是否在字符串内
if 'e' in my_str :
    print('e在字符串里')
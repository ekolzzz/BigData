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
print("I'm a smart boy")
# \：反斜杠在 python 叫转义符，\'就表示这个'就是一个普通的单引号，不具有特殊含义
print('I\'m a smart boy')

# 打印出：鲁迅说:"学IT，来黑马程序员"
print('鲁迅说:"学IT，来黑马程序员"')
print("鲁迅说:\"学IT，来黑马程序员\"")

# 三引号用来定义多行字符串
"""
春有百花秋有月，
夏有凉风冬有雪，
若无闲事挂心头，
便是人间好时节
"""
# 这句代码虽然看起来字符串换行了，实际是没有换行的
print('春有百花秋有月，'
      '夏有凉风冬有雪，'
      '若无闲事挂心头，'
      '便是人间好时节')


# 三引号定义多行字符串，看着是什么样，实际就是什么样
print("""
春有百花秋有月，
夏有凉风冬有雪，
若无闲事挂心头，
便是人间好时节
""")

# \n：在 python 的字符串中，\n表示换行符
# \t：在 python 的字符串中，\t表示制表符，tab键
print('春有百花秋有月，\n夏有凉风冬有雪，\n若无闲事挂心头，\n便是人间好时节')

print('===========================================')

"""
字符串可以通过下标获取指定位置的字符
字符串可以遍历获取其中的每个字符
"""
#         01234
my_str = 'hello'

# 获取字符串中的 'e' 这个字符
print(my_str[1])
print(my_str[-4])

# 注意：字符串是一个整体，字符串中的字符不能被更改
# 尝试把字符串中的 'e' 改成 'a'
# TypeError: 'str' object does not support item assignment
# my_str[1] = 'a'

# 字符串的遍历
for c in my_str:
      print(c)

# 判断某个字符是否在字符串中
if 'e' in my_str:
      print('e在字符串')
else:
      print('e不在字符串')
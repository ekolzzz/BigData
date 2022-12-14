"""
格式化输出：按照一定的格式将信息打印输出到屏幕上
需求：
    我是学号 XXX 的 XXX，年龄为 XXX，身高为 XXX 米
示例：
    我是学号 000001 的小明，年龄为 18，身高为 1.78 米
    
怎么做格式化输出？需要在字符中挖空，然后填空
%s：在字符串挖一个空，这个空可以被任意类型的数据进行填充
%d：在字符串挖一个空，这个空只能被整数类型的数据进行填充
%f：在字符串挖一个空，这个空只能被小数类型的数据进行填充
"""

# 注意：字符串中空的数量和填充数据的数量必须一致，不能多也不能少
print('我是学号 %s 的 %s，年龄为 %s，身高为 %s 米' % (1, '小明', 18, 1.78))
print('我是学号 %d 的 %s，年龄为 %d，身高为 %f 米' % (1, '小明', 18, 1.78))
# %06d：表示填充的整数宽度占6位，不足6位数前面补0
# %.2f：表示填充的小数保留2位小数，会自动四舍五入
print('我是学号 %06d 的 %s，年龄为 %d，身高为 %.2f 米' % (1, '小明', 18, 1.78))

# 利用变量进行数据填充
# 学号
no = 2
# 姓名
name = "小王"
# 年龄
age = 20
# 身高
height = 1.83
print('我是学号 %06d 的 %s，年龄为 %d，身高为 %.2f 米' % (no, name, age, height))

# 进行格式化输出时，如果只有一个空，则 % 后面的小括号可以省略
print("我的姓名：%s" % (name))
print("我的姓名：%s" % name)


"""
fstring：python3.6版本之后提供了进行字符串格式化的另外一个方式
"""

name = 'smart'
age = 18
height = 1.83
sex = '男'

# 需求：按照如下格式打印信息
# 姓名：smart, 年龄：18, 性别：男, 身高：1.83

"""
传统格式化
%s：在字符串中挖空，可以被任意类型的数据进行填充
%d：在字符串中挖空，只能被整数类型的数据进行填充
%f：在字符串中挖空，只能被小数类型的数据进行填充
"""
print('姓名：%s, 年龄：%d, 身高：%.2f, 性别：%s' % (name, age, height, sex))

"""
fstring格式化
"""
# 注意：fstring字符串前面要添加f或F，注意f或F不要添加在引号里面

print(f'我叫{name}, 年龄为{age}, 身高为{height}, 性别为：{sex}')
print(F'我叫{name}, 年龄为{age}, 身高为{height}, 性别为：{sex}')
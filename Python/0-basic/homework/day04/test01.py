# # 创建一个空字典{}，变量名为 info
# info = {}
#
# # 向字典 info 中添加新的键值对，保存如下信息：姓名是张三
# info['name'] = '张三'
#
# # 获取字典中元素 name 的值
# print(info['name'])
#
# # 修改字典中的元素 'name' 的值为 '李四'
# info['name'] = '李四'
# print(info['name'])
#
# # 存在字典 info = {'name':'李四'}, 删除元素 name
# info.pop('name')
# print(info)

# str = input('输入一个字符串：')
# print(str)
#
# for i in str:
#     if i == "q":
#         break
#     elif i == " ":
#         continue
#     print(i ,end='')

# a = "itheima"
#
# b = input('请输入一个字母：')
#
# for c in a :
#     if c == b:
#       print('找到了')
#       break
#     else:
#         print('查无此字')
#         break

# dict1 = {'name':'chuanzhi','age':18}
# # 1.使用循环将字典中所有的键输出到屏幕上
# for key in dict1:
#     print(key)
# # 2.使用循环将字典中所有的值输出到屏幕上
# for value in dict1.values():
#     print(value)
# # 3.使用循环将字典中所有的键值对输出到屏幕上
# for key, vaule in dict1.items() :
#   print(key,':',vaule, end=' ')

# product = [
#     {"name": "电脑", "price": 7000},
#     {"name": "鼠标", "price": 30},
#     {"name": "usb电动小风扇", "price": 20},
#     {"name": "遮阳伞", "price": 50},
# ]
#
# money = int(input('你有多少钱：'))
# sum_price= 0
#
# for product_dict in product :
#     price = product_dict['price']
#     sum_price += price
#
# print('电脑总价是:%d' % sum_price)
#
# if money >= sum_price :
#     print('你可以买！')
# else:
#     print('你钱不够！')

# words = "abcdefghi"
# res = words[2:7:2] # 从右到左
# res1 = words[-7:-2:2] # 从左到右
#
# print(res)
# print(res1)

#       0123456789
str1 = '1234567890'
#      -10-9-8-7-6-5-4-3-2-1
# - 截取字符串的第一位到第三位的字符：`123`
str2 = str1[0:3:1]
str3 = str1[-10:-7:1]
str2 = str1[:3]

print(str2)
print(str3)

# - 截取字符串最后三位的字符：`890`
str2 = str1[7:10:1]
str3 = str1[7:]
str4 = str1[-3:]

print(str2)
print(str3)
print(str4)

# - 截取字符串的全部字符：`1234567890`
str2 = str1[0:10:1]
str3 = str1[:]

print(str2)
print(str3)

# - 截取字符串的第七个字符到结尾：`7890`
str2 = str1[6:]

print(str2)

# - 截取字符串的第一位到倒数第三位之间的字符：`234567`
str2 = str1[1:-3]

print(str2)

# - 截取字符串的第三个字符：`3`
str2 = str1[2]

print(str2)

# - 截取字符串的倒数第一个字符：`0`
str2 = str1[:-2:-1]

print(str2)

# - 截取与原字符串顺序相反的字符串：`0987654321`
str2 = str1[::-1]

print(str2)

# - 截取字符串倒数第三位与倒数第一位之间的字符：`89`
str2 = str1[-3:-1:1]

print(str2)

# - 截取字符串的第一位字符到最后一位字符之间的字符，每隔一个字符截取一次：`2468`

str2 = str1[1:-2:2]

print(str2)
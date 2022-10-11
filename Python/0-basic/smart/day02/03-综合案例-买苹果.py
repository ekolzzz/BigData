"""
需求：完成一个买苹果的程序，要求用户输入苹果的单价(元/kg)和购买的数量(kg)，计算出总价并按照如下格式输出结果：
    苹果单价XXX元/kg，购买XXXkg，总价为XXX元
"""

"""
思路：
① 提示用户输入苹果的单价和购买的重量：input
② 计算苹果的总价：总价=单价*重量
③ 格式化输出：苹果单价XXX元/kg，购买XXXkg，总价为XXX元
"""

# ① 提示用户输入苹果的单价和购买的重量：input
price = input('请输入苹果的单价(元/kg)：')
weight = input('请输入购买的数量(kg)：')
# print(type(price), price)
# print(type(weight), weight)

# 将 price 和 weight 进行数据类型转换
price = float(price)
weight = float(weight)
# print(type(price), price)
# print(type(weight), weight)

# ② 计算苹果的总价：总价 = 单价 * 重量
total_price = price * weight
# print(total_price)

# ③ 格式化输出：苹果单价XXX元/kg，购买XXXkg，总价为XXX元
print('苹果单价%.2f元/kg，购买%.2fkg，总价为%.2f元' % (price, weight, total_price))


# ① 提示用户输入苹果的单价和购买的重量：input
# 先接收input的数据，然后将input接收的数据使用float函数进行类型转换，再赋值给=号左边的变量
price = float(input('请输入苹果的单价(元/kg)：'))
weight = float(input('请输入购买的数量(kg)：'))

# ② 计算苹果的总价：总价 = 单价 * 重量
total_price = price * weight

# ③ 格式化输出：苹果单价XXX元/kg，购买XXXkg，总价为XXX元
print('苹果单价%.2f元/kg，购买%.2fkg，总价为%.2f元' % (price, weight, total_price))



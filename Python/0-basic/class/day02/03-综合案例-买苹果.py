"""
需求：完成一个买苹果的程序，要求用户输入苹果的单价(元/kg)和购买的数量(kg)，计算出总价并按照如下格式输出结果：
    苹果单价XXX元/kg，购买XXXkg，总价为XXX元
"""

"""
思路：
1、提示用户输入数据
2、计算苹果的总价：总价 = 单价 * 数量
3、格式化输出： 苹果单价XXX元/kg，购买XXXkg，总价为XXX元
"""

# 1、提示用户输入数据
price = float(input('请输入苹果的单价：'))
weight = float(input('请输入苹果的重量：'))

# 2、计算苹果的总价：总价 = 单价 * 数量
total_price = price * weight

# 3、格式化输出： 苹果单价XXX元/kg，购买XXXkg，总价为XXX元
print('苹果单价 %.2f 元/kg，购买 %.2f kg，总价为 %.2f 元' % (price, weight, total_price))
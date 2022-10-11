"""
有这样的一个列表

product = [
    {"name": "电脑", "price": 7000},
    {"name": "鼠标", "price": 30},
    {"name": "usb电动小风扇", "price": 20},
    {"name": "遮阳伞", "price": 50},
]

然后小明一共有8000块钱，那么他能不能买下这所有商品？ 如果能，请输出“能”，否则输出“不能”
"""

product = [
    {"name": "电脑", "price": 7000},
    {"name": "鼠标", "price": 30},
    {"name": "usb电动小风扇", "price": 20},
    {"name": "遮阳伞", "price": 50},
]

money = 8000
sum = 0

for dict1 in product:
    sum += dict1['price']

if money >= sum:
    print('能')
else:
    print('不能')
"""
while循环应用
"""
"""
需求：计算1~100的累加和（包含1和100）
"""
# i = 1
# sum =0
# while i <=100 :
#     sum += i
#     i += 1
# print(sum)

"""
需求：计算1~100之间偶数的累加和-方式1
"""

# i = 2
# sum =  0
# while i <= 100 :
#     sum += i
#     i += 2
# print(sum)

"""
需求：计算1~100之间偶数的累加和-方式2
"""

i = 1
sum = 0

while i <= 100 :
    if i % 2 == 0 :
        sum += i
    i += 1
print(sum)














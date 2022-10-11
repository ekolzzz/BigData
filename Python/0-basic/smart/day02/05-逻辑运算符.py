"""
and	x and y	布尔"与"：如果 x 为 False，x and y 返回 False，否则它返回 y 的值。	True and False， 返回 False。
or	x or y	布尔"或"：如果 x 是 True，它返回 True，否则它返回 y 的值。	False or True， 返回 True。
not	not x	布尔"非"：如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not True 返回 False, not False 返回 True
"""

# 左右两边都为True，结果才为True
print(True and True) # True

# 结果：???
# 5 > 3 -> True
# 4 < 3 -> False
# True and False
print((5 > 3) and (4 < 3)) # False

# 左右两边任意一边为True，结果就为True
print(False or True) # True

# 结果：???
# 1 == 1：True
# 1 > 3：False
# True or False
print((1 == 1) or (1 > 3)) # True

# 取反：not True 为 False，not False 为 True
print(not True) # False

# 结果：???
# 1 == 1：True
# not True -> False
print(not (1 == 1)) # False


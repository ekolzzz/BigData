"""
列表嵌套：一个列表中的每个元素数据也是一个列表
"""

school_list = [['北京大学', '清华大学'], ['中山大学', '华南理工大学'], ['哈工大', '哈工程']]

# 思考：如何获取出'华南理工大学'?
# 1. 从 school_list 获取 ['中山大学', '华南理工大学']
print(school_list[1])

# 2. 从 school_list[1] 获取 华南理工大学
print(school_list[1][1])


# 练习：如何获取出'哈工大'?
print(school_list[2][0])
print(school_list[-1][-2])
print(school_list[-1][0])
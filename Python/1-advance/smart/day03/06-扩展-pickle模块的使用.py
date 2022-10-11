"""
pickle模块的使用：
* pickle.dumps(数据)：将数据转换为可以写入到文件中的一个二进制bytes数据
* pickle.loads(二进制bytes数据)：将二进制bytes数据恢复成原来的数据
"""
# 导入模块
import pickle

class Student(object):
    """学生类"""
    def __init__(self, _name, _age, _tel):
        """学生对象初始化方法，给创建的学生对象添加初始的属性"""
        self.name = _name
        self.age = _age
        self.tel = _tel

    def __str__(self):
        """返回一个字符串，包含学生对象的姓名、年龄、电话"""
        return f'姓名：{self.name}，' \
               f'年龄：{self.age}，' \
               f'电话：{self.tel}'


stu_list = []
stu1 = Student('smart', 18, '138')
stu2 = Student('linda', 16, '135')
stu_list.append(stu1)
stu_list.append(stu2)
print(stu_list)

# 需求1：直接将 stu_list 数据写入到文件
with open('./test.pickle', 'wb') as f:
    content = pickle.dumps(stu_list) # bytes
    f.write(content)

# 需求2：从 test.pickle 中加载数据
with open('./test.pickle', 'rb') as f:
    content = f.read()
    stu_list = pickle.loads(content)
    print(type(stu_list), stu_list)

for stu in stu_list:
    print(stu.name, stu.age, stu.tel)

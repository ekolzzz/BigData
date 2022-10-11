# 导入 pymysql 模块
import pymysql

# 创建数据库连接
conn = pymysql.connect(host='localhost', port=3306,
                       database='winfunc', user='root',
                       password='123456', charset='utf8')

# 获取游标
cursor = conn.cursor()

sql = 'select * from students'
num = cursor.execute(sql)
print(f'查询到了{num}行')

# 准备执行的 SQL 语句
sql = "INSERT INTO students VALUES (6, 'rose', 'Female', 93)"

# 使用游标执行 SQL 语句
row_count = cursor.execute(sql)
print("SQL语句执行影响的行数：%d" % row_count)

# 获取 SQL 查询的所有结果
sql = "SELECT * FROM students"
cursor.execute(sql)
res = cursor.fetchall()
print(res)

# 准备执行的 SQL 语句
sql = "INSERT INTO students VALUES (7, 'jack', 'Male', 99)"
cursor.execute(sql)

# 获取 SQL 查询的所有结果
sql = "SELECT * FROM students"
cursor.execute(sql)
res = cursor.fetchall()
print(res)

# 关闭游标
cursor.close()

# 关闭连接
conn.close()
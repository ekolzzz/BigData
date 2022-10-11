# 导入 pymysql 模块
import pymysql

# 创建数据库连接
conn = pymysql.connect(host='localhost', port=3306,
                       user='root', password='mysql',
                       database='winfunc', charset='utf8')

# 获取游标
cursor = conn.cursor()

# 准备执行的 SQL 语句
sql = "INSERT INTO students VALUES (6, 'rose', 'Female', 93)"

# 自动开启一个事务
# conn.begin()

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

# 事务提交
conn.commit()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()
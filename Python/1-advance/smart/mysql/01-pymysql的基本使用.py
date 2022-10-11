# 导入 pymysql
import pymysql

# 创建一个数据库的连接对象
conn = pymysql.connect(host='localhost', port=3306,
                       database='winfunc', user='root',
                       password='mysql', charset='utf8')
# <class 'pymysql.connections.Connection'>
# print(type(conn), conn)

# 创建一个游标对象（执行SQL）
cursor = conn.cursor()
# <class 'pymysql.cursors.Cursor'>
# print(type(cursor), cursor)

# 通过游标对象执行指定的 SQL
sql = 'select * from students'
num = cursor.execute(sql)
print(f'查询到了{num}行')

# 关闭游标
cursor.close()
# 关闭连接
conn.close()

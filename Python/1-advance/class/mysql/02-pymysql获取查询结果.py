# 1) 引入模块
# 导入 pymysql 扩展包
import pymysql


# 2） 创建连接(创建connection连接对象)
# 作用：用于和数据库建立连接，调用pymysql模块中的connect()方法

# 创建一个数据库的连接对象
conn = pymysql.connect(host='localhost', port=3306,
                       database='winfunc', user='root',
                       password='123456', charset='utf8')
# 参数说明：
# * 参数host：连接的mysql主机，如果本机是'localhost'
# * 参数port：连接的mysql主机的端口，默认是3306
# * 参数database：数据库的名称
# * 参数user：连接的用户名
# * 参数password：连接的密码
# * 参数charset：通信采用的编码方式，推荐使用utf8

# <class 'pymysql.connections.Connection'>
# print(type(conn), conn)

# 创建一个游标对象 (执行SQL)
cursor = conn.cursor()
# <class 'pymysql.cursors.Cursor'>
# print(type(cursor), cursor)

# 通过游标对象执行指定的 SQL
sql = 'select * from students'
num = cursor.execute(sql)
print(f'查询到了{num}行')

# fetchall()：获取查询的所有结果，返回值为tuple元祖类型【嵌套元祖】
# fetchone()：每次获取查询结果中的一条记录，返回值为tuple元祖类型【简单元祖】
# fetchmany(num)：每次获取查询结果中的num条记录，返回值为tuple元祖类型【嵌套元祖】
# 都是从上一次读到的位置继续往下读
res = cursor.fetchall()
print(res) # --> 嵌套元组

res = cursor.fetchone()
print(res) # --> 简单元组

res = cursor.fetchmany(2)
print(res) # --> 嵌套元组

# 关闭游标
cursor.close()
# 关闭连接
conn.close()


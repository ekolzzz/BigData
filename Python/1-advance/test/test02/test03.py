from pymysql import connect


def main():
    # 创建数据库连接对象
    conn = connect(host='localhost', port=3306,
                   database='python', user='root', password='mysql')
    # 创建游标对象
    cursor = conn.cursor()
    # 循环向 test_index 表中添加 10 万条测试数据
    for i in range(100000):
        cursor.execute("insert into test_index values('py-%d')" % i)
    # 提交数据
    conn.commit()
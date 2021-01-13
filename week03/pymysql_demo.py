import pymysql
import pretty_errors
from loguru import logger
from dbconfig import read_db_config
from pathlib import Path

db_file = Path(__file__).parent/'config.ini'
db_serverInfo = read_db_config(db_file)
db = pymysql.connect(**db_serverInfo)
# db = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='za261016',
#     database='test_db')

try:
    
    # 使用cursor() 方法创建一个游标对象 cursor
    with db.cursor() as cursor:
        # sql = '''select version();'''
        query_sql = '''select name from book;'''
        # update_sql = '''update book set name= %s where id = %s'''
        # delete_sql = '''delete from book where name= %s'''
        # insert_sql = 'INSERT INTO book (id, name) VALUES (%s, %s)'
        # value = (1002,"西游记")
        # values = (
        #     (1003, "红楼梦"),
        #     (1004, "水浒传"),
        #     (1005, "大学"),
        #     (1006, "中庸"),
        #     (1007, "史记"),
        #     (1008, "论语"),
        #     )
        # 使用execute() 方法执行sql查询
        # cursor.executemany(insert_sql, values)
        cursor.execute(query_sql)
        # result = cursor.fetchone()
        all_result = cursor.fetchall()  # 返回的是一个元组
    db.commit()
except Exception as e:
    logger.error(e)
finally:
    # 关闭数据库
    db.close()
    print(cursor.rowcount)

# print(f"database version: {all_result}")
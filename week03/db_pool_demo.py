import pymysql
from dbutils.pooled_db import PooledDB

db_config = {
    "host": "localhost", 
    "db": "test_db", 
    "user": "root", 
    "passwd": "za261016", 
    "port": 3306, 
    "charset": "utf8mb4", 
    "maxconnections": 0,    # 连接池允许的最大连接数
    "mincached": 4,         # 初始化时连接池中至少创建的空闲的连接, 0表示不创建
    "maxcached": 0,         # 连接池中最多闲置的连接, 0表示不限制
    "maxusage": 5,          # 每个连接最多被重复使用的次数, None表示无限制
    "blocking": True,          # 连接池中如果没有可用连接后是否阻塞等待; True 等待, False 不等待然后报错；
}

spool = PooledDB(pymysql, **db_config)

conn = spool.connection()
cur = conn.cursor()
SQL = 'select * from bookorm;'
cur.execute(SQL)
f = cur.fetchall()
print(f)
cur.close()
conn.close()

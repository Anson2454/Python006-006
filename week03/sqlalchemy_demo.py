import pymysql
from sqlalchemy import MetaData, String, Integer, Table, create_engine, ForeignKey, Column
from sqlalchemy.ext.declarative import declarative_base

db_url = 'mysql+pymysql://root:za261016@localhost:3306/test_db'
# echo=True 开启调试,一般用于开发环境
engine = create_engine(db_url, echo=True)

# 创建元数据
metadata = MetaData(engine)

book_table = Table('book',metadata,
                   Column('id',Integer, primary_key=True),
                   Column('name',String(20))
                   )

auth_table = Table('author',metadata,
                   Column('id', Integer, primary_key=True),
                   Column('book_id', None, ForeignKey('book.id')),
                   Column('author', String(128), nullable=False)
                   )

try:
    metadata.create_all()
except Exception as e:
    print(f'create error: {e}')
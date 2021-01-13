import pymysql
from sqlalchemy import MetaData, String, Integer, Table, create_engine, \
    ForeignKey, Column, DateTime, desc, func, and_, or_, not_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime



Base = declarative_base()
'''
其他数据类型及约束条件
Float, Decimal, Boolen, Text
autoincrement
'''

class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(50), index=True)
    
    def __repr__(self):
        return "Book_table(book_id='{self.book_id}',book_name={self.book_name})".format(self=self)

class Author_table(Base):
    __tablename__ = 'authororm'
    user_id = Column(Integer(), primary_key=True)
    user_name = Column(String(20), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now,onupdate=datetime.now)





# 实例化一个引擎
db_url = 'mysql+pymysql://root:za261016@localhost:3306/test_db?charset=utf8mb4'
engine = create_engine(db_url,echo=True, encoding="utf-8")

# 创建session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 增加数据
book_demo1 = Book_table(book_name = '哈利波特1')
book_demo2 = Book_table(book_name = '哈利波特2')
book_demo3 = Book_table(book_name = '哈利波特3')
# author_demo = Author_table(user_name = '东野圭吾')
# print(author_demo)
# Base.metadata.create_all(engine)


# session.add(book_demo1)
# session.add(book_demo2)
# session.add(book_demo3)
# session.flush()

# result = session.query(Book_table).all()
# for result in session.query(Book_table).all():
#     print(result)
# result = session.query(Book_table).first()
# one()  超过一行会抛异常
# scalar() 超过一行会抛异常


# 指定列数
# result=session.query(Book_table.book_name).first()

# 查询&排序
# for result in session.query(Book_table.book_id,Book_table.book_name).order_by(desc(Book_table.book_id)):
#     print(result)

# query_result = session.query(Book_table).order_by(desc(Book_table.book_id)).limit(2)
# print([result.book_name for result in query_result])

# result = session.query(func.count(Book_table.book_name)).first()
# print(result)

# results = session.query(Book_table).filter(Book_table.book_id < 10 ).all()
# results = session.query(Book_table).filter(
#     and_(
#         Book_table.book_id < 10 ,
#         Book_table.book_id >2
#         )
#     ).all()
# for result  in  results:
#     print(result.book_id)
    
# 更新

# query = session.query(Book_table)
# query = query.filter(Book_table.book_id == 1)
# query.update({Book_table.book_name: '(新)七宗罪'})
# new_book = query.first()
# print(new_book.book_name)

# 删除    
query = session.query(Book_table)
query = query.filter(Book_table.book_id == 12)
# session.delete(query.one())

query.delete()
print(query.first())


session.commit()

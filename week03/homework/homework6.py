import pymysql
from sqlalchemy import MetaData, String, Integer, DECIMAL, Table, create_engine, \
    ForeignKey, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True,autoincrement=True)
    name = Column(String(20),nullable=False)
    created_at = 
    updated_at =
    
    def __repr__(self):
        return "user(id = {self.id},name = {self.name})".format(self=self)
            
class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer(),primary_key=True,autoincrement=True)
    user_id = Column(ForeignKey('user.id'))
    account = Column(DECIMAL(20,2))
    
    
    def __repr__(self):
        return "Account(id = {self.id},user_id = {self.user_id}, \
        account = {self.account})".format(self=self)
    
class trans(Base):
    __tablename__ = 'trans_detail'
    id = Column(Integer(),primary_key=True)
    own_id = Column()
    target_id = Column()
    trans_amount = Column(DECIMAL(20,2))
    trans_date = Column(Datetime(), default=datetime.now)
    
    def __repr__(self):
        return "Table(id = {self.id},name = {self.name})".format(self=self)


# 实例化一个引擎
db_url = 'mysql+pymysql://root:za261016@localhost:3306/test_db?charset=utf8mb4'
engine = create_engine(db_url,echo=True, encoding="utf-8")

Base.metadata.create_all(engine)
# 创建session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()
 
table2_data1 = Table2(id=1,name='table1_table2') 
session.add(table2_data2)    


session.commit()




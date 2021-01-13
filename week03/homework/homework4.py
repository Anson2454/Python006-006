import pymysql
from sqlalchemy import MetaData, String, Integer, Table, create_engine, \
    ForeignKey, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()



class Table1(Base):
    __tablename__ = 'Table1'
    id = Column(Integer(), primary_key=True)
    name = Column(String(20))
    
    def __repr__(self):
        return "Table(id = {self.id},name = {self.name})".format(self=self)
            
class Table2(Base):
    __tablename__ = 'Table2'
    id = Column(Integer(),primary_key=True)
    name = Column(String(20))
    
    def __repr__(self):
        return "Table(id = {self.id},name = {self.name})".format(self=self)


# 实例化一个引擎
db_url = 'mysql+pymysql://root:za261016@localhost:3306/test_db?charset=utf8mb4'
engine = create_engine(db_url,echo=True, encoding="utf-8")

Base.metadata.create_all(engine)
# 创建session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# table1_data1 = Table1(id=1,name='table1_table2')
# table1_data2 = Table1(id=2,name='table1')
# session.add(table1_data1)   
# session.add(table1_data2)    
table2_data1 = Table2(id=1,name='table1_table2')
table2_data2 = Table2(id=3,name='table2')
session.add(table2_data1)   
session.add(table2_data2)    


session.commit()




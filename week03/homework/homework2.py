import pymysql
from sqlalchemy import MetaData, String, Integer, Boolean, Table, create_engine, \
    ForeignKey, Column, DateTime, desc, func, and_, or_, not_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from  faker import Faker
import random

# 初始化Faker实例，默认设置中文
f=Faker("zh_CN")

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    user_id = Column(Integer(), primary_key=True, autoincrement=True)
    user_name = Column(String(20), index=True, nullable=False,unique=True)
    age = Column(Integer())
    birth = Column(DateTime())
    gender = Column(String(10))
    degree = Column(String(20))
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now,onupdate=datetime.now)
    
    def __repr__(self):
        return "Student(user_id = {self.user_id},\
            user_name = {self.user_name},\
            age = {self.age},\
            birth = {self.birth},\
            gender = {self.gender},\
            degree = {self.degree}\
            )".format(self=self)


# 实例化一个引擎
db_url = 'mysql+pymysql://root:za261016@localhost:3306/test_db?charset=utf8mb4'
engine = create_engine(db_url,echo=True, encoding="utf-8")

Base.metadata.create_all(engine)
# 创建session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 插入数据
for i in range(3):
    student = Student(
        user_name = f.name(),
        age = f.random_int(18,100),
        birth = f.date_object(),
        gender = random.choice(["F","M","O"]),
        degree = random.choice(["初中", "高中", "本科", "硕士", "博士", "博士后"]),
        )
    # print(student)
    # session.add(student)
    # session.commit()
    
# 查询数据
query = session.query(Student).all()
for result in query:
    print(result)

session.commit()




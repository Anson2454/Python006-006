import pymysql
from sqlalchemy import MetaData, String, Integer, Float, Table, create_engine, \
    ForeignKey, Column, DateTime,DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from loguru import logger

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True,autoincrement=True)
    name = Column(String(20),nullable=False)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now,onupdate=datetime.now)
    
    def __repr__(self):
        return "user(id = {self.id},name = {self.name})".format(self=self)
            
class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer(),primary_key=True,autoincrement=True)
    user_id = Column(ForeignKey('user.id'))
    account = Column(DECIMAL(20,2),default = 0.00)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now,onupdate=datetime.now)
    
    def __repr__(self):
        return "Account(id = {self.id},user_id = {self.user_id}, \
        account = {self.account})".format(self=self)
    
class Trans(Base):
    __tablename__ = 'trans_detail'
    id = Column(Integer(),primary_key=True)
    own_id = Column(Integer())
    target_id = Column(Integer())
    trans_amount = Column(DECIMAL(20,2))
    trans_date = Column(DateTime(), default=datetime.now)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now,onupdate=datetime.now)
    def __repr__(self):
        return "Table(target_id = {self.target_id},\
            own_id = {self.own_id},trans_amount = {self.trans_amount},\
            trans_date = {self.trans_date})".format(self=self)


# 实例化一个引擎
# db_url = 'mysql+pymysql://root:za261016@localhost:3306/test_db?charset=utf8mb4'
# engine = create_engine(db_url,echo=True, encoding="utf-8")

# Base.metadata.create_all(engine)

# # 创建session
# SessionClass = sessionmaker(bind=engine)
# session = SessionClass()

# user = User(name='王五')
# account = Account(user_id=3,account= 500.00)
# session.add(account)
# session.commit()




class TransEvent():
    # 输入条件：转账人，目标转账人，转账金额
    def __init__(self, own_id, target_id, trans_amount=0.00):
        # 实例化一个引擎
        db_url = 'mysql+pymysql://root:za261016@localhost:3306/test_db?charset=utf8mb4'
        engine = create_engine(db_url, encoding="utf-8")
        # Base.metadata.create_all(engine)
        
        # 创建session
        SessionClass = sessionmaker(bind=engine)
        self.session = SessionClass()

        self.own_id = int(own_id)
        self.target_id = int(target_id)
        self.trans_amount = float(trans_amount)
        
    def trans_event(self):
        global account_query,targetUser_query,ownUser_query
        # 先判断目标转账用户是否存在
        try:
            user_query = self.session.query(User)
            targetUser_query = user_query.filter(User.id==self.target_id)
            ownUser_query = user_query.filter(User.id==self.own_id)
            # 判断输入的用户ID是否存在
            if targetUser_query.first() and ownUser_query.first():
                if targetUser_query.first().id != ownUser_query.first().id:
                    # 查询转账用户账户余额；若不足，提示余额不足; 
                    account_query = self.session.query(Account)
                    account_query = account_query.filter(Account.user_id==self.own_id)
                    # print(account_query.first().account)
                    if account_query.first().account >= self.trans_amount:
                    # 插入转账明细,更新目标转账用户账户余额
                        try:
                            # 先插入 trans_detail 
                            trans_detail = Trans(
                                own_id = self.own_id,
                                target_id=self.target_id,
                                trans_amount=self.trans_amount)
                            query =  self.session.add(trans_detail)
                            self.session.commit()
                        except Exception as e:
                            logger.error(f'转账明细插入失败:{e}')
                        try:
                            # 更新账户余额
                            account_query = self.session.query(Account)  
                            # 更新转账用户余额
                            own_account_query = account_query.filter(Account.user_id==self.own_id)
                            own_new_account = float(own_account_query.first().account) - self.trans_amount
                            print(f'转账用户余额:{own_new_account}')
                            own_account_query.update({Account.account:own_new_account})
                            # 更新目标用户余额
                            target_account_query = account_query.filter(Account.user_id==self.target_id)
                            target_new_account = float(target_account_query.first().account) +  self.trans_amount
                            print(f'目标用余额:{target_new_account}')
                            target_account_query.update({Account.account:target_new_account})
                        except Exception as e:
                            logger.error(f'更新余额失败{e}')
                    else:
                        logger.error('转账用户余额不足')
                else:
                    logger.error('不能给自己转账') 
            else:
                if targetUser_query.first():        
                    logger.error("转账用户不存在")
                else:
                    logger.error('目标转账用户不存在')
        except Exception as e:
            logger.error(f'转账失败:{e}')    
        finally:
            self.session.commit()
        
       
if __name__ == "__main__":
    try:
        trans=TransEvent(1,2,50.5555)
        trans.trans_event()
    except Exception as e:
        logger.error(f'输入错误,输入要求: 转账用户ID(int),目标用户ID(int), 转账金额(float)')


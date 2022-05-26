from email.mime import base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from Base import Base
engine = create_engine('sqlite:///test.db', echo=True)
from ContractHandler import ContractHandler


class LoanSchema(Base):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)

class LoanContract(ContractHandler):
    def __init__(self):
        super()
    
    def create(self):
        self.schema
        loan = LoanSchema(name='ed', fullname='Ed Jones', nickname='edsnickname')
        self.updateState(loan)
        


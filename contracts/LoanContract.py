from email.mime import base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from Base import Base
from entity.LoanSchema import LoanSchema
from entity.User import User

engine = create_engine('sqlite:///test.db', echo=True)
from ContractHandler import ContractHandler


# class LoanSchema(Base):
#     __tablename__ = 'loans'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     fullname = Column(String)
#     nickname = Column(String)
#     def __repr__(self):
#        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
#                             self.name, self.fullname, self.nickname)

class LoanContract(ContractHandler):
    def __init__(self,session):
        self.session=session
        super()
    
    def create(self):
        loan = LoanSchema(name='ed', fullname='Ed Jones', nickname='edsnickname')
        self.updateState(loan)
        wrongEntity= User(name='ed', fullname='Ed Jones', nickname='edsnickname')
        self.updateState(wrongEntity)




from entity.BaseEntity import BaseEntity
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String

class LoanSchema(BaseEntity):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)
    def belongsToContract(self):
        return ["LoanContract"]


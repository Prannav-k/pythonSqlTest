from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String


from entity.BaseEntity import BaseEntity


class User(BaseEntity):
    def belongsToContract(self):
        return ["BondContract"]

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)


from email.mime import base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from Base import Base
engine = create_engine('sqlite:///test.db', echo=True)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)




# Session = sessionmaker(bind=engine)
# session = Session()


# ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')

# session.add(ed_user)
# session.commit()
# session.close()
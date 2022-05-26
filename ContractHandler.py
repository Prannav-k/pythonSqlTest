from email.mime import base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from Base import Base


class ContractHandler:
    def __init__(self, session):
        self.session = session

    def updateState(self, state):
        #who is calling it, do they have state type in thier schema
        self.session.add(state)
        self.session.commit()


    


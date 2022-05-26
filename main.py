from email.mime import base
import importlib
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from Base import Base
engine = create_engine('sqlite:///test.db', echo=True)
from contracts.LoanContract import LoanContract

import sys
import inspect
from pathlib import Path


contracts = os.listdir('contracts')
# contracts = filter(lambda migration: '.py' in migration, contracts)
for contract in contracts:
    contract = contract.replace('.py', '')
    contract = importlib.import_module('contracts' + '.' + contract)

Base.metadata.create_all(engine)

engine = create_engine('sqlite:///test.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

lc = LoanContract(session=session)
lc.create()
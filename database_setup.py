from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	id = Column('user_id', Integer, primary_key = True)
	name = Column(String)
	email = Column(String, primary_key=True)  
	password = Column(String)

def __init__(self, name, email, password):
   self.name = name
   self.email = email
   self.password = password
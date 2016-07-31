from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	id = Column('user_id', Integer, primary_key = True)
	name = Column(String(100))
	email = Column(String(50))  
	password = Column(String(200))

def __init__(self, name, email, password):
   self.name = name
   self.email = email
   self.password = password
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()



class User(Base):
    __tablename__ = 'Users'
    username = Column(String, primary_key=True)
    email = Column(String)
    hashed_password = Column(String)

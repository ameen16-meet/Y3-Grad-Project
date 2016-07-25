from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Person(Base):
    __tablename__ = 'user'
    name = Column(String)
    id = Column(Integer, primary_key=True)
    gender = Column(String)
    nationality = Column(String)
    hometown = Column(String)


from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Person(Base):
    __tablename__ = 'user'
    name = Column(String)
    id = Column(Integer, primary_key=True)
    email = Column(email)
    password = Column(password)
    XP = Column(Integer)
    coins = Column(Integer)
    nationalfrom flask import Flask, render_template
	app = Flask(__name__)

#users = 
#[
#    {
#       
#  }
#]

@app.route('/')
def index():
  return render_template('index.html', users=users)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html')

if __name__ == '__main__':
  app.run(debug=True)ity = Column(String)
    hometown = Column(String)

